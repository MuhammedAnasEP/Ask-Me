from django.shortcuts import render, redirect
from posts.views import home
from django.contrib import messages
from django.contrib.auth.models import User, auth
from posts.models import Question, Answer, UpVotes, DownVotes, Comments, CustomUser
from .forms import ProfileForm

# Create your views here.
def signup(request):
    if request.user.is_authenticated:
        return redirect(home)
        
    if request.method == "POST":
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']
        user_name = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirmpassword']
        
        if password == confirm_password:
            if CustomUser.objects.filter(username = user_name).exists():
                messages.info(request,"Username already exisst!")
                return redirect(signup)

            if CustomUser.objects.filter(email = email).exists():
                messages.info(request,"Email already exists!")
                return redirect(signup)

            user = CustomUser.objects.create_user(first_name = first_name, last_name = last_name, username = user_name, email = email, password = password)
            user.save()
            return redirect(home)

        messages.info(request, "Password is not matching!")

    return render(request, "signup.html")

def signin(request):
    if request.user.is_authenticated:
        return redirect(home)
        
    if request.method == "POST":
        user_name = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=user_name, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect(home)
        else:
            messages.info(request, "Invalid Credentials!")
            return redirect(signin)
    else:
        return render(request, "login.html")

def signout(request):
    if request.user.is_authenticated:
        auth.logout(request)
    return redirect(home)


def profile(request):
    quests=Question.objects.filter(user=request.user).order_by('-id')
    answers=Answer.objects.filter(user=request.user).order_by('-id')
    comments=Comments.objects.filter(user=request.user).order_by('-id')
    upvotes=UpVotes.objects.filter(user=request.user).order_by('-id')
    downvotes=DownVotes.objects.filter(user=request.user).order_by('-id')
    if request.method=='POST':
        profileForm=ProfileForm(request.POST,instance=request.user)
        if profileForm.is_valid():
            profileForm.save()
            messages.success(request,'Profile has been updated.')
    form=ProfileForm(instance=request.user)
    return render(request,'profile.html',{
        'form':form,
        'quests':quests,
        'answers':answers,
        'comments':comments,
        'upvotes':upvotes,
        'downvotes':downvotes,
    })