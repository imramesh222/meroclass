from django.contrib import admin

from courses.models import Category, Course, Lesson, CourseLog

# Register your models here.

admin.site.register(Category)
admin.site.register(Course)
admin.site.register(Lesson)
admin.site.register(CourseLog)

