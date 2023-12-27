OSRS Star Tracker - DEPRECATED

Project written to help friends locate stars. Deprecated after MVP finding an already built RuneLite extension.
Now presented publicly in all it's glory for learning purposes.

This application runs on an endless loop, scraping data every N seconds.

Setup Instructions:

1. Install Python 3 if you haven't already. You can download it from https://www.python.org/downloads/.

2. Create a virtual environment (venv) to isolate the Python environment for this project. Here's how you can do it:
   - Open a terminal.
   - Navigate to the project directory.
   - Run the following command: `python3 -m venv env`
   - This will create a new directory named `env` in your project directory.

3. Activate the virtual environment:
   - On Windows, run: `env\Scripts\activate`
   - On Unix or MacOS, run: `source env/bin/activate`

4. Once the virtual environment is activated, you should see `(env)` at the start of your terminal prompt.

5. Install the required Python packages:
   - Run the following command: `pip install -r requirements.txt`
   - This will install all the packages listed in `requirements.txt`.

6. Run the application:
   - Run the following command: `python tracker.py`
   - The application will start running and print data every minute.
