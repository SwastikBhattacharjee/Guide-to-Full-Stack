
# Beginner's Guide to Full Stack

This project is designed to teach beginners how **APIs**, **databases**, **frontend**, and **backend** work together to create a web application.

The application consists of two parts:

1.  A **Flask backend** that acts as an API to handle data storage and retrieval.
2.  A **frontend** (HTML, CSS, and JavaScript) to interact with the API.

----------
****

# What You'll Learn

### 1. **Frontend**

The frontend is what the user sees and interacts with. In this project, the frontend:

-   Collects student information (name, class, and age).
-   Sends the data to the backend API.
-   Retrieves and displays student data from the backend.

Key technologies:

-   **HTML**: Structure of the webpage.
-   **CSS**: Styles and designs the page.
-   **JavaScript**: Adds interactivity and communicates with the backend.

****
### 2. **Backend**

The backend is the server-side logic that processes requests and manages data. In this project:

-   We use **Flask**, a Python web framework, to create an API.
-   Data is stored in a file called `database.json`.

Key concepts:

-   **API**: An interface that allows the frontend and backend to communicate.
-   **JSON**: A lightweight format to store and exchange data.

****

### 3. **Two Servers**

To run this project, you need two servers:

1.  **Flask Server**: To host the backend API (`api.py`).
2.  **Web Server**: To serve the frontend (`index.html`). A simple tool like **Web Server for Chrome** can be used.

----------

****
# Project Structure

```
.
├── index.html          # Frontend HTML structure
├── style.css           # CSS for styling the application
├── script.js           # JavaScript for frontend logic
├── api.py              # Backend API using Flask
├── database.json       # File-based database for storing student data

```

----------
****

# How to Set Up

### 1. Flask Backend (API)

1.  Install Python (if not already installed).
2.  Install required libraries:
    
    ```bash
    pip install flask flask-cors
    
    ```
    
3.  Run the Flask server:
    
    ```bash
    python api.py
    
    ```
    
4.  The server will start on `http://127.0.0.1:5000`.

----------

### 2. Frontend (HTML + JavaScript)

1.  Install **Web Server for Chrome**:
    -   Go to the Chrome Web Store and install the **Web Server for Chrome** extension.
2.  Serve the `index.html` file:
    -   Open Web Server for Chrome.
    -   Select the folder containing the project files.
    -   Start the server.

By default, Web Server for Chrome runs on `http://127.0.0.1:8887`. Open this URL in your browser to see the frontend.

----------
****

# How It Works

1.  **Add Student**:
    
    -   Fill out the "Name," "Class," and "Age" fields in the **Student Application Form**.
    -   Click **Submit** to send the data to the Flask API.
    -   The API adds the data to `database.json`.
2.  **Fetch Student**:
    
    -   Enter the student’s name in the **Student Data Fetch Form**.
    -   Click **Fetch** to retrieve their information from the API.
    -   The data (class and age) will be displayed in the placeholders.

----------
****

# Definitions and Concepts

### API (Application Programming Interface)

An API allows the frontend and backend to communicate. In this project:

-   `GET /getStudent/<username>` retrieves a student's data.
-   `GET /addStudent` adds a student's data to the database.

****

### JSON (JavaScript Object Notation)

JSON is used to store and exchange data in a lightweight, easy-to-read format. Example:

```json
{
  "John": {
    "class": "5",
    "age": "10"
  }
}

```

****

### Flask

Flask is a Python framework for creating web applications and APIs.

****

### Web Server

A web server is software that serves HTML files to the browser. Tools like **Web Server for Chrome** are simple and effective for this purpose.

****

----------

# Key Steps for Beginners

1.  **Understand the Flow**:
    
    -   Frontend collects data → sends to backend → backend processes data → responds to frontend.
2.  **Set Up Two Servers**:
    
    -   Flask for backend (`http://127.0.0.1:5000`).
    -   Web Server for frontend (`http://127.0.0.1:8887`).
3.  **Experiment with the Code**:
    
    -   Modify the frontend (e.g., change styles or form fields).
    -   Add more API endpoints to the backend.

----------
****

# Troubleshooting

-   **CORS Issues**:  
    If the browser blocks requests from the frontend to the backend, ensure `Flask-CORS` is installed and enabled in `api.py`.
    
-   **Server Errors**:  
    Check that both servers are running, and URLs in `script.js` match the server addresses.
    

----------

# Future Additions

-   Add features like updating or deleting student records.
-   Replace the JSON file with a proper database like SQLite.
-   Enhance the UI for better usability.

----------

This project is a starting point to understand how web development works. Feel free to explore and build upon it! 😊