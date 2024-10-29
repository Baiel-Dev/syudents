from django.utils.timezone import now
from django.shortcuts import render, redirect
from .models import Student, Attendance, WeekDay
from datetime import datetime
from django.shortcuts import get_object_or_404

def attendance_view(request):
    today = datetime.today().strftime('%A').lower()
    active_days = WeekDay.objects.filter(day=today)

    if not active_days.exists():
        return render(request, 'students/on_classes.html')

    students = Student.objects.all()

    if request.method == 'POST':
        for student in students:
            attendance_status = request.POST.get(f'attendance_{student.id}')
            grade = request.POST.get(f'grade_{student.id}')

            Attendance.objects.update_or_create(
                student=student,
                day=active_days.first(),
                defaults={'attendance_status': attendance_status, 'grade': grade}
            )
        return redirect('attendance_view')

    context = {
        'students': students,
        'today': today
    }

    return render(request, 'students/attendance.html', context)


def student_list(request):
    students = Student.objects.all()
    return render(request, 'students/student_list.html', {'students': students})

def student_detail(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    attendance_records = Attendance.objects.filter(student=student)
    total_days = (now().date() - student.date_joined).days
    present_count = attendance_records.filter(attendance_status='present').count()
    absent_count = attendance_records.filter(attendance_status='absent').count()
    excused_count = attendance_records.filter(attendance_status='excused').count()
    total_grades = sum([record.grade for record in attendance_records])

    context = {
        'student': student,
        'total_days': total_days,
        'present_count': present_count,
        'absent_count': absent_count,
        'excused_count': excused_count,
        'total_grades': total_grades,
    }
    return render(request, 'students/student_detail.html', context)
