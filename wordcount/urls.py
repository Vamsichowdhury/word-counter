from django.urls import path
from .views import home,about,count

urlpatterns = [
    path('home/',home,name='home'),
    path('about/',about,name='about'),
    path('count/',count,name='count'),
]
