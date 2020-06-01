from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.shortcuts import redirect

from social_network.forms import SignUpForm
from social_network.models import User, Post


class SignUpView(CreateView):
    template_name = 'signup.html'
    form_class = SignUpForm
    queryset = User.objects.all()
    success_url = reverse_lazy('index')


class CreatePostView(CreateView):
    template_name = 'post_form.html'
    model = Post
    fields = ('title', 'text')
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        post = form.save(commit=False)
        post.title = form.instance.title
        post.text = form.instance.text
        post.author = self.request.user.id
        post.save()
        return self.form_valid()





