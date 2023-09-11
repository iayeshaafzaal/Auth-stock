from rest_framework import status
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from home.models import Stockdata, Transactiontable
from home.serializers import UserSerializer, StockSerializer, TransactionSerializer
from .models import UserData


# view for registering users
class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class UsersAPIView(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)

    def create(self, request):
        data = request.data
        serializer = UserSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"Detail": "the data has been written to the db"}, status=status.HTTP_200_OK)

    def get(self, request):
        data = UserData.objects.all()
        serializer = UserSerializer(data=data, many=True)
        serializer.is_valid()
        return Response({"data": serializer.data}, status=status.HTTP_200_OK)


class SpecificUserAPI(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)

    def list(self, request, username):

        filter_data = UserData.objects.filter(name=username).first()

        serializer = UserSerializer(instance=filter_data)
        return Response({"data": serializer.data}, status=status.HTTP_200_OK)


class StockAPIView(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)

    def create(self, request):
        data = request.data
        serializer = StockSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"Detail": "stock has been added"}, status=status.HTTP_200_OK)

    def get(self, request):
        data = Stockdata.objects.all()
        serializer = StockSerializer(data=data, many=True)
        serializer.is_valid()
        return Response({"data": serializer.data}, status=status.HTTP_200_OK)


class SpecificStockAPI(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)

    def list(self, request, ticker):

        filter_data = Stockdata.objects.filter(ticker=ticker).first()
        data = {
            "ticker": filter_data.ticker,
            "open_price": filter_data.open_price,
            "close_price": filter_data.close_price,
            "high": filter_data.high,
            "low": filter_data.low,
            "volume": filter_data.volume
        }
        return Response({"data": data}, status=status.HTTP_200_OK)


class TransactionAPIView(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)

    def create(self, request):
        data = request.data
        serializer = TransactionSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"Detail": "transaction has been completed"}, status=status.HTTP_200_OK)

    def get(self, request):
        data = Transactiontable.objects.all()
        serializer = TransactionSerializer(data=data, many=True)
        serializer.is_valid()
        return Response({"data": serializer.data}, status=status.HTTP_200_OK)


class SpecificTransactionAPI(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)

    def list(self, request, transaction_id):
        filter_data = Transactiontable.objects.filter(transaction_id=transaction_id).first()
        data = {
            "transaction_id": filter_data.transaction_id,
            "user_id": filter_data.user_id,
            "ticker": filter_data.ticker,
            "transaction_type": filter_data.transaction_type,
            "transaction_volume": filter_data.transaction_volume,
            "transaction_price": filter_data.transaction_price,
            "timestamp": filter_data.timestamp}
        return Response({"data": data}, status=status.HTTP_200_OK)
