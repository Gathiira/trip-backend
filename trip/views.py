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
					date = process_request.date_created

					notification_message = notification.start_trip_notification_message.\
						format(title, reference_number, date)

					message_payload = {
						"email_subject":"SMOKIN ACE UPDATES",
						"email_body":notification_message,
						"to_email":users
					}
					
					notification.broad_cast_system_notification(
						message_payload
					)
				except Exception as e:
					print(e)
					transaction.set_rollback(True)
					return Response(
						{"details":"Failed to send notifications"},
						status = status.HTTP_400_BAD_REQUEST)

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

