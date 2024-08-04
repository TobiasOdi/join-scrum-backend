from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.template.context_processors import csrf
from add_task.models import CategoryItem
from add_task.serializers import CategoryItemSerializer
from rest_framework.views import APIView, Response# Create your views here.
from add_task.models import TaskItem, AssignedContactItem, SubtaskItem
import json
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core import serializers

class CategoriesView(APIView): 
    #authenticaiton_classes = [TokenAuthentication]
    #permission_classes = [IsAuthenticated]
    @csrf_exempt
    def get(self, request, format=None):
        #tasks = TaskItem.objects.filter(created_by=request.user)
        categories = CategoryItem.objects.all()
        serializer = CategoryItemSerializer(categories, many=True)
        return Response(serializer.data)

class SaveTaskCategoryView(APIView):
    #authenticaiton_classes = [TokenAuthentication]
    #permission_classes = [IsAuthenticated]
    @csrf_exempt
    def post(self, request):
        currentTask = json.loads(request.body)
        print("JSON", currentTask['id'])
        TaskItem.objects.filter(pk=currentTask['id']).update(
            statusCategory=currentTask['statusCategory'],
        )      
        return Response({ "status": "OK - Status category updated"})
    
    
#@login_required(login_url='/login/')
class SaveCreatedTaskView(APIView):
    #authenticaiton_classes = [TokenAuthentication]
    #permission_classes = [IsAuthenticated]
    @csrf_exempt
    def post(self, request):
        currentTask = json.loads(request.body)
        print('currentTask',currentTask)
        #serialized_obj = serializers.serialize('json', [currentTask])
        #dict_currentTask = serialized_obj[1:-1]
        #print(dict_currentTask)

       
        taskData = currentTask[0]['taskData']
        print('taskData', taskData)
        subtaskData = currentTask[0]['subtaskData']
        print('subtaskData', subtaskData)
        assignedToData = currentTask[0]['assignedToData']
        print('assignedToData', assignedToData)
        
        loggedInUser = User.objects.all()
        print('LOGGED IN USER', loggedInUser)

        newTask = TaskItem.objects.create(
            category=taskData[0]['category'], 
            created_by=loggedInUser,
            description=taskData[0]['description'],
            due_date=taskData[0]['due_date'],
            priorityValue=taskData[0]['priorityValue'],
            statusCategory=taskData[0]['statusCategory'],
            title=taskData[0]['title']
            )
        print('NEW TASK', newTask)

        newSubtasks = SubtaskItem.objects.create(
            parent_task_id=newTask,
            status=subtaskData[0]['status'], 
            subtaskName=subtaskData[0]['subtaskName']
            )
        print('NEW SUBTASK', newTask)

        newAssignedContacts = AssignedContactItem.objects.create(
            parent_task_id=newTask,
            contactColor=assignedToData[0]['contactColor'], 
            first_name=assignedToData[0]['first_name'],
            last_name=assignedToData[0]['last_name'],
            user_id=assignedToData[0]['user_id']
            )
        print('NEW ASSIGNED USER', newTask)

        return Response({ "status": "OK - New task created"})
    
class SaveEditedTaskView(APIView):
    #authenticaiton_classes = [TokenAuthentication]
    #permission_classes = [IsAuthenticated]
    @csrf_exempt
    def post(self, request):
        currentTask = json.loads(request.body)
        print(currentTask)
        #taskData = currentTask[0]['']
        #subtaskData = currentTask[0]['']
        #assignedToData = currentTask[0]['']

        #TaskItem.objects.filter(pk=currentTask['id']).update(
            #category=currentTask['category'],
            #created_at=currentTask['created_at'],
            #created_by=currentTask['created_by'],
            #description=currentTask['description'],
            #due_date=currentTask['due_date'],
            #priorityValue=currentTask['priorityValue'],
        #    statusCategory=currentTask['statusCategory'],
            #title=currentTask['title'],
        #)      
        return Response({ "status": "OK - Task edited"})
