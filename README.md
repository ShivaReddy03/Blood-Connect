## Blood Connect

## Overview

**Blood Connect** is a Django-based web application designed to facilitate the management of blood donations and patient requests. The primary goal of this system is to collect and manage donor and patient information efficiently. By matching blood groups of donors and patients, the application ensures that patients in need of blood receive timely assistance from available donors.

## Features

**Blood Connect** offers the following features:
- **User Authentication**: Users can log in through Django's default authentication system.
- **Donor Registration**: Donors can provide their personal and medical details to be registered in the system.
- **Patient Blood Requests**: Patients can submit their blood requirements, including the specific blood group needed.
- **Matching System**: The application matches patient requests with available donors based on blood group compatibility and facilitates communication.

## Technologies Used

- **Django**: A high-level Python web framework for rapid development.
- **Python 3.x**: The programming language used for backend development.
- **SQLite**: The default database for storing data.
- **HTML/CSS**: For frontend design and styling.

## Installation

To set up the project locally, follow these steps:

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/ShivaReddy03/blood-connect.git
    cd blood-connect
    ```

2. **Create and Activate a Virtual Environment**:
    ```bash
    python -m venv venv
    ```

    - On Windows:
      ```bash
      venv\Scripts\activate
      ```

    - On macOS/Linux:
      ```bash
      source venv/bin/activate
      ```

3. **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Apply Database Migrations**:
    ```bash
    python manage.py migrate
    ```

5. **Create a Superuser**:
    ```bash
    python manage.py createsuperuser
    ```

6. **Run the Development Server**:
    ```bash
    python manage.py runserver
    ```

   You can now access the application by navigating to `http://127.0.0.1:8000/` in your web browser.

## Usage

The application includes:
- **Login Page**: Accessible at `/login/` for user authentication.
- **Donor Registration**: Donors can register their details, including personal and medical information.
- **Patient Blood Requests**: Patients can submit requests specifying the blood group they need.
- **Matching and Notification**: The system will match patient requests with donor availability based on blood group and facilitate the process of connecting donors with patients.

## Contributing

To contribute to **Blood Connect**:
1. Fork the repository to create your own copy.
2. Create a new branch for your changes (`git checkout -b feature-branch`).
3. Implement your changes and commit them (`git commit -am 'Add new feature'`).
4. Push the branch to your fork (`git push origin feature-branch`).
5. Submit a Pull Request to the original repository.

## Contact

For any questions or feedback about **Blood Connect**, please contact:

- **Shiva**: shivareddykoppula03gmail.com

