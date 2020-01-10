
"""projclinicas URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from dashboard.api.viewsets import ClientesViewset, FuncionarioViewset, AtivosViewset, PassivosViewset
from django.conf import settings
from django.conf.urls.static import static

router = DefaultRouter()
router.register(r'bdclientes', ClientesViewset, base_name='ClientesViewset')
router.register(r'funcionario', FuncionarioViewset,
                base_name='FuncionarioViewset')
router.register(r'ativos', AtivosViewset, base_name='AtivosViewset')
router.register(r'passivos', PassivosViewset, base_name='PassivosViewset')

urlpatterns = [
    path('', include('index.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('dashboard/', include('dashboard.urls')),
    path('chatbot/', include('chatbot.urls')),
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('django_plotly_dash/', include('django_plotly_dash.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
