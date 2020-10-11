from rest_framework import serializers
from .models import TripLoading,TripOffloading, SharesModel

class UserProfitShareSerializer(serializers.ModelSerializer):
	class Meta:
		model = SharesModel
		fields =['id','offloading','user','profit_share']

		read_only_fields = ['profit_share']

class ProfitShareSerializer(serializers.ModelSerializer):
	# profit_share = serializers.SerializerMethodField(method_name='calculate_profit')
	user = serializers.SlugRelatedField(read_only=True, slug_field='username')
	class Meta:
		model = SharesModel
		fields =['id','offloading','user','profit_share']

		read_only_fields = ['profit_share']
		


class TripOffloadingSerializer(serializers.ModelSerializer):
	profits = ProfitShareSerializer(many=True,read_only=True)
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

	
	def get_serializer_context(self):
		pass
