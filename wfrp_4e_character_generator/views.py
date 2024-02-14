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

def login(request):
    if request.method == "POST":
        data = json.loads(request.body)
        username = data.get("username")
        password = data.get("password")
        
        user = User.objects.filter(username=username).first()  # get user 

        if user and user.check_password(password):
            return JsonResponse({"message": "login succeeded"})
        else:
            return JsonResponse({"error": "wrong username or password"}, status=400)

    return JsonResponse({"error": "method must be POST!"}, status=400)

def save_json(request):
    if request.method == "POST":
        data = json.loads(request.body)
        username = data.get("username")
        json_data = data.get("json_data")

        user = User.objects.filter(username=username).first()  # get user

        if user:
            # # update json objcet
            # user.profile.json_data = json_data
            # user.profile.save()

            return JsonResponse({"message": "JSON data saved successfully"})
        else:
            return JsonResponse({"error": "User not found"}, status=400)

    return JsonResponse({"error": "Method must be POST"}, status=400)