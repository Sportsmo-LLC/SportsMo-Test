# SportsMo Mobile App Automation

## Setup
1. Install Python 3.x
2. Install Appium Server
3. Install Android SDK
4. Connect Android device or start emulator
5. Install requirements: `pip install -r requirements.txt`

## Running Tests
1. Start Appium server
2. Connect Android device/emulator
3. Run tests: `pytest -v`
4. Generate report: `pytest --html=reports/report.html`

## Project Structure
- `pages/`: Page Object Models
- `tests/`: Test cases
- `utils/`: Utility functions and configurations
- `resources/`: Test data and other resources
- `reports/`: Test execution reports
