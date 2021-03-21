from rest_framework import serializers

from trip import models as trip_models
from accounts import models as account_models


# generic serializers
class GenericRequestSerializer(serializers.Serializer):
    request_id = serializers.CharField(required=True)


class UserSerializer(serializers.Serializer):
    username = serializers.CharField()
    percentage = serializers.FloatField(
        max_value=None, min_value=10, required=True)


class ListTripRequestSerializer(serializers.ModelSerializer):

    class Meta:
        model = trip_models.TripRequest
        fields = [
            'id',
            'title',
            'reference_number',
            'total_expense',
            'profit_margin',
            'status',
            'date_created',
        ]


#  creating requests serializers


class TripRequestSerializer(serializers.Serializer):
    title = serializers.CharField(
        max_length=255,
        required=True)


class TripLoadingRequestSerializer(TripRequestSerializer):
    buying_price_per_kg = serializers.FloatField(
        max_value=None, min_value=10, required=True)
    total_weight_bought = serializers.FloatField(
        max_value=None, min_value=10, required=True)
    loading_cost = serializers.FloatField(
        max_value=None, min_value=None, required=True)
    departure_date = serializers.DateField()


class TripExpenseRequestSerializer(GenericRequestSerializer):
    transport_cost = serializers.FloatField(
        max_value=None, min_value=10, required=True)
    clearance_cost = serializers.FloatField(
        max_value=None, min_value=10, required=True)
    broker_cost = serializers.FloatField(
        max_value=None, min_value=10, required=True)


class TripOffloadingRequestSerializer(TripExpenseRequestSerializer):
    selling_price_per_kg = serializers.FloatField(
        max_value=None, min_value=10, required=True)
    total_weight_sold = serializers.FloatField(
        max_value=None, min_value=10, required=True)
    offloading_cost = serializers.FloatField(
        max_value=None, min_value=10, required=True)
    selling_date = serializers.DateField()


# detail view serializers
class LoadingDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = trip_models.TripLoading
        fields = ['buying_price_per_kg', 'total_weight_bought',
                  'total_buying_price', 'loading_cost', 'departure_date']


class OffloadingDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = trip_models.TripOffloading
        fields = ['selling_price_per_kg', 'total_weight_sold',
                  'total_selling_price', 'offloading_cost', 'selling_date']


class ExpenseDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = trip_models.TripExpense
        fields = ['transport_cost', 'clearance_cost', 'broker_cost']


class ShareDetailSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField("get_username")
    percentage = serializers.SerializerMethodField("get_percentage")

    class Meta:
        model = trip_models.TripShare
        fields = ['username', 'percentage', 'profit_share']

    def get_username(self, obj):
        user_id = obj.user
        try:
            user_details = account_models.User.objects.\
                get(id=user_id)
        except Exception as e:
            print(e)
            return {}

        if user_details:
            user_record = UserSerializer(user_details, many=False).data
            return user_record['username']
        else:
            return []

    def get_percentage(self, obj):
        user_id = obj.user
        try:
            user_details = account_models.User.objects.\
                get(id=user_id)
        except Exception as e:
            print(e)
            return {}

        if user_details:
            user_record = UserSerializer(user_details, many=False).data
            return user_record['percentage']
        else:
            return []


class TripDetailSerializer(ListTripRequestSerializer):
    loading = serializers.SerializerMethodField("get_loading_details")
    offloading = serializers.SerializerMethodField("get_offloading_details")
    expense = serializers.SerializerMethodField("get_expense_details")
    shares = serializers.SerializerMethodField("get_share_details")

    class Meta:
        model = trip_models.TripRequest
        fields = ListTripRequestSerializer.Meta.fields + [
            'loading',
            'offloading',
            'expense',
            'shares'
        ]

    def get_loading_details(self, obj):
        try:
            loading = obj.trip_loading_details
        except Exception as e:
            print(e)
            return {}
        if loading:
            loading_record = LoadingDetailSerializer(loading, many=False).data
            return loading_record
        else:
            return {}

    def get_offloading_details(self, obj):
        try:
            offloading = obj.trip_offloading_details
        except Exception as e:
            print(e)
            return {}
        if offloading:
            offloading_record = OffloadingDetailSerializer(
                offloading, many=False).data
            return offloading_record
        else:
            return []

    def get_expense_details(self, obj):
        try:
            expense = obj.trip_expense_details
        except Exception as e:
            print(e)
            return {}
        if expense:
            expense_record = ExpenseDetailSerializer(expense, many=False).data
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
