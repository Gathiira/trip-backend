from rest_framework import serializers
from .models import TripLoading,TripOffloading
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields =['username','first_name','last_name','email']
		read_only_fields = ['is_active', 'is_staff']

class TripOffloadingSerializer(serializers.ModelSerializer):
	class Meta:
		model = TripOffloading
		fields =['trip_loading','transport_cost'
				,'selling_price_per_kg','clearance_cost'
				,'total_weight_sold','total_selling_price'
				,'offloading_cost','broker_expenses'
				,'total_expenses','profit_margin'
				,'selling_date','comment']

		read_only_fields = ['total_selling_price','total_expenses','profit_margin']
		
		extra_kwargs = {
			'id': {'write_only': True},
			'trip_loading': {'write_only': True},
		}

class TripLoadingSerializer(serializers.HyperlinkedModelSerializer):
	trip_offloading =  TripOffloadingSerializer(read_only=True)
	class Meta:
		model = TripLoading
		fields =['title','buying_price_per_kg','total_weight_bought'
				,'total_buying_price','loading_cost'
				,'departure_date','comment','trip_offloading']
		read_only_fields = ['total_buying_price']
		
		extra_kwargs = {
			'id': {'write_only': True},
		}


# class TripSerializer(serializers.HyperlinkedModelSerializer):
# 	loading =  LoadingSerializer(read_only=True)
# 	offloading =  OffloadingSerializer(read_only=True)
# 	tripInfo = TripInfoSerializer(read_only=True)
# 	class Meta:
# 		model = Trip
# 		fields =['title','created_on','loading','offloading','tripInfo']
# 		extra_kwargs = {
# 			'id': {'write_only': True},
# 			# 'title': {'read_only': True},
# 			# 'created_on': {'read_only': True},
# 		}

