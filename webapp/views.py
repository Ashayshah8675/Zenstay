from django.shortcuts import render, HttpResponse, redirect
# from django.contrib.auth.decorators import login_required
# from webapp.forms import RegisterUserForm, UserProfileForm
from .models import *
from .forms import *
# from django.contrib.auth import authenticate ,login,logout,update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm,PasswordChangeForm

# Create your views here.
def index(request):
  return render(request,"index.html")

def About(request):
  feedData = abouttesti.objects.all()
  data = {
    "feedData" : feedData
  }
  return render(request,'about.html',data)

def Restaurant(request):
  if request.method == "POST":
    name = request.POST.get('name')
    email = request.POST.get('email')
    date = request.POST.get('date')
    people = request.POST.get('people')
    timeslot = request.POST.get('timeslot')
    roomno = request.POST.get('roomno')
    message = request.POST.get('message')
    formData = bookingtable(name=name, email=email , date=date, people=people, timeslot=timeslot, roomno=roomno, message=message)
    formData.save()
  return render(request,'restaurant.html')

def Spa(request):
  return render(request,'spa.html')

def Holiday(request):
  if request.method == "POST":
     name = request.POST.get('name')
     date = request.POST.get('date')
     people = request.POST.get('people')
     ename = request.POST.get('ename')
     request = request.POST.get('request')
     email = request.POST.get('email')
     formdata = eventdetailform(name=name, date = date, people=people, ename=ename, email=email,request=request)
     formdata.save()
  return render(request,'holiday.html')

def Wedding(request):
  if request.method == "POST":
     name = request.POST.get('name')
     date = request.POST.get('date')
     people = request.POST.get('people')
    #  ename = request.POST.get('ename')
     request = request.POST.get('request')
     email = request.POST.get('email')
     formdata = eventdetailform(name=name, date = date, people=people, email=email,request=request)
     formdata.save()
  return render(request,'wedding.html')

def Corporate(request):
  if request.method == "POST":
     name = request.POST.get('name')
     date = request.POST.get('date')
     people = request.POST.get('people')
     ename = request.POST.get('ename')
     request = request.POST.get('request')
     email = request.POST.get('email')
     formdata = eventdetailform(name=name, date = date, people=people, ename=ename, email=email)
     formdata.save()
  return render(request,'corporate.html')

def Event(request):
  
  return render(request,'event.html')

def Activities(request):
  return render(request,'activities.html')

def Cab(request):
  if request.method == "POST":
     name = request.POST.get('name')
     date = request.POST.get('date')
     number = request.POST.get('number')
     airport = request.POST.get('airport')
     time = request.POST.get('time')
     formdata = cabdetailform(name=name, date = date, number=number,airport=airport,time=time)
     formdata.save()
  return render(request,'cab.html')
def Sample(request):
  return render(request,'sample.html')

def Gym(request):
  return render(request,'gym.html')

def Booking(request):
  if request.method == "POST":
    name = request.POST.get('name')
    email = request.POST.get('email')
    checkin = request.POST.get('checkin')
    checkout = request.POST.get('checkout')
    adultnum = request.POST.get('adultnum')
    childnum = request.POST.get('childnum')
    roomnum = request.POST.get('roomnum')
    req = request.POST.get('request')
    formData = bookingdetailform(name=name , email=email, checkin=checkin, checkout=checkout, adultnum=adultnum, childnum=childnum, roomnum=roomnum, request=req)
    formData.save()
  return render(request,'booking.html')
  
   
def contact(request):
  if request.method == "POST":
    name = request.POST.get('name')
    email = request.POST.get('email')
    subject = request.POST.get('subject')
    message = request.POST.get('message')
    formData = contactform(name=name, email=email , subject=subject, message=message)
    formData.save()
  return render(request,'contact.html')

def Room(request):
  feedData = roomtesti.objects.all()
  roomData = roomtype.objects.all()
  data = {
    "feedData" : feedData,
    "roomData" : roomData
  }
  return render(request,'room.html', data)

def Service(request):
  feedData = services.objects.all()
  data = {
    "feedData" : feedData,
  }
  return render(request,'service.html', data)

def Team(request):
  feedData = team.objects.all()
  data = {
    "feedData" : feedData
  }
  return render(request,'team.html', data)

def Testimonial(request):
  feedData = testimonial.objects.all()
  data = {
    "feedData" : feedData,
  }
  return render(request,'testimonial.html',data)  

def login_user(request):
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        loginData = Register.objects.all().filter(username = username , password1 = password).count()

        if loginData>0:
          request.session['IS_LOGIN'] = True
          request.session['username'] = username
          return redirect("index.html")
        
        else:
          messages.error(request,"Wrong Username or Password")
          return redirect("login.html")
    return render(request,"login.html")
    
    
    

def logout_user(request):
    del request.session['IS_LOGIN']  
    messages.success(request, ("Logout Successfull !!"))
    return redirect('login.html')

def register_user(request):
    if request.method == 'POST':
      fname = request.POST.get('first_name')
      lname = request.POST.get('last_name')
      user_name = request.POST.get('username')
      email = request.POST.get('email')
      password1 = request.POST.get('password1')
      password2 = request.POST.get('password2')
      registrationData = Register(fname=fname , lname=lname , username = user_name , email=email , password1=password1 , password2 = password2)
      registrationData.save()
        # form = RegisterUserForm(request.POST)
        # if form.is_valid():
        #     form.save()
        #     username = form.cleaned_data['username']
        #     password = form.cleaned_data['password1']
        #     user = authenticate(username=username,password=password)
        #     login(request, user)
      
      messages.success(request, "Registration Successfull !!")
      return redirect('login.html')
    return render(request,"register.html")




def profile_user(request):
    return render(request,'profile.html')


def edit_profile(request):
    user_profile, created = UserProfile.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=user_profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = UserProfileForm(instance=user_profile)

    return render(request, 'editprofile.html', {'form': form})



def change_password(request):
    # if request.method == 'POST':
    #     form = PasswordChangeForm(request.user, request.POST)
    #     if form.is_valid():
    #         user = form.save()
    #         update_session_auth_hash(request, user)  # To keep the user logged in
    #         return redirect('profile')
    # else:
    #     form = PasswordChangeForm(request.user)
    return render(request, 'changepassword.html')