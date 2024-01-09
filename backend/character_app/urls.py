from django.urls import path, register_converter
from .views import All_characters, A_character
from .converters import IntOrStrConverter

register_converter(IntOrStrConverter, 'int_or_str')

urlpatterns = [
    path('', All_characters.as_view(), name='all_characters'),
    path('<int_or_str:id>/', A_character.as_view(), name='a_character')
]