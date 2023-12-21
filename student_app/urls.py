from django.urls import path
from .views import home, all_students,student_update,student_delete

urlpatterns = [
    path('', home, name='home'),
    path('all/', all_students, name='all_students'),
    path('student/<int:pk>/update/', student_update, name='student_update'),
    path('student/<int:pk>/delete/', student_delete, name='student_delete'),
]
