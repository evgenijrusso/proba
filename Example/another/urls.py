from django.urls import path

from Example.another.views import TaskListView, MessageListView

urlpatterns = [
    path('another/', TaskListView.as_view(), name='tasks'),
    path('another/messages', MessageListView.as_view(), name='messages'),
]