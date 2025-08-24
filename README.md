# MeroClass - Online Learning Platform

MeroClass is a RESTful API for an online learning platform built with Django and Django REST Framework. It provides endpoints to manage courses, lessons, and categories.

## Features

- **Course Management**: Create, read, update, and delete courses
- **Lesson Management**: Organize lessons within courses with ordering
- **Category System**: Categorize courses for better organization
- **Search & Filtering**: Search through courses and lessons with various filters
- **Pagination**: Efficient data loading with customizable page sizes

## API Endpoints

### Courses
- `GET /api/courses/` - List all courses
- `POST /api/courses/` - Create a new course
- `GET /api/courses/{id}/` - Get course details
- `PUT /api/courses/{id}/` - Update a course
- `DELETE /api/courses/{id}/` - Delete a course

### Lessons
- `GET /api/lessons/` - List all lessons
- `POST /api/lessons/` - Create a new lesson
- `GET /api/lessons/{id}/` - Get lesson details
- `PUT /api/lessons/{id}/` - Update a lesson
- `DELETE /api/lessons/{id}/` - Delete a lesson

### Categories
- `GET /api/categories/` - List all categories
- `POST /api/categories/` - Create a new category

## Query Parameters

### For Lessons and Courses:
- `search`: Search in title and description
- `ordering`: Order by any field (prefix with '-' for descending)
- `page`: Page number for pagination
- `page_size`: Number of items per page (default: 5, max: 100)

## Setup

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd meroclass
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run migrations:
   ```bash
   python manage.py migrate
   ```

5. Create a superuser (optional):
   ```bash
   python manage.py createsuperuser
   ```

6. Run the development server:
   ```bash
   python manage.py runserver
   ```

## Seeding Data

To populate the database with sample data:

```bash
python manage.py seed_data
```

## API Documentation

API documentation is available at `/api/` when running the development server. The documentation is interactive and allows you to test the API endpoints directly from your browser.

### Example API Requests

#### Create a new course
```bash
curl -X POST http://127.0.0.1:8000/api/courses/ \
  -H "Content-Type: application/json" \
  -u username:password \
  -d '{"title": "New Course", "description": "Course description"}'
```

#### Search and pagination
```bash
# Search for courses with pagination
curl "http://127.0.0.1:8000/api/courses/?search=python&page=1&page_size=5"
```

## Logging

The application logs important events such as:
- Course creation and updates
- Field-level changes during updates

Logs are output to the console with the following format:
```
[timestamp] New course created: Course Title (ID: 1)
[timestamp] Course updated: Course Title (ID: 1)
[timestamp] Changed fields: title: Old Title -> New Title
```

## Authentication

The API supports the following authentication methods:

1. **Session Authentication** (for web interface)
   - Log in via the Django admin interface at `/admin/`
   - Or use the browsable API login at `/api-auth/login/`

2. **Basic Authentication** (for API clients)
   ```bash
   curl -X GET http://127.0.0.1:8000/api/courses/ -u username:password
   ```

### Permissions
- **Read operations** (GET, HEAD, OPTIONS) are allowed for all users
- **Write operations** (POST, PUT, PATCH, DELETE) require authentication
- Admin users have full access to all operations

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.
