from django.shortcuts import render,redirect
from .models import messages,friends
from users.models import Profile
from django.contrib.auth.models import User
from django.db.models import Q
from django.contrib.auth.decorators import login_required
# Create your views here.

def index(request):
    if not request.user.is_authenticated:
        return redirect('main')
    try:
        Profile.objects.get(user=request.user)
    except:
        return redirect("create_profile")
    friends_list = friends.objects.filter(user=request.user)
    friends_data = []

    for friend2 in friends_list:
        last_msg = messages.objects.filter(receiver=request.user, sender=friend2.friend).exclude(seen=True).order_by("-date").first()
        count = messages.objects.filter(receiver=request.user, sender=friend2.friend).exclude(seen=True).count()
        
        friends_data.append({
            'friend': friend2.friend,
            'last_msg': last_msg.body if last_msg else 'No new messages',
            'count':count,
            'user':Profile.objects.get(user=friend2.friend.id),
        })


    user = User.objects.get(username=request.user)
    data = {
        'user': user,
        'friends_data': friends_data,
        'user':Profile.objects.get(user=request.user),
    }

    return render(request, 'index.html', data)

@login_required
def single(request,pk):
    try:
        Profile.objects.get(user=request.user)
    except:
        return redirect("create_profile")
    try:
        msg = messages.objects.filter(
        Q(sender=request.user, receiver=User.objects.get(id=pk)) | 
        Q(sender=User.objects.get(id=pk), receiver=request.user)
        ).order_by('date')
    except:
        return redirect('main')
    if request.method == 'POST':
        message=messages(sender=request.user,receiver=User.objects.get(id=pk),body=request.POST['content'])
        message.save()
        return redirect('single_chat',pk)
   
    
    try:
        user2 = friends.objects.get(Q(friend=pk)&Q(user=request.user))
    except:
        return redirect('main')
    for i in msg:
        if i.receiver==request.user:
            i.seen=True
            i.save()
    friends_list = friends.objects.filter(user=request.user)
    friends_data = []

    for friend2 in friends_list:
        last_msg = messages.objects.filter(receiver=request.user, sender=friend2.friend).exclude(seen=True).order_by('-date').first()
        count = messages.objects.filter(receiver=request.user, sender=friend2.friend).exclude(seen=True).count()
        friends_data.append({
            'friend': friend2.friend,
            'last_msg': last_msg.body if last_msg else 'No new messages',
            'count':count,
            'user':Profile.objects.get(user=friend2.friend.id),
        })

    count = messages.objects.filter(receiver=request.user).exclude(seen=True).count()

    user = User.objects.get(username=request.user)
    data = {
        'user': user,
        'friends_data': friends_data,
        'msg':msg,
        'users':Profile.objects.get(user=user2.friend.id),
        'user':Profile.objects.get(user=request.user)
    }
    return render(request,'single_chat.html',data)

@login_required
def add_friend(request,pk):
    try:
        Profile.objects.get(user=request.user)
    except:
        return redirect("create_profile")
    try:
        friend = friends(user=request.user, friend=User.objects.get(id=pk))
        friend.save()
        friend2 = friends(user=User.objects.get(id=pk), friend=request.user)
        friend2.save()
        return redirect('/')
    except:
        return redirect('main')

@login_required
def search(request):
    try:
        Profile.objects.get(user=request.user)
    except:
        return redirect("create_profile")
    if not request.user.is_authenticated:
        return redirect('login')
    search=False
    
    if request.GET.get('search'):
        search = request.GET.get('search')

    current_user = request.user

    friends_ids = friends.objects.filter(user=current_user).values_list('friend_id', flat=True)
    available_users = Profile.objects.filter(Q(username__icontains=search)|Q(full_name__icontains=search)).exclude(user__in=friends_ids).exclude(user=current_user.id)
 

    data={'users':available_users,'isin':search}
    return render(request,'search.html',data)

@login_required
def delete_friend(request,pk):
    try:
        Profile.objects.get(user=request.user)
    except:
        return redirect("create_profile")
    try:
        friend = friends.objects.get(Q(friend=pk)&Q(user=request.user))
        message = messages.objects.filter(Q(sender=pk)&Q(receiver=request.user))
        message.delete()
        friend.delete()
        friend2 = friends.objects.get(Q(friend=request.user.id)&Q(user=pk))
        message2 = messages.objects.filter(Q(sender=request.user.id)&Q(receiver=pk))
        message2.delete()
        friend2.delete()
        return redirect('/')
    except:
        return redirect('main')
