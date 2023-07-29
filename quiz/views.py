from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from .models import *
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from collections import deque,defaultdict
# Create your views here.
@login_required
def index(request):
    user=request.user
    exams=Exam.objects.all()
    context={'user': user,'exams': exams}
    return render(request,'index.html',context)

def register(request):
    if request.method=='POST':
        username=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')
        password2=request.POST.get('password2')
        # return redirect('register')
        if username!='' and password!='' and password==password2 and email!='':
            if User.objects.filter(email=email).exists():
                messages.warning(request,'Email already in use')
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.warning(request,'Username already in use')
                return redirect('register')
            else:
                user=User.objects.create_user(username=username,email=email,password=password)
                user.save()
                userlogin=authenticate(username=username,password=password)
                login(request,userlogin)
                return redirect('quiz-index')
        elif username=='':
            messages.warning(request,'Enter the username')
            return redirect('register')
        elif email=='':
            messages.warning(request,'Enter the email ID')
            return redirect('register')
        elif password =='' or password!=password2:
            messages.warning(request,'Confirmation password did not match with the given password')
            return redirect('register')
    else:
        return render(request,'register.html')
    
def customlogin(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('quiz-index')
        else:
            messages.warning(request,'Invalid Credentials. Please put down correct username and password')
            return redirect('login')
    return render(request,'login.html')

@login_required
def customlogout(request):
    logout(request)
    return redirect('login')


@login_required
def selectsections(request,exam):
    user=request.user
    sections=Section.objects.all()
    print(exam)
    context={'user': user,'sections': sections,'exam': exam}
    return render(request,'section.html',context)

@login_required
def questions(request,exam,section):
    user=request.user
    section=Section.objects.get(name=section)
    questions=Question.objects.filter(section=section)
    optlist=[]
    if request.method == 'POST':
        for qind in range(len(questions)):
            res= request.POST.get(str(qind))
            print(res)
            optlist.append(res)
        anslist=[]
        for q in questions:
            anslist.append(q.ans)
        score=0
        for o,a in zip(optlist,anslist):
            if o==a:
                score+=1
        context={'user': user,'score': score}
        exam=Exam.objects.get(name=exam)
        Quizlog.objects.create(user=user,score=score,exam=exam,section=section)
        messages.success(request,'you can see the result of quiz in the Quiz logs')
        return redirect('quiz-index')
    context={'user': user,'questions': questions}
    return render(request,'questions.html',context)

@login_required
def quizlog(request):
    user=request.user
    quizzes=Quizlog.objects.filter(user=user)
    print(quizzes)
    context={'quizzes':quizzes}
    return render(request,'quizzes.html',context)