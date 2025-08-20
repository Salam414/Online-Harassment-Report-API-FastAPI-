# Online Harassment Report API (FastAPI)

A simple REST API built with FastAPI for handling online harassment reports. This API allows users to submit reports, view all reports, filter by platform, and manage report data.

## Problem Statement

Online harassment is a significant issue across digital platforms. This API provides a lightweight solution to:
- Allow users to report harassment incidents
- Store and manage harassment reports
- Filter reports by platform
- Provide basic CRUD operations for report management

## Features

- Submit individual harassment reports
- Submit multiple reports in bulk
- View all reports with count
- Filter reports by platform
- Delete reports by ID
- Automatic API documentation with Swagger UI
- Data validation with Pydantic models
- Fast performance with FastAPI

## API Endpoints

### 1. POST `/report` - Submit Single Report

Submit a new harassment report.

**Request Body:**
```json
{
  "reporter_name": "John Doe",
  "description": "User was sending threatening messages in chat",
  "platform": "Discord"
}
```

**Response (200 OK):**
```json
{
  "message": "Report submitted successfully",
  "report": {
    "reporter_name": "John Doe",
    "description": "User was sending threatening messages in chat",
    "platform": "Discord"
  }
}
```

### 2. POST `/reports/bulk` - Submit Multiple Reports

Submit multiple harassment reports at once.

**Request Body:**
```json
[
  {
    "reporter_name": "Alice Smith",
    "description": "Spam messages in group chat",
    "platform": "WhatsApp"
  },
  {
    "reporter_name": "Bob Johnson",
    "description": "Inappropriate content shared",
    "platform": "Instagram"
  }
]
```

**Response (200 OK):**
```json
{
  "message": "2 reports submitted",
  "reports": [
    {
      "reporter_name": "Alice Smith",
      "description": "Spam messages in group chat",
      "platform": "WhatsApp"
    },
    {
      "reporter_name": "Bob Johnson",
      "description": "Inappropriate content shared",
      "platform": "Instagram"
    }
  ]
}
```

### 3. GET `/reports` - Get All Reports

Retrieve all harassment reports.

**Response (200 OK):**
```json
{
  "total_reports": 3,
  "reports": [
    {
      "reporter_name": "John Doe",
      "description": "User was sending threatening messages in chat",
      "platform": "Discord"
    },
    {
      "reporter_name": "Alice Smith",
      "description": "Spam messages in group chat",
      "platform": "WhatsApp"
    },
    {
      "reporter_name": "Bob Johnson",
      "description": "Inappropriate content shared",
      "platform": "Instagram"
    }
  ]
}
```

### 4. GET `/reports/filter?platform={platform_name}` - Filter Reports by Platform

Filter reports by specific platform.

**Example:** `GET /reports/filter?platform=Discord`

**Response (200 OK):**
```json
{
  "platform": "Discord",
  "count": 1,
  "reports": [
    {
      "reporter_name": "John Doe",
      "description": "User was sending threatening messages in chat",
      "platform": "Discord"
    }
  ]
}
```

### 5. DELETE `/report/{report_id}` - Delete Report by ID

Delete a specific report by its index ID.

**Example:** `DELETE /report/0`

**Response (200 OK):**
```json
{
  "message": "Report deleted",
  "report": {
    "reporter_name": "John Doe",
    "description": "User was sending threatening messages in chat",
    "platform": "Discord"
  }
}
```

**Error Response (Invalid ID):**
```json
{
  "error": "Invalid report ID"
}
```

## How to Run

### Prerequisites
- Python 3.7 or higher
- pip (Python package installer)

### Step 1: Set up the project

Create a new folder for your project:
```bash
mkdir harassment-report-api
cd harassment-report-api
```

### Step 2: Create the main file

Create a file named `main.py` and copy your FastAPI code into it.

### Step 3: Create requirements.txt

Create a `requirements.txt` file with the following content:
```
fastapi==0.104.1
uvicorn[standard]==0.24.0
pydantic==2.5.0
```

### Step 4: Install dependencies

```bash
pip install -r requirements.txt
```

### Step 5: Run the server

```bash
uvicorn main:app --reload
```

**Expected Output:**
```
INFO:     Will watch for changes in these directories: ['/path/to/your/project']
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process [12345] using StatReload
INFO:     Started server process [12346]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
```

