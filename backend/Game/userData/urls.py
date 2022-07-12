from django.urls import path, include
from . import views

urlpatterns = [
    path('stats/', views.get_post),
    path('stats/<slug:pk>', views.get_put),

]