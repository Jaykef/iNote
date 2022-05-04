from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Note
from datetime import date
from django.contrib import messages
import time


def index(request):
    newnote = request.POST.get('note')
    newnotebody = request.POST.get('noteeditor')
    if request.method == 'POST':
        note = Note(note=newnote, note_body=newnotebody)
        note.save()
        data = Note.objects.all()
        n = len(data)
        parmas = {'range': n, 'data': data}
        return render(request, r'iNoteApp/index.html', parmas)
    else:
        data = Note.objects.all()
        n = len(data)
        parmas = {'range': n, 'data': data}
        return render(request, r'iNoteApp/index.html', parmas)


def note_single(request):
    if request.method == 'GET':
        note = request.GET.get('note')
        note_body = request.GET.get('note_body')
        print(note)
        print(note_body)
        parmas = {'note': note, 'note_body': note_body}
        instance = Note.objects.filter(note=note, note_body=note_body)
        instance.save()
        return render(request, r'iNoteApp/note-detail.html', parmas)


def delete(request):
    if request.method == 'GET':
        note = request.GET.get('note')
        print(note)
        parmas = {'note': note}
        instance = Note.objects.filter(note=note)
        instance.delete()
        return render(request, r'iNoteApp/delete.html', parmas)
