from django.urls import path
from .views import All_characters

urlpatterns = [
    path('', All_characters.as_view(), name='all_characters')
]