from rest_framework import serializers
from .models import CustomUser, Donate_food, Donate_Grocery, Request

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'mobile', 'login_status', 'created_date', 'address','password']
        read_only_fields = ['id', 'created_date']

class DonateFoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Donate_food
        fields = ['id', 'donator', 'receiver', 'description', 'food_quantity', 'type_of_food', 'time', 'status', 'address']
        read_only_fields = ['id', 'time']


class DonateFoodACCSerializer(serializers.ModelSerializer):
    class Meta:
        model = Donate_food
        fields = ['id', 'donator', 'receiver', 'description', 'food_quantity', 'type_of_food', 'time', 'status', 'address']
        # read_only_fields = ['id', 'time']
class DonateGrocerySerializer(serializers.ModelSerializer):
    class Meta:
        model = Donate_Grocery
        fields = ['id', 'donator', 'receiver', 'description', 'grocery_quantity', 'type_of_grocery', 'time', 'status', 'address']
        read_only_fields = ['id', 'time']

class RequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Request
        fields = ['id', 'requestor', 'helper', 'description', 'help', 'time', 'status', 'address']
        read_only_fields = ['id', 'time']
