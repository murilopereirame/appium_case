# Appium Case
This automation was developed with purpose of studying and learn how to automate tests in Android. The app used during the
tests was a simple To Do app that can be found at this [GitHub](https://github.com/murilopereirame/kotlin_case) repository.

## How to Set Up and Run
1. Install latest Node.js LTS;
2. Install Appium 2 through the following command:
    ```bash
    npm install -g appium
    ```
3. Set up Android environment variable ANDROID_SDK_ROOT 
   ```bash
   #Unix System
    export ANDROID_SDK_ROOT=~/Android/Sdk
   
   #Windows System  
    set ANDROID_SDK_ROOT=C:\Users\{YOUR_USER_NAME}\AppData\Local\Android\Sdk 
   ```
4. Install UiAutomator2 Driver:
    ```bash
   appium driver install uiautomator2
   ```
5. Install Python 3;
6. Install Appium-Python-Client:
    ```bash
    pip install Appium-Python-Client
    ```
7. Run this code:
    ```bash
   python main.py
   ```

## To Do
- [ ] Code refactoring
- [ ] Save test results
- [ ] Add this automation to a CI/CD workflow
- [ ] Publish the results somewhere