from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import uuid


# Create your views here.
def say_hello(request):
    # return HttpResponse("Hello World")
    return render(request, "hello.html")


@csrf_exempt  # Disable CSRF for this view. Be cautious using this in production.
def generate_uuid_view(request):
    if request.method == "POST":
        # Generate a new UUID
        new_uuid = uuid.uuid4()
        return JsonResponse({'uuid': str(new_uuid)})
    else:
        return JsonResponse({'error': 'This endpoint only supports POST requests'}, status=405)
