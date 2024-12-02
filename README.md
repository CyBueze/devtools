# DevTool API

DevTool API is a simple RESTful API that helps you list, create, update, and delete your favourite web development tools and resources.

## Features
- **Django & Django Rest Framework**: For building the backend of the RESTful API.
- **SwaggerUI**: For proper documentation and testing of the RESTful API.
- **PostgreSQL**: Planned for future versions (currently using SQLite due to technical issues).

## Tools Used
- **Django** and **Django Rest Framework** for the backend.
- **SwaggerUI** for API documentation and testing.
- **PostgreSQL** (to be added in future versions).

## Getting Started

Follow the steps below to set up the project on your local machine.

### Prerequisites

Make sure you have the following installed:
- Python 3.9+
- pip (Python package installer)
- PostgreSQL (for future versions; SQLite is used in the current version)

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/CyBueze/devtools.git
   cd devtools

2. Create a virtual environment:
  ```bash
  python3 -m venv venv

3. Activate the virtual env:
 - On macOS/Linux:
   ```bash
   source venv/bin/activate
 - On Windows:

4. Install dependencies:
  ```bash
  pip install -r requirements.txt
  
5. Apply migrations:
  ```bash
  python manage.py migrate

6. Run server:
  ```bash
  python manage.py runserver
 ```
  
7. Populate the database by running a POST request when testing the API.


I hope you enjoy using this API as much as i enjoyed creating it.