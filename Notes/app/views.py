from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from rest_framework.decorators import api_view 
from rest_framework.response import Response
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from rest_framework.exceptions import AuthenticationFailed
from .serializers import *
# Create your views here.

# @login_required(login_url='/login/')
@api_view(['POST','GET'])
def getNotesOfUser(request):
    try:
        data = request.data
        username = data['username']

        user = User.objects.get(username=username)
        if user.is_authenticated:
            notes = Notes.objects.filter(user=user)

            serializer = NotesSerializer(notes, many=True)
            return Response({'status':200,'Notes':serializer.data})

    except Exception as e:
        return Response({'status':400,'message':str(e)})


# @login_required(login_url='/login/')
@api_view(['POST',])
def addNote(request):
    try:
        data = request.data
        user = User.objects.get(username=data['username'])
        if user.is_authenticated:
            note = Notes()
            note.user = user
            note.title = data['title']
            note.note = data['note']
            note.save()
            return Response({'status':200,'message':'success'})
    except Exception as e:
        return Response({'status':400,'message':str(e)})


# @login_required(login_url='/login/')
@api_view(['POST',])
def updateNote(request):
    try:
        data = request.data
        user = User.objects.get(username=data['username'])
        if user.is_authenticated:
            note = Notes.objects.get(user=user,title=data['prevtitle'])
            note.title = data['title']
            note.note = data['note']
            note.save()
            return Response({'status':200,'message':'success'})
    except Exception as e:
        return Response({'status':400,'message':str(e)})


# @login_required(login_url='/login/')
@api_view(['POST',])
def deleteNote(request):
    try:
        data = request.data
        user = User.objects.get(username=data['username'])
        if user.is_authenticated:
            note = Notes.objects.get(user=user,title=data['title'])
            note.delete()
            return Response({'status':200,'message':'success'})
    except Exception as e:
        return Response({'status':400,'message':str(e)})


@api_view(['POST',])
def registerUser(request):
    try:
        data = request.data 
        email = data['email']
        username = data['username']
        password = data['password']

        user = User.objects.create_user(username=username,email=email)
        user.set_password(password)
        user.save()
        return Response({'status':200,'message':'success'})
    except Exception as e:
        return Response({'status':404,'message':str(e)})


@api_view(['POST',])
def loginFunction(request):
    try:
        data = request.data 
        username = data['username']
        password = data['password']

        user = authenticate(request,username=username,password=password)
        try:
            if user is not None:
                login(request,user)
                return Response({'status':200,'message':'successfully logged In'})
        except AuthenticationFailed:
            return Response({'status':404,'message':'Invalid credentials'})
    except:
        return Response({'status':404,'message':'Error'})
    

@api_view(['GET',])
@login_required(login_url='/login/')
def loggingOUT(request):
    try:
        logout(request)
        return Response({'status':200,'message':'successfully logged Out'})
    except Exception as e:
        return Response({'status':404,'message':str(e)})