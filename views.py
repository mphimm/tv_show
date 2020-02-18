from django.shortcuts import render, redirect
from .models import Show

def index(request):
    return render(request, "index.html")

def viewInfoPage(request,id):
    print("Running info_page")
    context = {
        "tv_show" : Show.objects.get(id=id),
    }
    return render(request, "info_page.html", context)

def create_show(request):
    currentShow = request.POST["title"]
    currentNetwork = request.POST["network"]
    currentDescription = request.POST["desc"]
    releaseDate = request.POST["date"]
    print(request.POST)
    Show.objects.create(title=currentShow, network=currentNetwork, desc=currentDescription, release_date=releaseDate)
    print("Book Submitted!!")
    return redirect("/all_shows")

def all_shows(request):
    context = {
        "all_shows" : Show.objects.all(),
    }
    return render(request, "all_shows.html", context)

def edit_process(request,id):
    print("show edited!!!!!!!")
    show = Show.objects.get(id=id)
    show.title = request.POST["editTitle"]    
    show.network = request.POST["editNetwork"]
    show.release_date = request.POST["editDate"]
    show.desc = request.POST["editDesc"]
    print("show.title", show.title)
    print("show.network", show.network)
    print("show.release_date", show.release_date)
    print("show.desc", show.desc)
    show.save()
    return redirect(f"/info_page/{id}")

def edit(request,id):
    context = {
    "tv_show" : Show.objects.get(id=id)
    }
    return render(request, "edit.html", context)

def deleteShow(request,id):
    show = Show.objects.get(id=id)
    show.delete()
    return redirect ("/all_shows")
