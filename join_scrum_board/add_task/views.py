from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from add_task.models import CategoryItem
from add_task.serializers import CategoryItemSerializer
from rest_framework.views import APIView, Response# Create your views here.

class CategoriesView(APIView): 
    #authenticaiton_classes = [TokenAuthentication]
    #permission_classes = [IsAuthenticated]
    @csrf_exempt
    def get(self, request, format=None):
        #tasks = TaskItem.objects.filter(created_by=request.user)
        categories = CategoryItem.objects
        serializer = CategoryItemSerializer(categories, many=True)
        return Response(serializer.data)