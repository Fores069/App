from .views import home,create,TaskUpdateView,TaskDeleteView,TaskDetailView
from django.urls import path

urlpatterns = [
    path('', home, name='home'),
    path('create/',create, name='create'),
    path('<int:pk>',TaskDetailView.as_view(), name='task-detail'),
    path('<int:pk>/update',TaskUpdateView.as_view(), name='task-update'),
    path('<int:pk>/delete',TaskDeleteView.as_view(), name='task-delete')
]
