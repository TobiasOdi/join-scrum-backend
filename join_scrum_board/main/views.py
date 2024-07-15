from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.core import serializers
from django.http import JsonResponse

# Create your views here.
def loginView(request):
    wrongPassword = False
    if request.method == 'POST':
        user = authenticate(email=request.POST.get('email'), password=request.POST.get('password'))
        if user:
            login(request, user)
            serialized_obj = serializers.serialize('json', [user])
            return JsonResponse(serialized_obj[1:-1], safe=False)
            #return HttpResponseRedirect('/chat/')
        #else:
        #    wrongPassword = True
            #serialized_obj = serializers.serialize('json', [user])
            #return JsonResponse(serialized_obj[1:-1], safe=False)

        #    return render(request, 'chat/login.html', {'wrongpassword': wrongPassword})  
    return render(request, 'chat/login.html')