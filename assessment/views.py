from django.shortcuts import render
#from django.http import HttpResponse
# Create your views here.

ques_ans = [
    {
        'quest': 'Do you have thoughts of suicide?',
        '5':'Never',
        '4':'Rarely',
        '3':'Sometimes',
        '2':'Often',
        '1':'Many a times'
    },
    {
        'quest': 'Have you been a victim of ragging?',
        '5':'Never',
        '4':'Rarely',
        '3':'Sometimes',
        '2':'Often',
        '1':'Many a times'
    }
]

def home(request):
    context = {
        'questions':ques_ans
    }

    return render(request, 'assessment/home.html',context)

def about(request):
    return render(request, 'assessment/about.html',{'title':'About US'})

def index(request):
    return render(request,'assessment/index.html')