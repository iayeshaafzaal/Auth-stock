from django.urls import path

from . import views
from .views import RegisterView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path('api/register/', RegisterView.as_view(), name="sign_up"),
    path('api/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('users/',views.UsersAPIView.as_view({'post':'create', 'get':'get'}),name='Users'),
    path('users/<str:username>/',views.SpecificUserAPI.as_view({'get':'list'}),name="specific"),
    path('stock/',views.StockAPIView.as_view({'post':'create','get':'get'}),name="stock"),
    path('stock/<str:ticker>/',views.SpecificStockAPI.as_view({'get':'list'}),name="specificstock"),
    path('transaction/',views.TransactionAPIView.as_view({'post':'create', 'get':'get'}),name='transaction'),
    path('transaction/<str:transaction_id>/',views.SpecificTransactionAPI.as_view({'get':'list'}),name="specifictransaction"),

]