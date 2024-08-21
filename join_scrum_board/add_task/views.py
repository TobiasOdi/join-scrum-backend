from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.template.context_processors import csrf
from add_task.models import CategoryItem
from add_task.serializers import CategoryItemSerializer
from rest_framework.views import APIView, Response# Create your views here.
from add_task.models import TaskItem, AssignedContactItem, SubtaskItem
from contacts.models import ContactItem
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
        print('currentTask', currentTask)
       
        taskData = currentTask[0]['taskData']
        subtaskData = currentTask[0]['subtaskData']
        assignedToData = currentTask[0]['assignedToData']
        
        newTask = TaskItem.objects.create(
            category=taskData[0]['category'], 
            created_by=1,
            description=taskData[0]['description'],
            due_date=taskData[0]['due_date'],
            priorityValue=taskData[0]['priorityValue'],
            statusCategory=taskData[0]['statusCategory'],
            title=taskData[0]['title']
            )

        for subtask in subtaskData: 
            SubtaskItem.objects.create(
                parent_task_id=newTask,
                status=subtask['status'], 
                subtaskName=subtask['subtaskName']
            )

        for assignedContact in assignedToData:
            contactId = ContactItem.objects.filter(id=assignedContact)     
            #print("CONTACT ITEM CORRECT??", contactId)          
            AssignedContactItem.objects.create(
                parent_task_id=newTask,
                #contactColor=assignedContact['contactColor'], 
                #first_name=assignedContact['first_name'],
                #last_name=assignedContact['last_name'],
                contact_id=contactId[0]
            )

        return Response({ "status": "OK - New task created"})
    
class SaveEditedTaskView(APIView):
    #authenticaiton_classes = [TokenAuthentication]
    #permission_classes = [IsAuthenticated]
    @csrf_exempt
    def post(self, request):
        currentTask = json.loads(request.body)
        print('currentTask', currentTask)
        
        taskData = currentTask[0]['taskData']
        subtaskData = currentTask[0]['subtaskData']
        assignedToData = currentTask[0]['assignedToData']

        get_current_Task=TaskItem.objects.filter(pk=taskData[0]['id'])

        TaskItem.objects.filter(pk=taskData[0]['id']).update(
            category=taskData[0]['category'], 
            description=taskData[0]['description'],
            due_date=taskData[0]['due_date'],
            priorityValue=taskData[0]['priorityValue'],
            statusCategory=taskData[0]['statusCategory'],
            title=taskData[0]['title']
        )  
        
        # DELETE ALL SUBTASKS AND ASSIGNED CONTACTS THAT REFER TO THE CURRENT TASK
        SubtaskItem.objects.filter(parent_task_id=get_current_Task[0]).delete()
        AssignedContactItem.objects.filter(parent_task_id=get_current_Task[0]).delete()

        # ADD NEW SUBTASKS AND ASSIGNED CONTACTS
        for subtask in subtaskData: 
            SubtaskItem.objects.create(
                parent_task_id=get_current_Task[0],
                status=subtask['status'], 
                subtaskName=subtask['subtaskName']
            )

        for assignedContact in assignedToData:
            current_contact = ContactItem.objects.filter(pk=assignedContact['contact_id'])
            
            AssignedContactItem.objects.create(
                parent_task_id=get_current_Task[0],
                contact_id=current_contact[0]
            )
            
        return Response({ "status": "OK - Task edited"})


class SaveCreatedCategoryView(APIView):    
    @csrf_exempt
    def post(self, request):
        newCategory = json.loads(request.body)
        print('newCategory', newCategory)
        
        CategoryItem.objects.create(
            categoryName=newCategory['categoryName'], 
            color=newCategory['color'],
            categoryType=newCategory['categoryType'],
        )  
        
        return Response({ "status": "OK - Category created"})
    
class DeleteCategoryView(APIView):
    #authenticaiton_classes = [TokenAuthentication]
    #permission_classes = [IsAuthenticated]
    @csrf_exempt
    def post(self, request):
        currentCategory = json.loads(request.body)
        print('currentCategory', currentCategory)
        
        CategoryItem.objects.filter(id=currentCategory['id']).delete()
        return Response({ "status": "OK - Catgory deleted"})