from django.shortcuts import render
from django.http import JsonResponse
from .models import Contacts

# Create your views here.
def hello_world(request):
    return JsonResponse({"message": "Hello, World!"})
  
def contcts_list(request):
    queryset = Contacts.objects.all()
    contacts_details = []
    for contact in queryset:
      formatted_data = {
        'name' : contact.name,
        'phone_number': contact.phone_number
      }
      contacts_details.append(formatted_data)
    
    return JsonResponse( {'contacts':contacts_details})

