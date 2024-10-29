from django.db import models
from django.utils import timezone

class WeekDay(models.Model):
    DAYS_OF_WEEK = [
        ('monday', 'Понедельник'),
        ('tuesday', 'Вторник'),
        ('wednesday', 'Среда'),
        ('thursday', 'Четверг'),
        ('friday', 'Пятница'),
        ('saturday', 'Суббота'),
        ('sunday', 'Воскресенье'),
    ]
    day = models.CharField(max_length=10, choices=DAYS_OF_WEEK, unique=True)

    def __str__(self):
        return self.get_day_display()


class Student(models.Model):
    name = models.CharField(max_length=100)
    date_joined = models.DateField(default=timezone.now)


    def __str__(self):
        return self.name


class Attendance(models.Model):
    ATTENDANCE_STATUS = [
        ('present', 'Был'),
        ('absent', 'Не был'),
        ('excused', 'Отпросился'),
    ]
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    day = models.ForeignKey(WeekDay, on_delete=models.CASCADE)
    attendance_status = models.CharField(max_length=10, choices=ATTENDANCE_STATUS)
    grade = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.student.name} - {self.get_attendance_status_display()} - Оценка: {self.grade}"
