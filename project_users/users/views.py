from django.http import JsonResponse

def hello(request):
    return JsonResponse({"message": "Hello from Users app!"})

def get_user(request, user_id):
    return JsonResponse({"user_id": user_id, "name": f"User{user_id}"})

def list_users(request):
    return JsonResponse({"users": ["User1", "User2", "User3"]})