### Step 6: Access the API

- **API Base URL:** http://127.0.0.1:8000
- **Interactive API Docs (Swagger UI):** http://127.0.0.1:8000/docs
- **Alternative API Docs (ReDoc):** http://127.0.0.1:8000/redoc

## Testing the API

You can test the API using curl commands, the interactive Swagger UI, or tools like Postman.

### Using Curl Commands:

**1. Submit a Report:**
```bash
curl -X POST "http://127.0.0.1:8000/report" \
  -H "Content-Type: application/json" \
  -d '{
    "reporter_name": "John Doe",
    "description": "User was sending threatening messages",
    "platform": "Discord"
  }'
```

**2. Get All Reports:**
```bash
curl "http://127.0.0.1:8000/reports"
```

**3. Filter Reports by Platform:**
```bash
curl "http://127.0.0.1:8000/reports/filter?platform=Discord"
```

**4. Submit Bulk Reports:**
```bash
curl -X POST "http://127.0.0.1:8000/reports/bulk" \
  -H "Content-Type: application/json" \
  -d '[
    {
      "reporter_name": "Alice",
      "description": "Spam messages",
      "platform": "WhatsApp"
    },
    {
      "reporter_name": "Bob",
      "description": "Inappropriate content",
      "platform": "Instagram"
    }
  ]'
```

**5. Delete a Report:**
```bash
curl -X DELETE "http://127.0.0.1:8000/report/0"
```

### Using Swagger UI:

1. Open http://127.0.0.1:8000/docs in your browser
2. You'll see an interactive interface with all endpoints
3. Click on any endpoint to expand it
4. Click "Try it out" to test the endpoint
5. Fill in the required parameters and click "Execute"

## Project Structure

```
harassment-report-api/
├── main.py              # Main FastAPI application
├── requirements.txt     # Python dependencies
├── README.md           # Project documentation
└── __pycache__/        # Python cache (auto-generated)
```

## Data Model

### Report Model
```python
class Report(BaseModel):
    reporter_name: str    # Name of person reporting
    description: str      # Description of the incident
    platform: str        # Platform where harassment occurred
```

## Error Handling

The API includes basic error handling:

- **400 Bad Request**: When no reports are provided in bulk submission
- **422 Unprocessable Entity**: When request data doesn't match the expected schema
- **Custom Error**: When trying to delete a report with invalid ID

## Features of FastAPI

This API leverages several FastAPI features:

1. **Automatic API Documentation**: Swagger UI and ReDoc
2. **Data Validation**: Automatic validation with Pydantic models
3. **Type Hints**: Full Python type hint support
4. **Fast Performance**: High performance async framework
5. **Easy Testing**: Built-in testing capabilities


## Next Steps

### Immediate Improvements:
1. **Database Integration**: Replace in-memory list with a database (SQLite, PostgreSQL, MongoDB)
2. **Better ID System**: Use UUIDs instead of array indices for report IDs
3. **Status Tracking**: Add status field (pending, investigating, resolved)
4. **Timestamps**: Add created_at and updated_at fields
5. **Input Validation**: Add more robust validation (email format, text length limits)

### Advanced Features:
1. **Authentication**: Add user authentication and authorization
2. **Rate Limiting**: Prevent spam submissions
3. **File Uploads**: Allow evidence attachments
4. **Email Notifications**: Send confirmations and alerts
5. **Search Functionality**: Full-text search across reports
6. **Analytics Dashboard**: Report statistics and trends
7. **API Versioning**: Version your API endpoints
8. **Caching**: Add Redis caching for better performance
9. **Logging**: Comprehensive logging and monitoring
10. **Docker Deployment**: Containerize the application

### Production Considerations:
- Environment configuration
- Security headers
- HTTPS enforcement
- Database migrations
- Background job processing
- Load balancing
- Monitoring and alerting

## Security Notes

⚠️ **Important**: This is a basic implementation for learning purposes. For production use:

- Add proper authentication and authorization
- Implement input sanitization
- Use environment variables for sensitive data
- Add rate limiting to prevent abuse
- Implement proper error handling and logging
- Use HTTPS in production

---

**Happy coding!** 🚀
