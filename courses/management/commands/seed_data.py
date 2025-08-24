from django.core.management.base import BaseCommand
from courses.models import Course, Lesson, Category

class Command(BaseCommand):
    help = 'Seed the database with test data'

    def handle(self, *args, **options):
        # Create a category
        python_category = Category.objects.create(name='Python Programming')
        
        # Create a course
        course = Course.objects.create(
            title='Python for Beginners',
            description='Learn Python from scratch'
        )
        

        lessons = [
            {
                'title': 'Introduction to Python',
                'description': 'Learn the basics of Python programming',
                'content': 'Python is a high-level programming language...',
                'course': course,
                'category': python_category,
                'is_published': True,
                'order': 1
            },
            {
                'title': 'Python Data Types',
                'description': 'Learn about Python data types',
                'content': 'Python has several built-in data types...',
                'course': course,
                'category': python_category,
                'is_published': True,
                'order': 2
            },
            {
                'title': 'Python Functions',
                'description': 'Learn how to write functions in Python',
                'content': 'Functions are reusable blocks of code...',
                'course': course,
                'category': python_category,
                'is_published': True,
                'order': 3
            }
        ]
        
        for lesson_data in lessons:
            Lesson.objects.create(**lesson_data)
            
        self.stdout.write(self.style.SUCCESS('Successfully seeded test data'))
