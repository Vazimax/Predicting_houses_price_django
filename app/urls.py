from django.urls import path
from .views import home, prediction, prediction_result

urlpatterns = [
    path('',home,name="home"),
    path('prediction/',prediction,name="prediction"),
    path('prediction/result',prediction_result),
]
