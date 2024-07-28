from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.core import serializers
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.hashers import check_password
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from main.models import UserAccount
from django.contrib.auth.backends import BaseBackend
from add_task.models import TaskItem, SubtaskItem, AssignedContactItem
from rest_framework.views import APIView, Response
from add_task.serializers import TaskItemSerializer, SubtaskItemSerializer, AssignedContactItemSerializer, UserAccountSerializer

# Create your views here.
""" @csrf_exempt
def loginView(request):
    if request.method == 'POST':
        user = authenticate(username=request.POST.get('email'), password=request.POST.get('password'))
        
        if user:
            login(request, user)
            user_serialized = serializers.serialize('json', [user])
            print(user_serialized)
            return JsonResponse(user_serialized[1:-1], safe=False) """


@csrf_exempt
def loginView(request):
    if request.method == 'POST':
        email = request.POST['email']
        upass = request.POST['password']
        user = authenticate(username=request.POST.get('email'), password=request.POST.get('password'))

        get_user_obj = User.objects.filter(username=email).exists()
        if get_user_obj:
            get_user=User.objects.filter(username=email)
            check_pass = check_password(upass,get_user[0].password)
            if not check_pass:
                print(f"Password dose not exist with username = {get_user[0].username}")
                return JsonResponse({
                    #"id": request.id,
                    "status": 1
                })
            else:
                login(request, user)
                #user_serialized = serializers.serialize('json', [user])
                #json_user_serialized = user_serialized[1:-1]
                
                userForColor = User.objects.get(username=request.POST.get('email'))
                userColor = userForColor.useraccount.color   
                return JsonResponse({
                    "id": user.pk,
                    "username": user.username,
                    "firstname": user.first_name,
                    "lastname": user.last_name,
                    "email": user.email,
                    "userColor": userColor
                })
                
                #return JsonResponse(user_serialized[1:-1], safe=False)

        else:
            print('Username dose not exist')
            return JsonResponse({
                #"id": request.id,
                "status": 2
            })

class TasksView(APIView): 
    #authenticaiton_classes = [TokenAuthentication]
    #permission_classes = [IsAuthenticated]
    @csrf_exempt
    def get(self, request, format=None):
        #tasks = TaskItem.objects.filter(created_by=request.user)
        tasks = TaskItem.objects.filter(created_by=1)
        serializer = TaskItemSerializer(tasks, many=True)
        print(Response(serializer.data))
        return Response(serializer.data)

class SubtasksView(APIView): 
    #authenticaiton_classes = [TokenAuthentication]
    #permission_classes = [IsAuthenticated]
    @csrf_exempt
    def get(self, request, format=None):
        subtasks = SubtaskItem.objects.filter(created_by=1)
        serializer = SubtaskItemSerializer(subtasks, many=True)
        print(Response(serializer.data))
        return Response(serializer.data)

class AssignedContactView(APIView): 
    #authenticaiton_classes = [TokenAuthentication]
    #permission_classes = [IsAuthenticated]
    @csrf_exempt
    def get(self, request, format=None):
        assignedContacts = AssignedContactItem.objects
        serializer = AssignedContactItemSerializer(assignedContacts, many=True)
        print(Response(serializer.data))
        return Response(serializer.data)

class ContactsView(APIView): 
    #authenticaiton_classes = [TokenAuthentication]
    #permission_classes = [IsAuthenticated]
    @csrf_exempt
    def get(self, request, format=None):
        contacts = UserAccount.objects
        serializer = UserAccountSerializer(contacts, many=True)
        print(Response(serializer.data))
        return Response(serializer.data)
