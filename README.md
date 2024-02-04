
# LavaLab Coding Project

This project is a web application built using FastAPI. Follow the steps below to set up and run the application on your local machine.

## Prerequisites

Before you begin, ensure you have Python installed on your machine. This project requires Python 3.6+.

## Installation Steps

### 1. Install Python

If you don't have Python installed, download and install it from [python.org](https://www.python.org/downloads/). Ensure you add Python to your system's PATH during the installation process.

### 2. Install Pip

Pip is Python's package installer. It's included by default with Python 3.4+ versions. To check if you have pip installed, run the following command in your terminal:

```bash
pip --version
```

If pip is not installed, [follow these instructions](https://pip.pypa.io/en/stable/installing/) to install it.

### 3. Install Python Dependencies

Navigate to the project's root directory in your terminal and run the following command to install the required Python packages:

```bash
pip3 install -r requirements.txt
```

This command will install all the dependencies listed in the `requirements.txt` file.

### 4. Run the Application

Use Uvicorn, an ASGI server, to run the application. In the project's root directory, execute:

```bash
uvicorn app:app --reload
```

The `--reload` flag enables auto-reloading of the server when you make changes to the code.

### 5. Accessing the Application

Open your web browser and go to:

```
http://127.0.0.1:8000
```

This is the home page of the application.

### 6. Admin Dashboard

To access the admin dashboard, navigate to (username: admin, password: admin1234):

```
http://127.0.0.1:8000/admin
```

Here you can manage the application's settings and data.

## Troubleshooting

If you encounter any issues while setting up or running the project, ensure that:

- You are using Python 3.6 or higher.
- All dependencies are correctly installed.
- Uvicorn is running and the terminal does not show any errors.
