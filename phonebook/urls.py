
from django.urls import path, include
from phonebook.views import hello_world, contcts_list


urlpatterns = [
  path('hello/', hello_world),
  path('contacts/', contcts_list )
]
