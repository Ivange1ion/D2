from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import User, Note
from .forms import UserForm, NoteForm
from django.contrib.auth.hashers import make_password, check_password
# Create your views here.

def first(request):
    if (request.method=='POST') and (request.path == '/reg'):
        form=UserForm(request.POST)
        if form.is_valid:
            client=User.objects.filter(name=request.POST.get('name'))
            if not client:
                user=User()
                user.name=request.POST.get('name')
                user.password=make_password(request.POST.get('password'))
                user.save()
                return HttpResponse (f"<script>alert('Successful registration')</script>")
            else: return HttpResponse (f"<script>alert('There is user with name {request.POST.get('name')}'); window.location.href='/'</script>")
        else: return HttpResponse ("Bad request")
    elif (request.method=='POST') and( request.path == '/'):
        # form=UserForm(request.POST)
        # if form.is_valid:
        client=User.objects.get(name=request.POST.get('name'))
        if check_password(request.POST.get('password'), client.password):
            context={
                "name":client.name
            }
            return render(request, 'auth.html', context)
        else:
            return HttpResponse (f"<script>alert('Error with name or password'); window.location.href='/'</script>")
    else:
        form=UserForm()
        return render(request, 'first.html')

def main(request):
    if request.method=='POST':
        newNote=Note()
        newNote.data=request.POST.get('data')
        newNote.author=request.POST.get('author')
        newNote.save()
        return HttpResponseRedirect('home')
    else:
        return render(request, 'add.html')

def home(request):
    if request.method=='POST':
    # form=NoteForm()
        notes=Note.objects.filter(author=request.POST.get('name'))
        context={"notes":notes}
        return render(request, 'home.html', context)
    else:
        notes=Note.objects.filter(author=request.POST.get('name'))
        context={"notes":notes}
        return render(request, 'home.html', context)
        # return HttpResponse('fail')

def logout(request):
    return HttpResponse("<script> alert('You logged out'); localStorage.clear();  window.location.href='/'</script>")