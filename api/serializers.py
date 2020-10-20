from rest_framework import serializers
from .models import TripLoading,TripOffloading, SharesModel

from accounts.models import Member

class ProfileSerializer(serializers.ModelSerializer):
	class Meta:
		model = Member
		fields = ['id','username','percentage']

class UserProfitShareSerializer(serializers.ModelSerializer):
	name = ProfileSerializer(read_only=True, source='user')
	class Meta:
		model = SharesModel
		fields =['id','offloading','user','name','profit_share']

		read_only_fields = ['profit_share']
	
	# def create(self, validated_data):
	# 	print('validate data ----->',validated_data)
	# 	shares = SharesModel.objects.create(
	# 		validated_data['offload'],
	# 		validated_data['user']
	# 	)
	# 	return shares

class TripOffloadingSerializer(serializers.ModelSerializer):
	profits = UserProfitShareSerializer(many=True,read_only=True)
	class Meta:
		model = TripOffloading
		fields =['trip_loading','id','transport_cost'
				,'selling_price_per_kg','clearance_cost'
				,'total_weight_sold','total_selling_price'
				,'offloading_cost','broker_expenses'
				,'total_expenses','profit_margin'
				,'selling_date','comment','profits']

		read_only_fields = ['total_selling_price','total_expenses','profit_margin']

class TripLoadingSerializer(serializers.HyperlinkedModelSerializer):
	trip_offloading =  TripOffloadingSerializer(read_only=True)
	class Meta:
		model = TripLoading
		fields =['id','trip_offloading','title','buying_price_per_kg','total_weight_bought'
				,'total_buying_price','loading_cost'
				,'departure_date','comment']
		read_only_fields = ['total_buying_price']