from django.urls import path
from todo_app.views import todo,edit,delete

urlpatterns = [
    path('' , todo , name = 'todo'),
    path('edit/<int:id>/', edit ,name = 'edit'),
    path('delete/<int:id>/', delete ,name = 'delete'),
]