# Report Maker
## Set up
1. Unzip the downloaded folder
2. Ensure Python3, Pip3 and Flask are installed on the machine
3. Navigate to the root directory (report_maker/) on a console
4. Activate the virtualenv by typing in `source report_maker/bin/activate`
5. Install the requirements by calling `pip3 install -r requirements.txt`
6. Run the flask app locally with `flask run`

## Using the app
To use the app, open a web browser of your choosing and go to [localhost:5000/index](localhost:5000/index). Once on the main home page, you will see a table of all the data from the Suade database. Select which organisation you wish to generate a report for and what format you want it to be in (XML or PDF). The file should automatically download to your machine. You can further see the file being generated inside the app directory under report_<id>. 
  
## Testing
Tests can be found in test_suade_app.py. To run the tests, enter `pytest` into the console once in the root directory. To see coverage, run `coverage run test_suade_app.py` and to see the report `coverage report suade_app/*.py`. Tests are limited due to time constraints of the challenge but rest assured there has been rigorous manual testing.  
