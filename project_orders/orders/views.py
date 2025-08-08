from django.http import JsonResponse

def list_orders(request):
    return JsonResponse({"orders": [1, 2, 3]})

def get_order(request, order_id):
    return JsonResponse({"order_id": order_id, "items": ["Item1", "Item2"]})

def order_status(request):
    return JsonResponse({"statuses": ["Pending", "Shipped", "Delivered"]})
