from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from .models import Contact, Blogs
from django.views.decorators.csrf import csrf_exempt
import json
from django.http import JsonResponse


# Create your views here.
def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    if (request.method == 'POST'):
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        msg = request.POST.get("msg")
        contact = Contact.objects.create(firstName= fname, lastName= lname, email=email, message=msg)
        contact.save()
        return redirect('/')
    return render(request, 'contact.html')

def blog(request):
    blogs = Blogs.objects.all()
    return render(request, "blog.html",{'blogs':blogs})

def login(request):
    if (request.method == "POST"):
        username = request.POST.get('username')
        password = request.POST.get('password')
        check_user = authenticate(username=username, password=password)
        if (check_user is not None):
            auth_login(request, check_user)
            return redirect('/')
        else:
            # wrong username or password
            return redirect('/login')
    return render(request, "login.html")

def signup(request):
    if (request.method == "POST"):
        firstName = request.POST.get('fname')
        lastName = request.POST.get('lname')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        check_user = User.objects.filter(username=username).first()
        if(check_user):
            return redirect('/signup')
        else:
            create_account = User.objects.create_user(username, email, password)
            create_account.first_name = firstName
            create_account.last_name = lastName
            create_account.save()
            return redirect('/login')
    return render(request, "signup.html")

def display_contact(request):
    if request.user.is_superuser:
        contact_list = Contact.objects.all()
        return render(request, 'displayContact.html', {"contacts":contact_list})
    else:
        return redirect('/')

def create_blog(request):
    if request.user.username:
        if request.method == "POST":
            username = request.user.username
            firstName = request.user.first_name
            lastName = request.user.last_name
            email = request.user.email
            title = request.POST.get('title')
            image = request.FILES.get('img')
            content = request.POST.get("content")
            blog = Blogs.objects.create(username=username, firstName=firstName, lastName=lastName, email=email, title=title, image=image, content=content)
            blog.save()
            return redirect('/')
        return render(request, "createBlog.html")
    else:
        print(request.user)
        return redirect('/')

# @csrf_exempt
def view_blog(request):
    if request.method == 'POST':
        # blogId = json.load(request)['blogId']
        blogId = request.POST.get('blogId')
        fetchBlog = Blogs.objects.filter(id=blogId).first()
        # data = {
        #     'title': str(fetchBlog.title),
        #     'username': str(fetchBlog.username),
        #     'img-name': str(fetchBlog.image),
        #     'content': str(fetchBlog.content)
        # }
        return render(request, 'viewBlog.html', {'blog':fetchBlog})
    return redirect('/blog')

def logout(request):
    auth_logout(request)
    return redirect('/login')

