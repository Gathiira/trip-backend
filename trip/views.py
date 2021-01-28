from django.db import transaction

from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response

from shared_functions import (
	notifications,
	utility_functions
)
from trip import models as trip_models
from trip import serializers as trip_serializers

from accounts import models as account_models

utility_function = utility_functions
notification = notifications.NotificationClass()


class TripViewSet(viewsets.ModelViewSet):
	
	@action(
		methods=['POST'],
		detail=False,
		url_path='start-trip',
		url_name='start-trip'
	)
	def start_trip(self, request):
		payload = request.data
		serializer = trip_serializers.TripLoadingRequestSerializer(
			data=payload, many=False
		)

		if serializer.is_valid():
			with transaction.atomic():
				title = payload['title']
				reference_number = utility_function.\
				unique_reference_number_generator(
					model=trip_models.TripRequest,
					process_prefix='TRIP'
				)

				try:
					trip_payload = {
						"title":title,
						"reference_number":reference_number,
						"status":"ONGOING",
					}
					process_request = trip_models.TripRequest\
						.objects.create(**trip_payload)

				except Exception as e:
					print(e)
					transaction.set_rollback(True)
					return Response(
						{"details":"Failed to start the trip"},
						status = status.HTTP_400_BAD_REQUEST)

				buying_price_per_kg = payload['buying_price_per_kg']
				total_weight_bought = payload['total_weight_bought']
				total_buying_price = buying_price_per_kg * total_weight_bought
				loading_cost = payload['loading_cost']
				departure_date = payload['departure_date']

				try:
					loading_payload = {
						"process_request":process_request,
						"buying_price_per_kg":buying_price_per_kg,
						"total_weight_bought":total_weight_bought,
						"total_buying_price":total_buying_price,
						"loading_cost":loading_cost,
						"departure_date":departure_date
					}
					trip_models.TripLoading.objects.create(
						**loading_payload
					)

				except Exception as e:
					print(e)
					transaction.set_rollback(True)
					return Response(
						{"details":"Failed to start the trip"},
						status = status.HTTP_400_BAD_REQUEST)


				try:
					# send emails notification
					users = list(account_models.User.objects.values_list('email', flat=True))
					title = process_request.title
					reference_number = process_request.reference_number
					subject = notification.trip_notification_subject

					notification_message = notification.start_trip_notification_message.\
						format(title, reference_number, departure_date, total_buying_price)

					message_payload = {
						"email_subject":subject,
						"email_body":notification_message,
						"to_email":users
					}
					
					notification.broad_cast_system_notification(
						message_payload
					)
				except Exception as e:
					print(e)
					pass

				respose_info = {
					"details":"Trip successfully started",
					"request_id":process_request.id
				}

				return Response (
					respose_info, status=status.HTTP_201_CREATED
				)

		else:
			return Response(
				serializer.errors,
				status = status.HTTP_400_BAD_REQUEST)


	@action(
		methods=['GET'],
		detail=False,
		url_path='detail-view',
		url_name='detail-view'
	)
	def detail_view(self, request):
		payload = request.query_params.dict()
		serializer = trip_serializers.GenericRequestSerializer(
			data=payload, many=False
		)

		if serializer.is_valid():
			request_id = payload['request_id']
			filter_params = {
                "id": request_id
            }

			try:
				process_request = trip_models.TripRequest.\
					objects.get(**filter_params)
			except Exception as e:
				print(e)
				return Response(
					{"details":"Invalid Trip request"},
					status=status.HTTP_400_BAD_REQUEST
				)

			record_details = trip_serializers.TripDetailSerializer(
				process_request, many=False
			)

			return Response(
				record_details.data, status=status.HTTP_200_OK
			)

		else:
			return Response(
				serializer.errors,
				status = status.HTTP_400_BAD_REQUEST)


	@action(
		methods=['POST'],
		detail=False,
		url_path='end-trip',
		url_name='end-trip'
	)
	def end_trip(self, request):
		payload = request.data
		serializer = trip_serializers.TripOffloadingRequestSerializer(
			data=payload, many=False
		)

		if serializer.is_valid():
			with transaction.atomic():
				request_id = payload['request_id']
				filter_params = {
					"id":request_id
				}

				try:
					process_request = trip_models.TripRequest\
						.objects.get(**filter_params)

				except Exception as e:
					print(e)
					transaction.set_rollback(True)
					return Response(
						{"details":"Invalid Trip Request"},
						status = status.HTTP_400_BAD_REQUEST)
				
				trip_status = process_request.status
				if trip_status=='CLOSED':
					transaction.set_rollback(True)
					return Response(
						{"details": "Trip already closed"},
						status=status.HTTP_400_BAD_REQUEST)


				selling_price_per_kg = payload['selling_price_per_kg']
				total_weight_sold = payload['total_weight_sold']
				total_selling_price = selling_price_per_kg * total_weight_sold
				offloading_cost = payload['offloading_cost']
				selling_date = payload['selling_date']

				try:
					loading_payload = {
						"process_request":process_request,
						"selling_price_per_kg":selling_price_per_kg,
						"total_weight_sold":total_weight_sold,
						"total_selling_price":total_selling_price,
						"offloading_cost":offloading_cost,
						"selling_date":selling_date
					}
					trip_models.TripOffloading.objects.create(
						**loading_payload
					)

				except Exception as e:
					print(e)
					transaction.set_rollback(True)
					return Response(
						{"details":"Failed to end the trip"},
						status = status.HTTP_400_BAD_REQUEST)

				transport_cost = payload['transport_cost']
				clearance_cost = payload['clearance_cost']
				broker_cost = payload['broker_cost']

				try:
					expense_payload = {
						"process_request":process_request,
						"transport_cost":transport_cost,
						"clearance_cost":clearance_cost,
						"broker_cost":broker_cost
					}

					trip_models.TripExpense.objects.create(
						**expense_payload
					)

				except Exception as e:
					print(e)
					transaction.set_rollback(True)
					return Response(
						{"details":"Failed to end the trip"},
						status = status.HTTP_400_BAD_REQUEST)

				
				loading_cost = process_request.\
					trip_loading_details.loading_cost
				
				total_buying_price = process_request.\
					trip_loading_details.total_buying_price

				total_expense = transport_cost + clearance_cost \
					 + broker_cost + loading_cost + offloading_cost + total_buying_price

				profit_margin = total_selling_price - total_expense

				process_request.total_expense = total_expense
				process_request.profit_margin = profit_margin
				process_request.status = 'CLOSED'
				process_request.save()

				user_emails = []
				try:
					users = account_models.User.objects.all()
					for user in users:
						percentage = user.percentage

						user_id = user.id
						profit_share = (percentage/100) * profit_margin

						share_payload = {
							"process_request":process_request,
							"user":user_id,
							"profit_share":profit_share
						}
						email = user.email

						user_emails.append(email)

						trip_models.TripShare.objects.create(
							**share_payload
						)

				except Exception as e:
					print(e)
					transaction.set_rollback(True)
					return Response(
						{"details":"Failed to calculate and record shares"},
						status = status.HTTP_400_BAD_REQUEST)

				try:
					# send emails notification
					title = process_request.title
					reference_number = process_request.reference_number
					subject = notification.trip_notification_subject

					notification_message = notification.end_trip_notification_message.\
						format(title, reference_number, selling_date, total_expense, profit_margin)

					message_payload = {
						"email_subject":subject,
						"email_body":notification_message,
						"to_email":user_emails
					}
					
					notification.broad_cast_system_notification(
						message_payload
					)
				except Exception as e:
					print(e)
					pass

				respose_info = {
					"details":"Trip closed successfully"
				}

				return Response (
					respose_info, status=status.HTTP_201_CREATED
				)

		else:
			return Response(
				serializer.errors,
				status = status.HTTP_400_BAD_REQUEST)

	@action(
		methods=['DELETE'],
		detail=False,
		url_path='delete-trip',
		url_name='delete-trip'
	)
	def delete_trip(self, request):
		payload = request.query_params.dict()
		serializer = trip_serializers.GenericRequestSerializer(
			data=payload, many=False
		)

		if serializer.is_valid():
			request_id = payload['request_id']
			filter_params = {
                "id": request_id
            }

			try:
				process_request = trip_models.TripRequest.\
					objects.get(**filter_params)
			except Exception as e:
				print(e)
				return Response(
					{"details":"Invalid Trip request"},
					status=status.HTTP_400_BAD_REQUEST
				)

			process_request.delete()

			return Response(
				{"details":"Trip record deleted successfully"},
				status=status.HTTP_200_OK
			)
		else:
			return Response(
				serializer.errors,
				status = status.HTTP_400_BAD_REQUEST)
