from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import ToDoList, Item
from .forms import CreateNewList


# Create your views here.

def index(response,id):
    owner = ToDoList.objects.get(id=id)
    if response.method =="POST":
        if response.POST.get("save"):
            for item in owner.item_set.all():
                if response.POST.get("c"+str(item.id))=="clicked":
                    item.complete=True
                else:
                    item.complete=False
                item.save()

        elif response.POST.get("newItem"):
            text = response.POST.get("new")

            if len(text)>2:
                owner.item_set.create(text=text, complete=False)
            else:
                print("invalid")

    return render(response, "main/list.html",{"owner": owner})
    # return HttpResponse("<h1>This is my site %s </h1><hr><p>%s</p>" % (owner.name,str(item.text)))

def home(response):
    return render(response, "main/home.html",{})

def create(response):
    if response.method =="POST":
        form = CreateNewList(response.POST)

        if form.is_valid():
            n = form.cleaned_data["name"]
            t=ToDoList(name=n)
            t.save()

            response.user.todolist.add(t)
        
            return HttpResponseRedirect("/%i" % t.id)
    else:
        form = CreateNewList()
        
    return render (response , "main/create.html",{"form": form})

def view(response):
    return render(response, "main/view.html",{})
