# Student Information System with GitHub Integration

## 1. Project Overview

The Student Information System is a Python-based command-line application designed to manage student records efficiently. It demonstrates CRUD (Create, Read, Update, Delete) operations, JSON data persistence, modular software design, configuration management, error handling, logging, and GitHub version control.

This project was developed as an exam project to demonstrate software development and cloud-ready architecture concepts.

## 2. Objectives

* Develop a functional system for managing student information.
* Implement CRUD operations for student records.
* Store and retrieve data using JSON.
* Apply modular programming and separation of concerns.
* Use external configuration files.
* Implement error handling and logging.
* Use GitHub for source code management and collaboration.
* Include documentation and unit tests.

## 3. Features

### Student Data Management

* Add new student records.
* View all student records.
* Find a student by student ID.
* Update existing student information.
* Delete student records with confirmation.
* Search students by ID, name, course, or email.
* Export student records to a JSON file.

### Data Validation and Persistence

* Validate required fields.
* Check numeric inputs such as age and year level.
* Store student records in a JSON file.
* Load saved records when using the application.

### Application Architecture

* Modular code organized into models, services, and utilities.
* External configuration through `config/config.json`.
* Error handling for common application errors.
* Logging of failed operations.
* Unit tests for student service functionality.

## 4. Technologies Used

* **Programming Language:** Python
* **Data Storage:** JSON
* **Development Environment:** Visual Studio Code
* **Version Control:** Git
* **Code Hosting:** GitHub
* **Testing:** Python `unittest` framework

The application uses Python's standard library and does not require third-party packages.

## 5. Project Structure

```text
student-info-system/
├── src/
│   ├── models/
│   │   └── student.py
│   ├── services/
│   │   └── student_service.py
│   ├── utils/
│   │   ├── config.py
│   │   └── logger.py
│   └── main.py
├── data/
│   └── students.json
├── config/
│   └── config.json
├── logs/
├── tests/
│   └── test_student_service.py
├── .gitignore
├── README.md
└── requirements.txt
```

## 6. Installation and Setup

### Prerequisites

* Python 3.10 or later
* Visual Studio Code (recommended)
* Git and a GitHub account for version control

### Step 1: Clone the Repository

Replace `YOUR-USERNAME` with your GitHub username.

```bash
git clone https://github.com/YOUR-USERNAME/student-info-system.git
```

### Step 2: Open the Project Folder

```bash
cd student-info-system
```

Open this folder in Visual Studio Code.

### Step 3: Run the Application

From the project root directory, run:

```bash
python -m src.main
```

On Windows, if the `python` command is unavailable, try:

```bash
py -m src.main
```

## 7. How to Use the Application

When the application starts, a menu appears with the following options:

| Option | Function                       |
| ------ | ------------------------------ |
| 1      | Add a student                  |
| 2      | View all students              |
| 3      | Find a student by ID           |
| 4      | Update student information     |
| 5      | Delete a student               |
| 6      | Search students                |
| 7      | Export student records to JSON |
| 0      | Exit the application           |

Enter the number of the desired option and follow the prompts displayed in the terminal.

## 8. Configuration Management

The application uses `config/config.json` to store external settings, including the application name, data file path, log file path, and logging level.

Keeping configuration separate from the application code makes the project easier to maintain and adapt to different environments.

## 9. Error Handling and Logging

The application validates user inputs and handles common errors, such as invalid values and failed student record operations.

Logging is configured through the utility module. Failed operations are recorded to help with troubleshooting and maintenance.

## 10. Testing

The project includes unit tests for student service operations.

To run the tests from the project root directory, use:

```bash
python -m unittest discover -s tests -v
```

On Windows, you can also use:

```bash
py -m unittest discover -s tests -v
```

## 11. Cloud-Ready Architecture

The project follows cloud-ready design principles through modular organization, external configuration, JSON-based data persistence, error handling, and logging.

**Current deployment status:** This is a local command-line application. It is not currently hosted as a public website or connected to cloud database storage. The architecture can be extended for cloud deployment in the future.

## 12. GitHub Integration

GitHub is used to store and manage the project's source code and version history.

Recommended version control practices include:

* Use meaningful commit messages.
* Commit related changes in logical steps.
* Use a feature branch when developing a new feature.
* Merge completed and tested changes into the main branch.
* Keep the README updated as the project changes.

## 13. Challenges Faced

The following are example challenges that may be included if they accurately describe your experience:

* Organizing the application into separate modules while ensuring the modules work together correctly.
* Handling invalid user inputs and missing student records.
* Maintaining student data in JSON format.
* Configuring file paths and logging.
* Learning to run, test, and manage a Python project in Visual Studio Code.
* Setting up GitHub version control and maintaining a clear project history.

## 14. Future Improvements

* Add a graphical or web-based user interface.
* Integrate a cloud database.
* Add user authentication and access control.
* Deploy the application to a cloud platform.
* Add automated testing and continuous integration.

## 15. Project Information

* **Project Name:** Student Information System with GitHub Integration
* **Course/Subject:** [Enter your course or subject]
* **Student Name:** [Enter your name]
* **GitHub Repository URL:** [Paste your repository URL here]

---

*This project was created for educational purposes to demonstrate Python programming, student record management, modular architecture, and GitHub version control.*
