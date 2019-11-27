from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
def home_page_view(request):
    return render(request,'venkyapp/home.html')
@login_required
def aptitude_page_view(request):
    return render(request,'venkyapp/aptitudexam.html')

def grneralscience_page_view(request):
    return render(request,'venkyapp/grneralsciencexam.html')

def resonaning_page_view(request):
    return render(request,'venkyapp/resonaningexam.html')
def logout_view(request):
    return render(request,'venkyapp/logout.html')

def signup_view(request):
    form=signupForm()
    if request.method=='POST':
        User=form.save()
        User.set_password(user.password)
        User.save()
        return HttpResponseRedirect('/accounts/login')
    return render(request,'venkyapp/signUp.html',{'form':form})
