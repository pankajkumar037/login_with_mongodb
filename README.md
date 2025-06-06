# FastAPI Login System

A simple and secure user authentication system built with FastAPI, featuring user registration, login, and JWT-based authentication.



## Setup Instructions

Follow these steps to get the project up and running on your local machine.

### 1. Clone the Repository



### 2. Create a Virtual Environment

It's recommended to use a virtual environment to manage dependencies.

```bash
python -m venv .venv
```

### 3. Activate the Virtual Environment

*   **On Windows:**
    ```bash
    .venv\Scripts\activate
    ```
*   **On macOS/Linux:**
    ```bash
    source .venv/bin/activate
    ```

### 4. Install Dependencies

Install the required Python packages using `pip`.

```bash
pip install -r requirements.txt
```

### 5. Environment Variables

Create a `.env` file in the root directory of the project and add the following environment variables:

```
MONGODB_URIs="mongodb+srv://<username>:<password>@<cluster-url>/<database>?retryWrites=true&w=majority"
SECRET_KEY="YOUR_SUPER_SECRET_KEY_FOR_JWT"
ACCESS_TOKEN_EXPIRE_MINUTES="30"
```

*   **`MONGODB_URIs`**: Your MongoDB connection string. You can get this from MongoDB Atlas or your local MongoDB setup.
*   **`SECRET_KEY`**: A strong, random string used to sign your JWT tokens. You can generate one using Python:
    ```python
    import os
    import secrets
    print(secrets.token_hex(32)) # Generates a 64-character hex string
    ```
*   **`ACCESS_TOKEN_EXPIRE_MINUTES`**: The expiration time for JWT access tokens in minutes (default is 30).

## Running the Application

### Development Mode (using Uvicorn)

For local development with automatic code reloading:

```bash
uvicorn main:app --reload
```

The API will be available at `http://127.0.0.1:8000`.

### Production Mode (using Gunicorn with Uvicorn Workers)

For a production deployment, use Gunicorn to manage Uvicorn workers for better performance and stability.

```bash
gunicorn -w 4 -k uvicorn.workers.UvicornWorker main:app
```

Adjust the `-w` (workers) flag based on your server's CPU cores. A common practice is `(2 * number_of_cores) + 1`.

## API Endpoints

### 1. Register User

*   **Endpoint:** `/register`
*   **Method:** `POST`
*   **Request Body (JSON):**
    ```json
    {
        "username": "testuser",
        "school": "Example School",
        "email": "test@example.com",
        "phone_number": "1234567890",
        "class_name": "Class A",
        "password": "securepassword"
    }
    ```
*   **Response:**
    ```json
    {"msg": "User registered successfully"}
    ```

### 2. Login User

*   **Endpoint:** `/login`
*   **Method:** `POST`
*   **Request Body (JSON):**
    ```json
    {
        "login": "test@example.com",  // Can be email or phone number
        "password": "securepassword"
    }
    ```
*   **Response:**
    ```json
    {
        "access_token": "your_jwt_token_here",
        "token_type": "bearer",
        "username": "testuser",
        "email": "test@example.com",
        "phone_number": "1234567890",
        "school": "Example School",
        "Class": "Class A"
    }
    ```
