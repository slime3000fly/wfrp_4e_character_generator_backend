from django.http import JsonResponse
from django.contrib.auth.models import User
import json

def signup(request):
    if request.method == "POST":
        data = json.loads(request.body)
        username = data.get("username")
        password = data.get("password")
        
        # check if user exist
        if User.objects.filter(username=username).exists():
            return JsonResponse({"error": "user exist"}, status=400)
        
        # create user
        user = User.objects.create_user(username=username, password=password)
        
        return JsonResponse({"message": "registration succeeded"})
    else:
        return JsonResponse({"error": "method must be POST!"}, status=400)
