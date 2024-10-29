from django.urls import path
from . import views

urlpatterns = [
    path('attendance/', views.attendance_view, name='attendance_view'),
    path('students/', views.student_list, name='students_list'),
    path('students/<int:student_id>/', views.student_detail, name='student_detail'),
]
