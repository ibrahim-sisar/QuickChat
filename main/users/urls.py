from django.urls import  path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
   path('',views.index,name='main'),
   path('login/',views.user_login,name='login'),
   path('logout/',views.user_logout,name='logout'),
   path('sighup/',views.sighup_user,name='sighup'),
   path('profile/<pk>/',views.profile,name='profile'),
   path('Edit_profile/<pk>/',views.edit_profile,name='edit'),
   path('delete_account/<pk>',views.delete_account,name='delete_account'),
   path('create_profile/',views.create_profile,name='create_profile'),
   path('friends_profile/<pk>/',views.friends_profile,name='friend_profile')

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)