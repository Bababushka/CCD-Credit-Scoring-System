# Credit Scoring System

This is a full-stack corporate credit scoring system that uses AI to analyze financial documents and assess risk. It consists of a **Python Backend** (FastAPI) and a **React Frontend**.

## 🚀 Quick Start Guide

Follow these instructions to get the project running on your local machine.

### 1. Prerequisites

Before you begin, make sure you have the following installed:

*   **Node.js** (v18 or higher): [Download here](https://nodejs.org/)
    *   To check if installed, open a terminal and run: `node -v`
*   **Python** (v3.9 or higher): [Download here](https://www.python.org/downloads/)
    *   To check if installed, open a terminal and run: `python --version`
*   **Git**: [Download here](https://git-scm.com/downloads)

### 2. Backend Setup (The Server)

The backend handles the data, AI processing, and database.

1.  **Open a terminal** (Command Prompt or PowerShell) in the project root folder.
2.  **Navigate to the backend folder**:
    ```bash
    cd backend
    ```
3.  **Create a virtual environment** (this keeps your project dependencies isolated):
    ```bash
    python -m venv venv
    ```
4.  **Activate the virtual environment**:
    *   **Windows (Command Prompt)**:
        ```cmd
        venv\Scripts\activate
        ```
    *   **Windows (PowerShell)**:
        ```powershell
        .\venv\Scripts\Activate.ps1
        ```
    *   *Note: If you see an error about scripts being disabled in PowerShell, run `Set-ExecutionPolicy RemoteSigned -Scope CurrentUser` and try again.*
    *   **Mac/Linux**:
        ```bash
        source venv/bin/activate
        ```
    *   *You should see `(venv)` at the beginning of your command line.*

5.  **Install the required libraries**:
    ```bash
    pip install -r requirements.txt
    ```

6.  **Set up Environment Variables**:
    *   Create a new file named `.env` inside the `backend` folder.
    *   Copy the contents from `.env.example` into your new `.env` file.
    *   **Important**: You will need to fill in your Azure API keys for the AI features to work fully. For local testing without AI, you can leave the defaults or ask the project owner for keys.

7.  **Start the Backend Server**:
    ```bash
    uvicorn app.main:app --reload
    ```
    *   You should see a message saying "Application startup complete".
    *   The backend is now running at `http://localhost:8000`.
    *   Keep this terminal window **OPEN**.

### 3. Frontend Setup (The User Interface)

The frontend is the web page you interact with.

1.  **Open a NEW terminal window** (do not close the backend terminal).
2.  **Navigate to the app folder** (from the project root):
    ```bash
    cd app
    ```
3.  **Install dependencies**:
    ```bash
    npm install
    ```
4.  **Set up Environment Variables**:
    *   Create a new file named `.env` inside the `app` folder.
    *   Add the following line to it:
        ```ini
        VITE_API_URL=http://localhost:8000
        ```
    *   *This tells the frontend to talk to your local backend server.*

5.  **Start the Frontend**:
    ```bash
    npm run dev
    ```
    *   You should see a message like "Local: http://localhost:3000/".
    *   Open your web browser and go to **http://localhost:3000**.

### 4. How to Use

1.  Open your browser to `http://localhost:3000`.
2.  You should see the Dashboard.
3.  **Login** with one of the default accounts:
    *   **Admin**: `admin` / `password` (or `admin@ccd.com`)
    *   **Manager**: `manager` / `password` (or `manager@ccd.com`)
    *   **Analyst**: `analyst` / `password` (or `analyst@ccd.com`)

## 📂 Project Structure

*   **`backend/`**: The server code (Python/FastAPI).
    *   `app/`: Main application logic.
    *   `app/main.py`: Entry point for the server.
    *   `requirements.txt`: List of Python libraries.
*   **`app/`**: The frontend code (React).
    *   `src/`: Source code for the UI.
    *   `package.json`: List of JavaScript libraries.

## 🛠 Troubleshooting

*   **"Port already in use"**:
    *   If `localhost:8000` or `localhost:3000` is busy, check if you have another instance of the app running. Close other terminal windows and try again.
*   **"python is not recognized"**:
    *   Make sure you checked "Add Python to PATH" during installation. You may need to restart your computer.
*   **"npm is not recognized"**:
    *   Make sure Node.js is installed and you restarted your terminal.
*   **PowerShell Security Error**:
    *   If `.\venv\Scripts\Activate.ps1` fails, run: `Set-ExecutionPolicy RemoteSigned -Scope CurrentUser` and confirm with `Y`.

## 📚 API Documentation

Once the backend is running, you can view the API documentation at:
*   [http://localhost:8000/docs](http://localhost:8000/docs) (Swagger UI)
*   [http://localhost:8000/redoc](http://localhost:8000/redoc) (ReDoc)
