from rest_framework import serializers
from .models import Course, CourseLog, Lesson, Category

class CourseLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseLog
        fields = ['action', 'timestamp', 'changes']

class CourseSerializer(serializers.ModelSerializer):
    logs = CourseLogSerializer(many=True, read_only=True)
    
    class Meta:
        model = Course
        fields = ['id', 'title', 'description', 'created_at', 'updated_at', 'logs']
        read_only_fields = ['created_at', 'updated_at', 'logs']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'slug']
        read_only_fields = ['slug']

class LessonSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    category_id = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(),
        source='category',
        write_only=True,
        required=False,
        allow_null=True
    )
    
    class Meta:
        model = Lesson
        fields = [
            'id', 'title', 'slug', 'description', 'content',
            'course', 'category', 'category_id', 'is_published',
            'order', 'created_at', 'updated_at'
        ]
        read_only_fields = ['slug', 'created_at', 'updated_at']
        extra_kwargs = {
            'course': {'required': True}
        }
    
    def create(self, validated_data):
        # Handle category assignment
        category = validated_data.pop('category', None)
        lesson = Lesson.objects.create(**validated_data)
        if category:
            lesson.category = category
            lesson.save()
        return lesson
