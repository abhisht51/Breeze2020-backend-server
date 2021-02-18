"""api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path,include
from events import views

urlpatterns = [
    path('jet/', include('jet.urls', 'jet')),  # Django JET URLS
    path('jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),
    path('admin/', admin.site.urls),
    path('',views.test),
    path('emails',views.index),
    path('api/cultural_events_get',views.cultural_events_get_name_poster),
    path('api/cultural_events_get/details/',views.cultural_events_get),
    path('api/technical_events_get',views.technical_events_get_name_poster),
    path('api/technical_events_get/<str:name>/',views.technical_events_get),
    path('api/sports_events_get/<str:name>/',views.sports_events_get),
    path('api/sports_events_get',views.sports_events_get_name_poster),
    path('api/cultural_events_post',views.cultural_events_post),
    path('api/technical_events_post',views.technical_events_post),
    path('api/registerevent',views.registerevent),
    path('api/getregisteredevents',views.getregisteredevent),
    path('api/sports_events_post',views.sports_events_post),
    path('rest-auth/register', views.register),
    path('rest-auth/user_get', views.user_get),
    path('rest-auth/login',views.Login),
    path('rest-auth/change_password',views.changePassword),
    path('rest-auth/verifyUser',views.verifyUser),
    path('cart',views.cart),
    path("api/makePayment", views.makePayment),
    path("api/getPayments", views.getPayments),
    path("accommodation", views.accommodation_register),

]
