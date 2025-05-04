from rest_framework import serializers
from django.contrib.auth.models import User
from .models import UserData
    
class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)  # ✅ important!
    first_name = serializers.CharField(required=True)  # ✅ Include required fields
    last_name = serializers.CharField(required=True)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password')

    def create(self, validated_data):
        # ✅ Create user with hashed password
        return User.objects.create_user(**validated_data)

#class UserDataSerializer(serializers.ModelSerializer):
    #class Meta:
        #model = UserData
        #fields = '__all__'

# class SleepDataSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = SleepData
#         fields = ['username', 'sleep_duration', 'quality_of_sleep', 'stress_level']

class FoodSerializer(serializers.Serializer):
    name = serializers.CharField()
    calories = serializers.FloatField()
    protein = serializers.FloatField()
    fat = serializers.FloatField()
    carbs = serializers.FloatField()
    image_url = serializers.CharField()

class RecommendationSerializer(serializers.Serializer):
    breakfast = FoodSerializer(many=True)
    lunch = FoodSerializer(many=True)
    dinner = FoodSerializer(many=True)
    bmi = serializers.FloatField()
    bmi_info = serializers.CharField()

class Page1Serializer(serializers.ModelSerializer):
    class Meta:
        model = UserData
        fields = ['gender', 'age', 'occupation', 'physical_activity_level']

class Page2Serializer(serializers.ModelSerializer):
    class Meta:
        model = UserData
        fields = ['sleep_hours', 'quality_of_sleep', 'stress_level']

class Page3Serializer(serializers.ModelSerializer):
    class Meta:
        model = UserData
        fields = ['height', 'weight']

class Page4Serializer(serializers.ModelSerializer):
    class Meta:
        model = UserData
        fields = ['blood_pressure_category', 'systolic', 'diastolic']

class Page5Serializer(serializers.ModelSerializer):
    class Meta:
        model = UserData
        fields = ['heart_rate', 'daily_steps', 'sleep_disorder']
