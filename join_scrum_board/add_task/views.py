from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from add_task.models import CategoryItem
from add_task.serializers import CategoryItemSerializer
from rest_framework.views import APIView, Response# Create your views here.
from add_task.models import TaskItem
import json

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

class SaveCreatedTaskView(APIView):
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
        return Response({ "status": "OK - New task created"})
