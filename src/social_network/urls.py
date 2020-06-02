from django.contrib import admin
from django.urls import path
from django.views.generic.base import TemplateView
from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from social_network.views import SignUpView, CreatePostView, VotesView, PostsView
from social_network.models import Post, LikeDislike

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', TemplateView.as_view(template_name='index.html'), name='index'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('new-post/', CreatePostView.as_view(), name='newpost'),
    path('posts/', PostsView.as_view(), name='posts'),
    url(r'^post/(?P<pk>\d+)/like/$',
        login_required(VotesView.as_view(model=Post, vote_type=LikeDislike.LIKE)),
        name='post_like'),
    url(r'^post/(?P<pk>\d+)/dislike/$',
        login_required(VotesView.as_view(model=Post, vote_type=LikeDislike.DISLIKE)),
        name='post_dislike'),
]