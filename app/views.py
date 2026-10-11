from django.shortcuts import render, redirect
from django.contrib import messages
# Create your views here.
from django.http import HttpResponse
from .models import Note
def indexView(req):
    notes = Note.objects.all()
    return render(req,'index.html',context={
        'notes':notes
    })
def aboutView(req):
    return render(req,'about.html')
def contactView(req):
    return render(req,'contact.html')

def saveDataView(req):
    # print(req.POST)
    title = req.POST.get("title",) 
    description = req.POST.get("description",)
    if not title or not description:
        messages.error(req,'Fill all Field')
        return redirect("/")
    note = Note(title = title, description=description)
    note.save()
    messages.success(req,"Details saved")
    return redirect("/")

def deleteView(req,id ): 
    note = Note.objects.get(id = id)
    note.delete()
    messages.success(req,"Note Deleted")
    return redirect("/")

def updateViewPage(req,id):
    note = Note.objects.get(id = id)
    if req.method == "POST":
        title = req.POST.get("title","") 
        description = req.POST.get("description","")
        published = req.POST.get("published","")
        published = True if published == 'on' else False
        print(published)
        if not title or not description:
            messages.error(req,'Fill All Details')
        note.title = title
        note.description = description
        note.isPublish = published
        note.save()
        messages.success(req,"Details Updated")
    note = Note.objects.get(id = id)
    return render(req,"editNote.html",context={
        "note":note  
    })