from rest_framework import serializers

from trip import models as trip_models
from accounts import models as account_models


# generic serializers
class GenericRequestSerializer(serializers.Serializer):
	request_id = serializers.CharField(required=True)

class UserSerializer(serializers.Serializer):
	username = serializers.CharField()

#  creating requests serializers
class TripRequestSerializer(serializers.Serializer):
	title = serializers.CharField(
		max_length=255,
		required=True)


class TripLoadingRequestSerializer(TripRequestSerializer):
	buying_price_per_kg = serializers.FloatField(
		max_value=None, min_value=10,required=True)
	total_weight_bought = serializers.FloatField(
		max_value=None, min_value=10,required=True)
	loading_cost = serializers.FloatField(
		max_value=None, min_value=None,required=True)
	departure_date = serializers.DateField()

class TripOffloadingRequestSerializer(serializers.Serializer):
	selling_price_per_kg = serializers.CharField(
		max_length=255,required=True)
	total_weight_sold = serializers.CharField(
		max_length=255,required=True)
	total_selling_price = serializers.CharField(
		max_length=255,required=True)
	offloading_cost = serializers.CharField(
		max_length=255,required=True)
	selling_date = serializers.DateField()
	
	def validate_total_selling_price(self, value):
		selling_price_per_kg = self.selling_price_per_kg
		total_weight_sold = self.total_weight_sold

		total_selling_price = selling_price_per_kg * total_weight_sold

		return total_selling_price

class TripExpenseRequestSerializer(serializers.Serializer):
	transport_cost = serializers.CharField(
		max_length=255,required=True)
	clearance_cost = serializers.CharField(
		max_length=255,required=True)
	broker_cost = serializers.CharField(
		max_length=255,required=True)

class TripShareRequestSerializer(serializers.Serializer):
	user = serializers.CharField(
		max_length=255,required=True)
	profit_share = serializers.CharField(
		max_length=255,required=True)


# detail view serializers
class LoadingDetailSerializer(serializers.ModelSerializer):
	class Meta:
		model = trip_models.TripLoading
		fields = ['buying_price_per_kg','total_weight_bought',
				'total_buying_price','loading_cost','departure_date']

class OffloadingDetailSerializer(serializers.ModelSerializer):
	class Meta:
		model = trip_models.TripOffloading
		fields = ['selling_price_per_kg','total_weight_sold',
				'total_selling_price','offloading_cost','selling_date']

class ExpenseDetailSerializer(serializers.ModelSerializer):
	class Meta:
		model = trip_models.TripExpense
		fields = ['transport_cost','clearance_cost','broker_cost']

class ShareDetailSerializer(serializers.ModelSerializer):
	user = serializers.SerializerMethodField("get_user_details")
	profit_share = serializers.SerializerMethodField("get_profit_share_details")

	class Meta:
		model = trip_models.TripShare
		fields = ['user','profit_share']

	def get_user_details(self, obj):
		user = obj.user
		try:
			user_details = account_models.User.objects.\
				get(username=user)
		except Exception as e:
			print(e)
			return {}

		if user_details:
			user_record = UserSerializer(user_details, many=False).data
			return user_record['username']
		else:
			return []

	def get_profit_share_details(self, obj):
		user = obj.user
		try:
			user_details = account_models.User.objects.\
				get(username=user)
		except Exception as e:
			print(e)
			return {}

		print(obj.process_request.trip_expense_details.all())

		if user_details:
			print(user_details.percentage)
		else:
			pass


class TripDetailSerializer(serializers.ModelSerializer):
	loading = serializers.SerializerMethodField("get_loading_details")
	offloading = serializers.SerializerMethodField("get_offloading_details")
	expense = serializers.SerializerMethodField("get_expense_details")
	share = serializers.SerializerMethodField("get_share_details")
	share = serializers.SerializerMethodField("get_share_details")

	class Meta:
		model = trip_models.TripRequest
		fields =['title','reference_number','status',
				'loading','offloading','expense','share',
				'total_expense']


	def get_loading_details(self, obj):
		loading = obj.trip_loading_details.all()
		if loading:
			loading_record = LoadingDetailSerializer(loading, many=True).data
			return loading_record
		else:
			return {}

	def get_offloading_details(self, obj):
		offloading = obj.trip_offloading_details.all()
		if offloading:
			offloading_record = OffloadingDetailSerializer(offloading, many=True).data
			return offloading_record
		else:
			return []

	def get_expense_details(self, obj):
		expense = obj.trip_expense_details.all()
		if expense:
			expense_record = ExpenseDetailSerializer(expense, many=True).data
			return expense_record
		else:
			return []

	def get_share_details(self, obj):
		share = obj.trip_profit_share.all()
		if share:
			share_record = ShareDetailSerializer(share, many=True).data
			return share_record
		else:
			return []

	def get_total_expenses(self, obj):
		pass