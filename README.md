
---

# Loyalty Token Management System

This project is a Django-based web application designed to manage and calculate loyalty tokens for users. Users can input their phone numbers to check their loyalty tokens, which are calculated based on their transactions. The admin panel allows managing users, transactions, and associated phone numbers.

---

## Features
- **Admin Panel**: Accessible at `/admin` for managing users, transactions, and associated phone numbers.
- **User Interface**: A form at `/showform` where users can enter their phone numbers to retrieve their loyalty tokens.
- **Dynamic Token Calculation**: Loyalty tokens are calculated based on the total of in-app transactions, package purchases, and shop transactions (1 token for every 100 units).
- **Responsive Design**: The user interface is styled for an intuitive and clean experience, optimized for different devices.

---

## Installation Guide

Follow these steps to set up the project on your local machine:

### 1. Clone the Repository
First, clone this repository to your local machine:
```bash
git clone https://github.com/your-repository/loyalty-token-system.git
cd loyalty-token-system
```

### 2. Create a Python Virtual Environment
Create a virtual environment to isolate project dependencies:
```bash
python3 -m venv venv
```

### 3. Activate the Virtual Environment
Activate the environment:
- **Linux/Mac**:
  ```bash
  source venv/bin/activate
  ```
- **Windows**:
  ```bash
  venv\Scripts\activate
  ```

### 4. Install Dependencies
Install the required packages from `requirements.txt`:
```bash
pip install -r requirements.txt
```

### 5. Apply Migrations
Run database migrations to set up the database schema:
```bash
python3 manage.py migrate
```

### 6. Start the Development Server
Launch the Django development server:
```bash
python3 manage.py runserver
```

---

## Usage

### 1. Access the Admin Panel
Visit the admin panel at `http://127.0.0.1:8000/admin` to log in. Use the superuser credentials you create with:
```bash
python3 manage.py createsuperuser
```

### 2. Access the User Form
Visit `http://127.0.0.1:8000/showform` to allow users to check their loyalty tokens by entering their phone number.

### 3. View Results
- Enter a valid phone number in the form.
- If the phone number exists, the user’s loyalty tokens and other details will be displayed.
- If the phone number doesn’t exist, an appropriate error message will be shown.

---

## Project Structure

Here’s an overview of the project structure:

```
loyalty-token-system/
├── admin_panel/
│   ├── migrations/
│   ├── templates/
│   │   ├── showform.html
│   │   ├── getscore.html
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── admin.py
├── static/
│   ├── icons/
│   │   ├── mtn-logo.png
│   │   ├── favicon.ico
│   │   └── phone-icon.png
│   └── styles/
│       └── form.css
├── templates/
│   └── base.html
├── manage.py
├── requirements.txt
└── README.md
```

- **`admin_panel`**: Core app for managing users, transactions, and phone numbers.
- **`static/`**: Contains static files like icons and CSS.
- **`templates/`**: Contains HTML templates for the user interface.
- **`manage.py`**: Django’s command-line utility.

---

## Requirements

This project requires:
- **Python 3.8+**
- **Django 4.0+**
- **SQLite** (default database)

Install all dependencies using the provided `requirements.txt`.

---

## Contributing

Feel free to fork the repository and submit pull requests for new features or bug fixes. Contributions are welcome!

---

## License

This project is licensed under the MIT License.

---

### Example Usage

1. **Launch the Server**:
   ```bash
   python3 manage.py runserver
   ```

2. **Admin Panel**:
   Navigate to `http://127.0.0.1:8000/admin` to log in with your superuser credentials and manage users and phone numbers.

3. **User Form**:
   Navigate to `http://127.0.0.1:8000/showform` to enter a phone number and view loyalty tokens.
