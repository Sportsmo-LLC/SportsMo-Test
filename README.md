# SportsMo - Mobile App Automation Testing

## 📌 Project Overview
SportsMo is a mobile application for sports enthusiasts. This project focuses on the **Automation Testing** of the SportsMo app using **Appium** and **Pytest**. The framework ensures robust test coverage, reliability, and automation efficiency for mobile UI testing.

## 🏗 Project Structure
```
SportsMo/
│-- pages/                  # Page Object Model (POM) implementation
│   │-- auth/               # Authentication-related page classes
│   │-- feed/               # Feed page-related classes
│   │-- impact/             # Impact page-related classes
│   │-- more/               # Miscellaneous settings, options
│   │-- pledge/             # Pledge-related test pages
│   │-- base_page.py        # Base Page with common reusable methods
│-- tests/                  # Test scripts
│   │-- auth/               # Authentication tests
│   │-- feed/               # Feed tests
│   │-- impact/             # Impact tests
│   │-- more/               # Miscellaneous tests
│   │-- pledge/             # Pledge tests
│-- venv/                   # Virtual environment for dependencies
│-- conftest.py             # Pytest fixture setup
│-- debug.log               # Debugging logs
│-- README.md               # Project documentation
│-- requirements.txt        # Dependencies file
```

## 🛠 Technologies Used
- **Python** (3.x)
- **Appium** (for Mobile UI Automation)
- **Pytest** (for test execution and reporting)
- **Selenium WebDriver** (used by Appium)
- **POM (Page Object Model)**
- **Azure DevOps** (for CI/CD integration)
- **Jenkins** (optional for automation execution)

## 📌 Setup Instructions
### 1️⃣ Clone the Repository
```sh
git clone <repo-url>
cd SportsMo
```
### 2️⃣ Create a Virtual Environment
```sh
python -m venv venv
source venv/bin/activate  # For Mac/Linux
venv\Scripts\activate     # For Windows
```
### 3️⃣ Install Dependencies
```sh
pip install -r requirements.txt
```
### 4️⃣ Start Appium Server
Make sure Appium is installed and running:
```sh
appium --relaxed-security
```

### 5️⃣ Run Tests
Execute all tests using Pytest:
```sh
pytest tests/
```
Run specific test module:
```sh
pytest tests/auth/test_auth_login.py
```

## 🏗 Framework Design
- **Page Object Model (POM)** ensures better maintainability.
- **Explicit Waits** are used to handle mobile elements.
- **Logging and Reporting** for debugging and test results.

## ✅ Test Execution & Reporting
Pytest generates reports after execution. To generate HTML reports:
```sh
pytest --html=report.html --self-contained-html
```

## 🛠 CI/CD Integration
- **Azure DevOps Pipelines** can be used to execute tests automatically.
- **Jenkins** integration is possible with scheduled test runs.

## 📌 Contributing
1. Fork the repository.
2. Create a feature branch.
3. Commit your changes.
4. Push to the branch and create a PR.

## 📝 License
MIT License © SportsMo Team.



