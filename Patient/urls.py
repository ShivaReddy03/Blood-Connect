from django.urls import path
from . import views

app_name="Patient"

urlpatterns = [
    path('', views.request_blood,name='request_blood'),
    path('save_to_db/', views.save_to_db, name='save_to_db'),
    path('saved/',views.saved,name="saved")
]
