from django.urls import path
from .views import homepage, about, contact

urlpatterns = [
    path('', homepage),
    path('about/', about),
    path('contact/', contact),
]
