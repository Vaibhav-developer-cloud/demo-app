from django.shortcuts import render
from .models import Team,employee
# Create your views here.
from django.http import HttpResponse

def hello(request):
    return HttpResponse("Hello World")

def calculate(request):
    return HttpResponse(eval("100+100"))

def index(request):

    # list_teams = Team.objects.filter(team_level="u01")
    # context={
    #     "teams":list_teams
    # }
    # return render(request,'appname/index.html',context)
    #
    # names = employee.objects.filter(id="1")
    # context = {
    #     "names": names
    # }
    # print(names)
    # return render(request, 'appname/index.html', context)

    names = employee.objects.get(id="1")
    context = {
        "names": names
    }
    print(names)
    return render(request, 'appname/index.html', context)

# def __iter__(request):
#   names = employee.objects.get(id="1")
#     context = {
#         "names": names
#     }
#     print(names)
#     return render(request, 'appname/index.html', context)

