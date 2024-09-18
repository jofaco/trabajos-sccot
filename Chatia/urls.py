from django.urls import path
from .views import PreguntarChatGPT,hola_mundo

urlpatterns = [
    path('', PreguntarChatGPT.as_view(), name='preguntarChatGPT'),
    path('hola-mundo/', hola_mundo, name='holaMundo'),
]