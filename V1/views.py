from django.db.models import Q
from django.shortcuts import render
from .models import Course

def index(request):
    courses = Course.objects.all()
    errors = []
    semester = ''
    level = ''
    department_name = ''

    if request.method == 'POST':
        semester = int(request.POST.get('semester'))
        level = int(request.POST.get('level'))
        department_name = request.POST.get('department_name')

        courses = courses.filter(
            Q(semester__iexact=semester) &
            Q(level__iexact=level) &
            Q(department_name__icontains=department_name)
        )

        if courses.exists():
            for course in courses:
                course.electives = course.electives.split(';')
            context = {
                'courses': courses,
            }
            return render(request, 'response.html', context)
        else:
            errors.append('Course not found!')
            user_messages = True
            context = {
                'semester': semester,
                'user_messages': user_messages,
                'level': level,
                'department_name': department_name,
                'errors': errors
            }
            return render(request, 'index.html', context)

    return render(request, 'index.html')


