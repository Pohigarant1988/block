from django.http import JsonResponse
from django.shortcuts import render

def hello_view(request):
    return JsonResponse(
        {
            "message": "Hello World!",
            "status": "success",
        }
    )


