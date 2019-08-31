
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import Profile,Post,Likes,Follows,Saves,Comment
from django.contrib.auth.models import User
from .forms import PostForm,CommentForm,ProfileForm
from django.contrib.auth.decorators import login_required
# Create your views here.


@login_required(login_url='/accounts/login/')
def home(request):
    image_form = PostForm()
    images = Post.objects.all()
    commentform = CommentForm()
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            request.user.profile.post(form)
    return render(request, 'index.html', locals())