# HWAutomation Project

> :robot: **Note:** This project is designed to automate the collection and submission of homework files by reading emails and utilizing Chrome browser automation through Selenium.

## Project Overview

HWAutomation is a bot that continuously and automatically collects homework files by reading through a user's emails and collecting those with certain subject parameters. It then utilizes Selenium, a web automation tool, to submit the collected files through a Chrome browser.

The project consists of three main files:

- `main.py`: This file contains the continuous email collection automation logic. It calls the functions defined in `seleniumFuncs.py` to manipulate the Chrome browser.
- `seleniumFuncs.py`: This file contains the functions to interact with the Chrome browser using Selenium.
- `credentials.py`: This file contains the user's email and password credentials.

## :rocket: Getting Started

To get started with the HWAutomation project, follow these steps:

1. :octocat: Clone the project repository:

   ```bash
   git clone https://github.com/nguyenttleo/HWAutomation.git
   ```

2. :package: Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

   Make sure to have the necessary libraries installed for Selenium and any other dependencies required by your project.

3. :wrench: Configure email and credentials:

   - In `main.py`, update the email parameters to match your email account settings. These parameters include the email server, username, and subject parameters to filter relevant homework emails.
   - In `credentials.py`, update the `get_user()` function to return your actual email address and update the `get_pass()` function to return your email account password.

4. :gear: Configure Chrome driver:

   Download the appropriate Chrome driver for your system and update the path in `main.py` to point to the location of the Chrome driver executable.

5. :rocket: Run the `main.py` script to start the HWAutomation:

   ```bash
   python main.py
   ```

## Project Structure

The project structure is as follows:

```
HWAutomation/
├── main.py
├── seleniumFuncs.py
└── credentials.py
```

- `main.py`: This file contains the continuous email collection automation logic. It reads through emails and utilizes functions from `seleniumFuncs.py` to interact with the Chrome browser.
- `seleniumFuncs.py`: This file contains the implementation of functions to manipulate the Chrome browser using Selenium.
- `credentials.py`: This file contains the user's email and password credentials.

## Dependencies

The following dependencies are required for the project:

- selenium: Used for browser automation with Selenium WebDriver.
- (Other dependencies specific to your project)

You can install the required dependencies by running:

```bash
pip install -r requirements.txt
```

Please ensure that you have updated the necessary fields in `credentials.py` to your own email and password credentials before running the project.

Enjoy automating your homework collection and submission with HWAutomation! :computer:
