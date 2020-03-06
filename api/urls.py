from django.urls import path
from tasks.views import TaskListView

helper_patterns = [
    path('tarefas/', TaskListView.as_view(), name='tarefas'),

]

urlpatterns = helper_patterns