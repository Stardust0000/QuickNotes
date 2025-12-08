from django.shortcuts import get_object_or_404, render, redirect
from .models import Notes
from .forms import NotesForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def home(request):    
    if request.method == "POST":
        if not request.user.is_authenticated:
            return redirect("login")

        form = NotesForm(request.POST) #save -> insert new row
        if form.is_valid():
            note = form.save(commit=False)
            note.user = request.user
            note.save()
            # form.save()
            return redirect("home")
        else:
            messages.error(request, form.errors['text'][0])
    else: 
        form = NotesForm() #empty -> create mode

    if request.user.is_authenticated:
        notes = Notes.objects.filter(user=request.user).order_by('status')
    else:
        notes = [] #show empty list
    return render(request, 'home.html', {"form":form, "notes" : notes})

def edit_notes(request, id):
    note = Notes.objects.get(id=id, user=request.user)
    if request.method == "POST":
        form = NotesForm(request.POST, instance=note) # save -> update exisiting row
        if form.is_valid():
            form.save()
            return redirect("home")
        else:
            messages.error(request, form.errors['text'][0])
    else:
        form = NotesForm(instance=note) #pre-filled -> edit mode
    notes = Notes.objects.filter(user=request.user).order_by('status')
    return render(request, 'home.html', {"form":form, "notes" : notes})

def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST) #POST method, insert->validate->save
        if form.is_valid():
            form.save()
            return redirect("login")
        else:
            messages.error(request, form.errors)
    else:
        form = UserCreationForm() #GET method, just display
    return render(request, 'signup.html', {"form":form})

def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        pwd = request.POST.get('password')
        user = authenticate(request, username=username, password=pwd)
        if user:
            login(request, user)
            return redirect("home")
        else:
            messages.error(request, 'Invalid username or password')
    return render(request, "login.html") 

def logout_view(request):
    logout(request)
    return redirect('login')

def delete_notes(request,id):
    if request.method == "POST":
        Notes.objects.filter(id=id, user=request.user).delete()
    return redirect("home")

def status_toggle(request, id):
    note = get_object_or_404(Notes, id=id, user=request.user)
    if note:
        note.status = not note.status
        note.save()
    return redirect("home")