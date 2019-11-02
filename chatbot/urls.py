from django.urls import path
from chatbot import views
from django.conf.urls import url
from chatbot.views import ChatterBotAppView, ChatterBotApiView


urlpatterns = [
    url(r'^$', ChatterBotAppView.as_view(), name='main'),
    url(r'^api/chatterbot/', ChatterBotApiView.as_view(), name='chatterbot'),
    # path('', ChatterBotApiView.as_view(), name='main'),
    # path('api/chatterbot/', ChatterBotApiView.as_view(), name='chatterbot'),
]

