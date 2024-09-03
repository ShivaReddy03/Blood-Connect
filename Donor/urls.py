from django.urls import path
from . import views

app_name="Donor"

urlpatterns = [
    path('',views.donate_req,name='donate_req'),
    path('save_to_db/', views.save_to_db, name='save_to_db'),
    path('saved/',views.saved,name="saved")
]