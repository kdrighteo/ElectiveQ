from django.db import models

# Create your models here.

class Course(models.Model):
    department_name = models.CharField( max_length=100)
    semester = models.IntegerField()
    level = models.IntegerField()
    electives = models.CharField( max_length=1000)

    def __str__(self):
        return f'{self.department_name} - Level({self.level}) for Semester {self.semester}'