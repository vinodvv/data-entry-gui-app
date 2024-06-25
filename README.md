# Data Entry App

A simple data entry application built using PyQt6. This application allows users to enter text and submit it by pressing a button or the Enter key. The entered text is then appended to a new row in an existing CSV file.

## Features

- **User-Friendly Interface**: A clean and intuitive design ensures easy navigation and usability.
- **Quick Data Entry**: Enter text and submit with just a click or by pressing Enter.
- **CSV Integration**: Automatically appends entered data into a CSV file for easy data management and retrieval.
- **Real-Time Feedback**: Instant success and warning messages keep you informed about your entries.

## Requirements

- Python 3.x
- PyQt6

## Installation

1. **Clone the repository:**
    ```sh
    git clone https://github.com/vinodvv/data-entry-app.git
    cd data-entry-app
    ```

2. **Create and activate a virtual environment (optional but recommended):**
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the required packages:**
    ```sh
    pip install pyqt6
    ```

## Usage

1. **Run the application:**
    ```sh
    python data_entry_app.py
    ```

2. **Interact with the application:**
    - Enter text in the input field.
    - Press the Enter key or click the Submit button.
    - The entered text will be appended to `data.csv`. If `data.csv` does not exist, it will be created.
