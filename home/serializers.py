from rest_framework import serializers

from home.models import Stockdata, Transactiontable
from .models import UserData


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=128, min_length=5, write_only=True)

    class Meta:
        model = UserData
        fields = "__all__"

    def create(self, validated_data):
        return UserData.objects.create_user(**validated_data)


class StockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stockdata
        fields = "__all__"

        def create(self, validated_data):
            return Stockdata.objects.create(**validated_data)


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transactiontable
        fields = "__all__"

        def create(self, validated_data):
            return Transactiontable.objects.create(**validated_data)
