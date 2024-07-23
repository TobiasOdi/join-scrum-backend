from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from add_task.models import CategoryItem
from add_task.serializers import CategoryItemSerializer
from rest_framework.views import APIView, Response# Create your views here.
from add_task.models import TaskItem

class CategoriesView(APIView): 
    #authenticaiton_classes = [TokenAuthentication]
    #permission_classes = [IsAuthenticated]
    @csrf_exempt
    def get(self, request, format=None):
        #tasks = TaskItem.objects.filter(created_by=request.user)
        categories = CategoryItem.objects
        serializer = CategoryItemSerializer(categories, many=True)
        return Response(serializer.data)

class SaveTasksView(APIView):
    @csrf_exempt
    def post(self, request):
        print(request.body)
        return Response({ "status": "ok"
                        })

    """         currentTask = TaskItem.objects.get(id=request.POST['textmessage'])
            currentTask.category = request.POST  # change field
            currentTask.created_at = 999  # change field
            currentTask.created_by = 999  # change field
            currentTask.description = 999  # change field
            currentTask.due_date = 999  # change field
            currentTask.priorityValue = 999  # change field
            currentTask.statusCategory = 999  # change field
            currentTask.title = 999  # change field
            currentTask.save() # this will update only
            
            
            myChat = Chat.objects.get(id=1)
            new_Message = Message.objects.create(text=request.POST['textmessage'], chat=myChat, author=request.user, receiver=request.user)
            serialized_obj = serializers.serialize('json', [new_Message])
            return JsonResponse(serialized_obj[1:-1], safe=False)
        chatMessages = Message.objects.filter(chat__id=1) # chat__id=1 > Man schaut von der Message auf das Objekt Chat mit der id 1
        return render(request, 'chat/index.html', {'messages': chatMessages}) """