from django.shortcuts import render
from django.views.generic import ListView
from .models import Task, Message


class TaskListView(ListView):
    model = Task
    template_name = 'another/tasks.html'
    context_object_name = 'tasks'
    queryset = Task.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Список задач'
        return context


class MessageListView(ListView):
    model = Message
    template_name = 'another/messages.html'
    context_object_name = 'messages'
    queryset = Message.objects.all()