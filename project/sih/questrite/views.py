from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import QuestionsP

# Create your views here.

def index(request):
    return render(request, 'index.html')

def signup(request):

    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:

            if User.objects.filter(username = username).exists():
                messages.info(request, 'username already taken')
                return redirect('signup')

            elif User.objects.filter(email = email).exists():
                messages.info(request, 'email already taken')
                return redirect('signup')            
            else:
                user = User.objects.create_user(username = username, password = password1, email = email, first_name = first_name, last_name = last_name)
                user.save()
                return redirect ('about')

        else:
            messages.info(request, 'password not matching')
            return redirect('signup')

        return redirect('/')

    else:
        return render(request, 'signup.html')


def logout(request):
    auth.logout(request)
    return redirect('/')

    

def about(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username = username, password = password)

        if user is not None:
            auth.login(request, user)

            return redirect("/")

        else:
            messages.info(request, "invalid credentials")
            return redirect('about')

    else:
        return render(request, 'about.html')

def analyst(request):
    return render(request, 'analyst.html')

def contactus(request):
    return render(request, 'contactus.html')

def faqs(request):
    return render(request, 'faqs.html')

def mcq1(request):
    return render(request, 'mcq1.html')

def mcq2(request):
    return render(request, 'mcq2.html')

def mcq3(request):
    return render(request, 'mcq3.html')

def ourservices(request):
    return render(request, 'ourservices.html')

def personality(request):
    return render(request, 'personality.html')

def result(request):
    return render(request, 'result.html')

def resultp(request):
    return render(request, 'resultp.html')

def reviews(request):
    return render(request, 'reviews.html')

def test1(request):
    return render(request, 'test1.html')

def test2(request):
    return render(request, 'test2.html')

def test3(request):
    return render(request, 'test3.html')


def mcq4(request):
    if request.method =="POST":
        q1 =request.POST['GROUP1']
        ans = QuestionsP(questions= 1, answers = q1)
        ans.save()
        answers = QuestionsP.objects.all()
        
        for a in answers:
            print(a.questions)
            print(a.answers)
            
    else:
        return render (request,'mcq4.html')


