
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


@login_required(login_url='/accounts/login/')
def user(request, user_id):
	user_object=get_object_or_404(User, pk=user_id)
	if request.user == user_object:
		return redirect('myaccount')
	isfollowing = user_object.profile not in request.user.profile.follows
	user_images = user_object.profile.posts.all()
	user_liked = [like.photo for like in user_object.profile.mylikes.all()]
	return render(request, 'profile.html', locals())