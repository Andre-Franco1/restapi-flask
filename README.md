# Flask REST API

A RESTful API built with **Flask**, **MongoDB**, and **Docker**, designed for learning and demonstration purposes.
The API provides operations for users and is ready for deployment in both **local** and **production** environments.

---

## Features

- **Flask REST API** with modular structure  
- **MongoDB** integration (local for dev, Atlas for production)  
- **Docker & Docker Compose** for containerized development  
- **Unit tests** with `pytest`  
- **Environment-based configuration** (development vs production)  
- Hosted on **Heroku**  

---

## Technologies

- Python 3.12  
- Flask + Flask-RESTful  
- MongoDB + MongoEngine  
- Docker & Docker Compose  
- Pytest  
- Heroku (production)  

---

## Installation & Setup

### Prerequisites

- Docker & Docker Compose  
- Python 3.12 (for local development without Docker)  

### Clone the repository

```bash
git clone https://github.com/Andre-Franco1/restapi-flask.git
cd restapi-flask
```

---

## Local Development

### Using Docker Compose
```bash
make compose
```
- This will start the Flask API and a local MongoDB instance.
- API will be available at http://localhost:5000.

### Without Docker

**1. Create virtual environment:**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

**2. Install dependencies:**
```bash
pip install -r requirements.txt
```

**3. Run the application:**
```bash
python3 wsgi.py
```
- API will run on http://127.0.0.1:5000.

---
 
## Configuration

The app uses environment-based configurations:
- DevConfig → local MongoDB
- ProdConfig → MongoDB Atlas
  
Set the following environment variables for production in the Heroku application settings 'Config Vars' after the MongoDB Atlas cluster is up and runnig:
- MONGODB_HOST
- MONGODB_USER
- MONGODB_PASSWORD
- MONGODB_DB

---

## API Endpoints

| Method | Endpoint      | Description       |
| ------ | ------------- | ----------------- |
| GET    | `/users`      | Get all users     |
| POST   | `/user`       | Create a new user |
| GET    | `/user/<cpf>` | Get user by CPF   |

Example request (POST /user):
```json
{
  "first_name": "John",
  "last_name": "Doe",
  "cpf": "635.631.290-45",
  "email": "johndoe@mail.com",
  "birth_date": "2001-01-01"
}

```

---

## Running Tests

```bash
make test
```

- Runs pytest and flake8 for code linting and unit tests.

---

## Deployment

### Heroku (Docker)

```bash
make heroku
```

- Logs into Heroku container registry, pushes the Docker image, and releases the web process.

---

## Notes

- The API is containerized using Docker; local MongoDB is used for development, and MongoDB Atlas is used in production.
- The application uses an app factory pattern, making it easier to scale and test.
