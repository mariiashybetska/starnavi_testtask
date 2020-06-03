from django.urls import path

from social_network.api import views

app_name = 'api-social_network'

urlpatterns = [
    path('analytics/', views.LikesAnalytics.as_view(), name='likes-analytics'),
]