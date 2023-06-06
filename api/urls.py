from django.contrib import admin
from django.urls import path,include
from api.views import ComapanyviewSet,EmployeeviewSet
from rest_framework import routers

router= routers.DefaultRouter()
router.register(r'companies',ComapanyviewSet )
router.register(r'employees',EmployeeviewSet )



urlpatterns = [
    path('',include(router.urls))
    
]