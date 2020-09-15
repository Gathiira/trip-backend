from rest_framework import serializers
from .models import Trip,TripInfo,Loading,Offloading
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields =['username','first_name','last_name','phone']
		read_only_fields = ['is_active', 'is_staff']

class LoadingSerializer(serializers.ModelSerializer):
	class Meta:
		model = Loading
		fields =['trip','buying_price_per_kg','total_weight_bought'
				,'total_buying_price','loading_cost'
				,'departure_date','comment']
		read_only_fields = ['total_buying_price']
		
		extra_kwargs = {
			'trip': {'write_only': True},
		}

class OffloadingSerializer(serializers.ModelSerializer):
	class Meta:
		model = Offloading
		fields =['trip','selling_price_per_kg','total_weight_sold'
				,'total_selling_price','offloading_cost'
				,'selling_date','comment']
		read_only_fields = ['total_selling_price']
		
		extra_kwargs = {
			'trip': {'write_only': True},
			'loading': {'write_only': True},
		}

class TripInfoSerializer(serializers.ModelSerializer):
	class Meta:
		model = TripInfo
		fields =['transport_cost','clearance_cost'
				,'broker_expenses','total_expenses'
				,'profit_margin','comment']
		read_only_fields = ['total_expenses','profit_margin']
		
		extra_kwargs = {
			'trip': {'write_only': True},
			'loading': {'write_only': True},
			'offloading': {'write_only': True},
		}


class TripSerializer(serializers.HyperlinkedModelSerializer):
	loading =  LoadingSerializer(read_only=True)
	offloading =  OffloadingSerializer(read_only=True)
	tripInfo = TripInfoSerializer(read_only=True)
	class Meta:
		model = Trip
		fields =['title','created_on','loading','offloading','tripInfo']
		extra_kwargs = {
			'id': {'write_only': True},
			# 'title': {'read_only': True},
			# 'created_on': {'read_only': True},
		}

