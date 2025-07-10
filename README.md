# File Share Project

This project is a Django REST Framework application designed for secure file sharing. It features JWT authentication, email verification, and a user-friendly interface for uploading and managing files.

## Project Features

- User registration and authentication using JWT.
- Email verification for new users.
- File upload, download, and management.
- Download tokens and download count tracking.
- Admin dashboard for managing users and files.
- Responsive web interface with client and operator dashboards.

## DevOps Features Added

To demonstrate practical DevOps skills suitable for internship applications, the following features have been added:

- **Dockerfile**: Containerizes the Django app using Python 3.11, installs dependencies, runs migrations, collects static files, and starts the server on port 8000.
- **docker-compose.yml**: Defines the web service for local development, simplifying environment setup.
- **GitHub Actions CI Workflow**: Automates continuous integration by running on push and pull requests to:
  - Set up Python environment
  - Install dependencies
  - Run linting with flake8
  - Run tests using Django's test runner
- **Simple Test Case**: Added a basic test in the `home` app to demonstrate testing for CI.

## Getting Started

### Prerequisites

- Docker and Docker Compose installed
- Python 3.11+ (for local development without Docker)
- Git (optional, for cloning the repository)

### Running with Docker

Build the Docker image:

```bash
docker build -t django-file-share .
```

Run the container:

```bash
docker run -p 8000:8000 django-file-share
```

Alternatively, use Docker Compose for local development:

```bash
docker-compose up --build
```

This will start the Django development server accessible at `http://localhost:8000`.

### Running Tests

To run tests locally:

```bash
python manage.py test home
```

This runs the test suite for the `home` app, including the simple test case added for CI demonstration.

### Linting

Lint the codebase using flake8:

```bash
flake8 .
```

This helps maintain code quality and consistency.

## Notes

- The project uses SQLite for simplicity and ease of setup.
- Email backend is configured for console output during development.
- For production, update email settings and database configuration accordingly.
- Static files are collected to `staticfiles` directory during Docker build.

## License

This project is for educational purposes and internship demonstration.
