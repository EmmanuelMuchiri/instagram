from django.conf.urls import url,include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url('^$',views.index,name='index'),
    url(r'^user/(?P<username>\w{0,50})',views.profile,name='profile'),
    url(r'^likephoto/$',views.likephoto,name = 'like_image'),
    url(r'^comment/$',views.comment),
    url(r'^search/', views.search,name='search'),
    url(r'^search/$',views.search_user,name='search_user'),
    url(r'^edit_profile/(?P<username>\w{0,50})',views.edit_profile,name='edit_profile'),
    url(r'^follow/$', views.follow_user,name='follow_user')
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)