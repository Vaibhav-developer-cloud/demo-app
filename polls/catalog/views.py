from django.shortcuts import render
from django.http import HttpResponse,HttpResponseBadRequest
# Create your views here.
from .models import Book,BookInstance,Author,Genre
from django.views import generic
from django.contrib.messages.storage import session
from django.contrib.auth.models import User
from .forms import InputForms,EmployeeForm
from .functions.functions import handle_uploaded_file

def setting_cookie(request):
    response = HttpResponse("We are getting cookie")
    response.set_cookie('Learning','Django')
    return response

def getting_cookie(request):
    first_test = request.COOKIES['Learning']
    return HttpResponse("practice:"+ first_test)

def delete_cookie(request):
    response = HttpResponse("We are getting cookie")
    response.delete_cookie('Learning',domain='127.0.0.1')
    return HttpResponseBadRequest('Successfully Deleted')

def index(request):
    #return HttpResponse("Hii This is Catalog apps")
    num_books = Book.objects.all().count()
    num_bookinstances = BookInstance.objects.all().count()
    num_author= Author.objects.all().count()
    num_instance_avail= BookInstance.objects.filter(status__exact='m').count()
    request.session['bookcount']=num_books
    bookcount = request.session.get('bookcount')

    # HttpResponse.set_cookie("LocalLibrary",'LocalLibrary.com')
    # request.COOKIES['LocalLibrary']

    cookies = request.COOKIES['Learning']

    context={
       "num_books": num_books,
        "num_bookinstances": num_bookinstances,
        "num_author": num_author,
        "num_instance_avail": num_instance_avail,
        # "bookcount":request.session["bookcount"]
         "bookcount":bookcount,
        # "cookies":cookies





    }
    return render(request,'catalog\home.html',context)

class BookListView(generic.ListView):
    model = Book
    # field =['title','isbn']
    # context_object_name = 'book_list'
    # queryset = Book.objects.filter(title__icontains='war')
    # template_name = 'catalog/book_list.html'


class BookDetailView(generic.DetailView):
    model = Book

def user_creation(request):
    user =User.objects.create_user('user3','user3@example.com','mypassword')
    user.first_name='user3'
    user.last_name ='user3'
    user.save()
    return HttpResponse('user has been created successfully')
    # print("user has been created succesfully")

def input_view(request):
    # input = Inputform()
    context = {
        # "form":input
        "form":InputForms()
    }
    return render(request,"catalog/input_view.html",context)


def employee_register(request):
    if request.method == 'POST':
        emp = EmployeeForm(request.POST,request.FILES)
        if emp.is_valid():
            handle_uploaded_file(request.FILE['file'])
            return HttpResponse("Files Uploaded Successfully")

    else:
        emp = EmployeeForm()
        context = {
            "form": emp
        }
        return render(request,'catalog/employeeform.html',context)
