from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from testApp import forms
# Create your views here.
@login_required
def home_page_view(request):
    return render(request, 'testApp/home.html')
@login_required
def java_exams_view(request):
    return render(request,'testApp/java.html')
@login_required
def python_exams_view(request):
    return render(request, 'testApp/python.html')
@login_required
def aptitude_exams_view(request):
    return render(request, 'testApp/aptitude.html')

def logout_view(request):
    return render(request, 'testApp/logout.html')

def signup_view(request):
    form = forms.SignUpForm()
    if request.method == "POST":
        form = forms.SignUpForm(request.POST)
        if form.is_valid():
            user=form.save()
            user.set_password(user.password)
            user.save()
            return redirect('/accounts/login')
    return render(request, 'testApp/signup.html',{'form':form})