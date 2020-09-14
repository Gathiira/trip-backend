from rest_framework import serializers
from .models import Task,TripInfo
from django.contrib.auth.models import User

class TaskSerializer(serializers.ModelSerializer):
	class Meta:
		model = Task
		fields ='__all__'

class TripSerializer(serializers.ModelSerializer):
	class Meta:
		model = TripInfo
		fields ='__all__'

class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields ='__all__'