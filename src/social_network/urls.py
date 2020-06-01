from django.contrib import admin
from django.urls import path
from django.views.generic.base import TemplateView

from social_network.views import SignUpView, CreatePostView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', TemplateView.as_view(template_name='index.html'), name='index'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('new-post/', CreatePostView.as_view(), name='newpost'),
]