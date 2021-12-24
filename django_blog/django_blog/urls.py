"""django_blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from app.portfolio.views import index,QueeselODS,Registrarme,recuperarcontraseña,foro,ODS1,ODS2,ODS3,ODS4,ODS5,ODS6,ODS7,ODS8,ODS9,ODS10,ODS11,ODS12,ODS13,ODS14,ODS15,ODS16,ODS17
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('QueeselODS/', QueeselODS, name='QueeselODS'),
    path('login/', auth_views.LoginView.as_view(template_name="login.html"), name="login"),
    path("logout/", auth_views.logout_then_login, name="logout"),
    path("Registrarme/", Registrarme, name="Registrarme"),
    path("recuperarcontraseña/", recuperarcontraseña, name="recuperarcontraseña"),
    path("foro/", foro, name="foro"),
    path("ODS1/", ODS1, name="ODS1"),
    path("ODS2/", ODS2, name="ODS2"),
    path("ODS3/", ODS3, name="ODS3"),
    path("ODS4/", ODS4, name="ODS4"),
    path("ODS5/", ODS5, name="ODS5"),
    path("ODS6/", ODS6, name="ODS6"),
    path("ODS7/", ODS7, name="ODS7"),
    path("ODS8/", ODS8, name="ODS8"),
    path("ODS9/", ODS9, name="ODS9"),
    path("ODS10/", ODS10, name="ODS10"),
    path("ODS11/", ODS11, name="ODS11"),
    path("ODS12/", ODS12, name="ODS12"),
    path("ODS13/", ODS13, name="ODS13"),
    path("ODS14/", ODS14, name="ODS14"),
    path("ODS15/", ODS15, name="ODS15"),
    path("ODS16/", ODS16, name="ODS16"),
    path("ODS17/", ODS17, name="ODS17"),

]
