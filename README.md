## Automating Desktop Games with Python and Pytest: A Guide Using AltTester for Unity Games
### Introduction
Desktop game testing is a crucial step to ensure a smooth user experience, especially for Unity-based games. With advancements in automation frameworks, automating repetitive tasks like gameplay flows, UI validations, and error handling has become efficient and reliable. In this blog, we'll walk you through automating a Unity desktop game using Python, Pytest, and the AltTester driver.
### Pre-Requisites
Before diving into the implementation, ensure the following prerequisites are met:
### 1. Instrumented Desktop Application:

The Unity game should be built with the integrated AltTester Unity SDK.
This allows the AltTester desktop app to interact with and retrieve elements from the game.
Here is the Instrumented app link for practice purposes.

### 2. AltTester Desktop Application:
Use the AltTester desktop app to inspect and fetch game elements.
Confirm accessibility of the elements (e.g., buttons, input fields) before scripting automation tests.

AltTester will connect automatically once you open the Instrumented app.
To access elements for your app, you'll need the Pro version. However, they offer a free trial of the Pro version, which you can use for your app as well.
### 3. Python Environment:
Python 3.x installed.
Required libraries installed via pip install alttester pytest.

## Tools Overview
**Python:** A versatile language for test scripting.

**Pytest:** A powerful, easy-to-use testing framework for Python.

**AltTester Driver:** A Unity-based tool to access game elements for automation.

### Setting Up Your Automation Environment
#### To get started, ensure you have the following installed:
Python (3.x). Download and install Python from the official site.

Pytest: Install via pip: pip3 install pytest.

IDE: PyCharm Community Edition

AltTester: Download and configure the driver.

Game Build: A Unity game for desktop with the AltTester SDK integrated.


#### If you are not familiar with that, Here are the steps for adding an AltTester driver in IDE:

Go to the ```File>> Setting>> Project>> Python Interpreter>> Click on '+' Icon>>``` Search ```altTester-Driver``` and then Click on Installation Package

After installation, it will show in the list with the version.

Just create a simple POM folder structure and start creating an automation script.

### Steps for running my practice project:
1. Paste the downloaded TrashCat app into the app folder

2. Change the app path in the config.py file
```
Full path to the application
app_path = r"D:\Projects\trash-cat-desktop\app\TrashCat.exe"
```
3. Run the test
```
3. File: D:\Projects\trash-cat-desktop\test\test_play_trash_cat.py
```

https://www.linkedin.com/in/ankitpatel216/