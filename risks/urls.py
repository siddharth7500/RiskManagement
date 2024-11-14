from django.urls import path
from . import views

urlpatterns = [
    path('risks', views.get_or_create_risk_view, name='get_or_create_risk_view'),
    path('risks/<str:id>', views.get_risk, name='get_risk'),
]