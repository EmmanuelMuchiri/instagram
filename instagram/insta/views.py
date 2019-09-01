from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .models import Image,Profile,Comment
from django.contrib.auth.models import User
from .forms import NewImageForm,CommentForm,ProfileForm
from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse
import json

# Create your views here.
@login_required(login_url='/accounts/login/')
def index(request):
    current_user = request.user
    images = Image.objects.order_by('-pub_date')
    profiles = Profile.objects.order_by('-last_update')
    comments = Comment.objects.order_by('-time_comment')
    return render(request, 'index.html', {'images':images, 'profiles':profiles,'comments':comments})

@login_required(login_url='/accounts/login/')
def profile(request):
    current_user = request.user
    profile = Profile.objects.get(user_id=current_user.id)
    images = Image.objects.all().filter(profile_id=current_user.id)
    return render(request, 'profile.html', {'images':images, 'profile':profile})

def ajaxlikephoto(request):
    img_id = None
    current_user = request.user

    if request.method == 'GET':
        img_id = request.GET['image_id']

    if not Image.objects.filter(id = img_id,likes = request.user ).exists():
        image = Image.objects.get(id = img_id)
        image.likes.add(current_user)
        image.save()

    image = Image.objects.get(id = img_id)
    likes = image.likes.all().count()
    return HttpResponse(likes)

def ajax_comment(request):
    comment = request.GET.get('comment')
    image = request.GET.get('image')
    user = request.user

    comment = Comment(comment = comment,image = image,user = user)
    comment.save()

    latest_comment = f"{Comment.objects.all().last().comment}"
    latest_comment_user = f"{Comment.objects.all().last().user}"
    data = {
        'latest_comment': latest_comment,
        'latest_comment_user': latest_comment_user
    }

    return JsonResponse(data)

def search(request):
    if request.is_ajax():
        q = request.GET.get('term', '')
        users = User.objects.filter(username__icontains=q)
        results = []
        for user in users:
            user_json = {}
            user_json = user.username
            results.append(user_json)
            data = json.dumps(results)
    else:
        data = 'fail'
    mimetype = 'application/json'
    return HttpResponse(data, mimetype)

def search_user(request):
    if 'username' in request.GET and request.GET['username']:
        username = request.GET.get('username')
        searched_user = Profile.search(username)

        return redirect('profile',username = searched_user)

def edit_profile(request,username):
    current_user = request.user
    if request.method == 'POST':
        form = ProfileForm(request.POST,request.FILES)
        if form.is_valid():
            bio = form.save(commit=False)
            bio.user = current_user
            bio.save()
        return redirect('index')
    elif Profile.objects.get(user=current_user):
        profile = Profile.objects.get(user=current_user)
        form = ProfileForm(instance=profile)
    else:
        form = ProfileForm()

    return render(request,'edit_profile.html',{"form":form})

def follow_user(request):
    user_id = None
    profile_id = None
    data = {}

    if request.method == 'GET':
        user_id = request.GET['user_id']
        profile_id = request.GET['profile_id']

        user = User.objects.get(id = user_id)
    if Profile.objects.filter(id=profile_id,followers = user).exists():
        data['message'] = "You are already following this user."
    else:
        profile = Profile.objects.get(id=profile_id)
        profile.followers.add(user)
        data['message'] = "You are now following {}".format(profile.user.username)
        return JsonResponse(data, safe=False)