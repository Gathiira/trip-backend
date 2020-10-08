from rest_framework import serializers
from .models import TripLoading,TripOffloading, SharesModel

class UserProfitShareSerializer(serializers.ModelSerializer):
	# profit_share = serializers.SerializerMethodField(method_name='calculate_profit')
	class Meta:
		model = SharesModel
		fields =['id','offloading','name','percentage','profit_share']

		read_only_fields = ['profit_share']

	# def calculate_profit(self,instance):
	# 	total_capital = 0
	# 	contribution = 0

	# 	contributions = SharesModel.objects.all()
	# 	for contrib in contributions:
	# 		contribution = contrib.contribution
	# 		total_capital = total_capital + contrib.contribution

	# 	profit = contribution / total_capital * contrib.offloading.profit_margin
	# 	return profit
		


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
