from django.urls import path
from . import views

urlpatterns = [
    path('', views.upload_form, name='upload_form'),
    path('stream/', views.event_stream, name='event_stream'),
    path('download/', views.download_report, name='download_report'),
]