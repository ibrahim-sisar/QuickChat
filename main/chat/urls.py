from django.urls import  path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.index,name='index'),
    path('chat/<pk>/',views.single,name='single_chat'),
    path('search/frindes/',views.search,name='search_friends'),
    path('add/<pk>/',views.add_friend,name='add'),
    path('delete/<pk>/',views.delete_friend,name='delete_friend')
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)