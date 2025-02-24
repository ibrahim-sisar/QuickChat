from django.shortcuts import render,redirect
from django.contrib.auth import login, authenticate,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
import re
from .models import Profile
# Create your views here.

def index(request):
    if request.user.is_authenticated:
        try:
            Profile.objects.get(user=request.user)
            return redirect('profile', pk=request.user.id)
        except Profile.DoesNotExist:
            return redirect("create_profile")
    return render(request, 'welcome.html')

def user_login(request):
    if request.user.is_authenticated:
        return redirect('index')
    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            try:
                Profile.objects.get(user=request.user)
            except:
                return redirect("create_profile")
            return redirect(request.GET.get('next', 'index'))

        else:
            messages.error(request, "Invalid username or password.")
            return render(request, 'login.html')
        
    return render(request, 'Login.html')
@login_required
def user_logout(request):
    logout(request)
    return redirect('login')

    
def signup_user(request):
    if request.user.is_authenticated:
        return redirect('index')
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')


        if not all([username, email, password, confirm_password]):
            messages.error(request, "All fields are required.")
            return render(request, 'signup.html')

        password_pattern = r'^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d@$!%*?&;:,.<>()[\]{}]{8,}$'
        if not re.match(password_pattern, password):
            messages.error(request, "Password must be at least 8 characters long, include a letter و a number .")
            return render(request, 'signup.html')


        if password != confirm_password:
            messages.error(request, "Passwords do not match.")
            return render(request, 'signup.html')


        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
            return render(request, 'signup.html')

 
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already exists.")
            return render(request, 'signup.html')

        email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if not re.match(email_pattern, email):
            messages.error(request, "Invalid email address.")
            return render(request, 'signup.html')

        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('create_profile')
        messages.success(request, "Account created successfully!")
        # return redirect('create_profile')

    return render(request, 'signup.html')
@login_required
def profile(request,pk):
    try:
        Profile.objects.get(user=request.user)
    except:
        return redirect("create_profile")
    if str(request.user.id) != pk:
        return redirect('index')
    profile = Profile.objects.get(user=pk)
    data={
        'profile':profile,
    }
    return render(request,'profile.html',data)
@login_required
def edit_profile(request, pk):
    try:
        Profile.objects.get(user=request.user)
    except Profile.DoesNotExist:
        return redirect("create_profile")
    if str(request.user.id) != pk:
        return redirect('index')
    profile = Profile.objects.get(user=request.user)
    if request.method == 'POST':
        file = request.FILES.get('profile_picture')
        full_name = request.POST.get('full_name')
        username = request.POST.get('username')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        bio = request.POST.get('bio')
        username_in = User.objects.filter(username=username).exclude(username=request.user.username).exists()
        if full_name and username:
            if username_in:
                messages.error(request, "Username already exists.")
                return render(request, 'edit_profile.html', {'profile': profile})
            if file:
                profile.file = file 
            profile.full_name = full_name
            profile.username = username
            profile.phone = phone
            profile.address = address
            profile.bio = bio
            profile.save()
            request.user.username = username
            request.user.save()
            return redirect('profile', pk=pk)
        else:
            messages.error(request, "All fields are required.")
            return render(request, 'edit_profile.html', {'profile': profile})
    data = {
        'profile': profile,
        'stats': 'edit'
    }
    return render(request, 'Edit_Profile.html', data)

@login_required
def create_profile(request):
    profile = User.objects.get(id = request.user.id)
    if request.method == 'POST':
        file = request.FILES.get('profile_picture')
        full_name = request.POST.get('full_name')
        username = request.POST.get('username')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        bio = request.POST.get('bio')
        username_in=User.objects.filter(username = username).exclude(username=request.user.username).exists()
        if username:
            if username_in and full_name:
                messages.error(request, "Username already exists.")
                return render(request,'edit_profile.html')
            user = User.objects.get(id = request.user.id)
            user.username = username
            user.save()
            if file:
                profile = Profile(

                    file=file ,
                    user=user,
                    full_name=full_name,
                    phone=phone, 
                    address=address, 
                    bio=bio, 
                    email = request.user.email,
                    username=username
                    )
                profile.save()
                request.user.username = username
                request.user.save()
            else:
                print(file)
            return redirect('profile',pk=request.user.id)
    data={
        'profile':profile,
        'stats':'create'
    }
    return render(request,'edit_profile.html',data)

@login_required
def delete_account(request,pk):

    if request.method == 'POST':
        user = User.objects.get(id=pk)
        user.delete()
        return redirect('index')
    return render(request,'delete_account.html')

@login_required
def friends_profile(request,pk):
    try:
        Profile.objects.get(user=request.user)
    except:
        return redirect('create_profile')
    profile = Profile.objects.get(id=pk)
    data = {
        'profile': profile
    }
    return render(request, 'friends_profile.html', data)