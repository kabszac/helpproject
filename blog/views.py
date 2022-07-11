from django.urls import reverse
from django.http import request
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Post, Comment, LikePost
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

# Create your views here.
def home(request):
    context = {
        'posts':Post.objects.all()
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title':'about'})

@login_required
def post_like(request, pk):
    username = request.user.username
    post_id = pk
    post = Post.objects.get(id=post_id)

    like_filter = LikePost.objects.filter(username = username, post_id= post_id).first()
    if like_filter == None:
        new_like = LikePost.objects.create(username=username, post_id=post_id)
        new_like.save()
        post.like_count += 1
        post.save()
        return redirect(reverse('blog-home'))
    else:
        like_filter.delete()
        post.like_count -= 1
        post.save()
        return redirect(reverse('blog-home'))


class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']

class PostDetailView(DetailView):
    model = Post

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = "/"

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    template_name = 'blog/add_comment.html'
    fields = ['content',]

    def form_valid(self, form):
        #associate a postid with a comment
        form.instance.post_id = self.kwargs['pk']
        form.instance.name = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        pk = self.kwargs["pk"]
        return reverse("post-detail", kwargs={"pk": pk})
    