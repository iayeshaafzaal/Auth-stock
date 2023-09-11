from django.contrib import admin

# Register your models here.
from .models import UserData
from home.models import Stockdata
from home.models import Transactiontable

# Register your models here.
admin.site.register(Stockdata)
admin.site.register(Transactiontable)
admin.site.register(UserData)
