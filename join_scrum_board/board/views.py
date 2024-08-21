from django.shortcuts import render
import json
from rest_framework.views import APIView, Response# Create your views here.
from add_task.models import TaskItem


# Create your views here.
class DeleteTaskView(APIView):
    #authenticaiton_classes = [TokenAuthentication]
    #permission_classes = [IsAuthenticated]
    def post(self, request):
        currentTask = json.loads(request.body)
        print('currentTask', currentTask)
        
        TaskItem.objects.filter(id=currentTask['id']).delete()
        return Response({ "status": "OK - Task deleted"})