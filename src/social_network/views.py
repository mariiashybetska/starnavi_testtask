import json

from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.views import View
from django.contrib.contenttypes.models import ContentType

from social_network.forms import SignUpForm
from social_network.models import User, Post, LikeDislike


class SignUpView(CreateView):
    template_name = 'signup.html'
    form_class = SignUpForm
    queryset = User.objects.all()
    success_url = reverse_lazy('index')


class CreatePostView(CreateView):
    template_name = 'post_form.html'
    fields = ('title', 'text', )
    model = Post
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        post = form.save(commit=False)
        post.author = self.request.user
        post.save()
        return super().form_valid(form)


class VotesView(View):
    model = Post
    vote_type = None

    def post(self, request, pk):
        obj = self.model.objects.get(pk=pk)
        # GenericForeignKey does not support get_or_create
        try:
            likedislike = LikeDislike.objects.get(content_type=ContentType.objects.get_for_model(obj), object_id=obj.id,
                                                  user=request.user)
            if likedislike.vote is not self.vote_type:
                likedislike.vote = self.vote_type
                likedislike.save(update_fields=['vote'])
                result = True
            else:
                likedislike.delete()
                result = False
        except LikeDislike.DoesNotExist:
            obj.votes.create(user=request.user, vote=self.vote_type)
            result = True

        return HttpResponse(
            json.dumps({
                "result": result,
                "like_count": obj.votes.likes().count(),
                "dislike_count": obj.votes.dislikes().count(),
                "sum_rating": obj.votes.sum_rating()
            }),
            content_type="application/json"
        )


class PostsView(ListView):
    model = Post
    template_name = 'posts.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context








