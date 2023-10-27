from django.urls import path
from studentapp import views 
urlpatterns = [
    path('', views.student, name="student"),
]