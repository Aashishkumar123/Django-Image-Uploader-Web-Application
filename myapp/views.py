from django.shortcuts import render
from .forms import UserRegsitrationForm,UpdateUserForm,ProfileUpdateForm
from .models import ImageUploader
from django.contrib import messages
from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
# Create your views here.

def home(request):
        if request.method == "POST" and 'upload' in request.POST:
                img_name = 'img_name' in request.POST and request.POST['img_name']
                img = 'img' in request.FILES and request.FILES['img']
                u_profile = 'u_profile' in request.POST and request.POST['u_profile']


                img_uploader = ImageUploader(image_name = img_name,
                                                image = img,
                                                user=request.user,
                                                user_profile = u_profile,
                                                date=datetime.now())
                img_uploader.save()
                messages.success(request,'Your Image Uploaded Successfully !!')


        images = ImageUploader.objects.all()
        return render(request,'home.html',{'images':images})


def signup(request):
        if request.method == "POST":
                fm = UserRegsitrationForm(request.POST)
                if fm.is_valid():
                        fm.save()
                        messages.success(request,'Signup Done !!')

        else:
                fm  = UserRegsitrationForm()

        context = {'fm':fm}
        return render(request,'signup.html',context)

@login_required
def profile(request):

        if request.method == "POST":
                u_form = UpdateUserForm(instance = request.user,data=request.POST)
                p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
                if u_form.is_valid() and p_form.is_valid():
                    u_form.save()
                    p_form.save()
                    messages.success(request, f'Your Profile has been updated!')


        
        
        else:
                u_form = UpdateUserForm(instance = request.user)
                p_form = ProfileUpdateForm(instance = request.user.profile)

        return render(request,'profile.html',{'u_form':u_form,'p_form':p_form})


def user_profile(request,user):

        users = User.objects.get(username=user)
        image = ImageUploader.objects.filter(user=user)


        return render(request,'user-profile.html',{'users':users,'image':image})
