from rest_framework import serializers
from .models import User

class userSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'number', 'password']
        #extra_kwargs = {'password': {'write_only': True}}
