Risk Management Application

Overview:
The Risk Management application provides an API for managing risks within an organization. It allows the creation, retrieval, and updating of risks. The system uses a simple JSON-based file storage to store risk data, with no database required.

Features:
* Create a Risk: You can create a new risk or update an existing one.
* Retrieve All Risks: List all existing risks.
* Retrieve Risk by ID: Get details of a specific risk by its ID.

Project Structure:

RiskManagement/
│
├── manage.py                # Django management script
├── RiskManagement/
│   ├── __init__.py
│   ├── settings.py          # Settings for the application
│   ├── urls.py              # URL routing
│   ├── views.py             # Views to handle API logic
│   ├── models.py            # Contains risk model and data handling logic
│   ├── apps.py
│   ├── migrations/          # Database migrations (not used in this project)
│
├── risks.json               # File used for storing risk data (in-memory for this application)
└── README.md                # Project documentation


Installation:
Prerequisites
Ensure that you have the following installed:

Python 3.x
Django 3.x or higher
Django REST Framework
Install Dependencies from req.txt
###  cmd --> cd RiskManagement
###  cmd --> pip install -r requirements.txt
###  cmd --> pip list (to check packages are there)

In mac (Cmd + Shift + P) -- Choose Python: Select Interpreter ----> then choose the python interpreter

* * * ---- python manage.py runserver 8080
The API will be available at http://127.0.0.1:8080/



API Endpoints:
1. Create or Update a Risk
Endpoint: POST http://127.0.0.1:8080/v1/risks

Description: Create a new risk or update an existing one based on title and description.

Request Body:
{
    "title": "Title of the Risk",
    "description": "Detailed description of the risk",
    "state": "open"  // Valid states: open, closed, accepted, investigating
}
Response:
On success:
{
    "message": "Risk created successfully.",
    "risk": { ...risk details... }
}
If the risk already exists with the same title and description, it will update the state:
{
    "message": "Risk updated successfully open --> closed",
    "risk": { ...updated risk details... }
}
If there is an error:
{
    "error": "Invalid risk state open. Choose from: open, closed, accepted, investigating"
}


2. Get All Risks
Endpoint: GET http://127.0.0.1:8080/v1/risks
Description: Retrieve all the risks.
Response:
{
    "risks_count": 2,
    "risks": [
        { ...risk1 details... },
        { ...risk2 details... }
    ]
}


3. Get a Risk by ID
Endpoint: GET http://127.0.0.1:8080/v1/risks/{id}

Description: Retrieve a specific risk by its ID.

Response:

On success:
{
    "id": "12345-uuid",
    "state": "open",
    "title": "Sample Risk",
    "description": "Description of the sample risk",
    "created_at": "2024-11-12T12:00:00",
    "updated_at": "2024-11-12T12:00:00"
}
If the risk is not found:
{
    "error": "Risk not found"
}


How It Works:
* models.py
Risk Class: 
Defines a Risk object with fields such as id, state, title, description, created_at, and updated_at. The to_dict() method returns a dictionary representation of the risk.

Risk Management Functions:
* * load_risks() loads the existing risks from a JSON file.
* * save_risks() saves the current list of risks back to the JSON file.
* * get_all_risks() retrieves all the risks.
* * get_risk_by_id() retrieves a specific risk by its id.
* * check_and_create_risk() checks if a risk with the same title and description exists. If it does, the state is updated; otherwise, a new risk is created.


* views.py
API Views:
* * get_risks(): Retrieves all risks.
* * get_risk(): Retrieves a specific risk by its id.
* * create_risk_view(): 
1. Handles POST requests to create or update a risk. It validates the state and inputs, calls the corresponding logic from check_and_create_risk(), and returns a JSON response.
risks.json
2. The risks are stored in this file in JSON format. Each risk is represented as a dictionary with fields like id, state, title, description, created_at, and updated_at.

* * * Running the Application
Start the Django development server:

Error Handling
400 Bad Request: If the required fields are missing or invalid, the API will return a 400 error with a message.
404 Not Found: If a specific risk is not found by its id, the API will return a 404 error.