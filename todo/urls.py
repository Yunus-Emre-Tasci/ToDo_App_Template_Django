from django.urls import path
from .views import *

# urlpatterns = [
#     path('',todo_list,name="todo_list"),
#     path('add/',todo_add,name="todo_add"),
#     path('update/<int:pk>',todo_update,name="todo_update"),
#     path('delete/<int:pk>',todo_delete,name="todo_delete"),
# ] 

urlpatterns = [
    path('',TodoListView.as_view(),name="todo_list"),
    path('add/',TodoCreateView.as_view(),name="todo_add"),
    # path('update/<int:pk>',todo_update,name="todo_update"),
    # path('delete/<int:pk>',todo_delete,name="todo_delete"),
] 