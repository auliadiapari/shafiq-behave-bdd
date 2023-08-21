To run the test and generate the report with Allure-Behave:

Run the test:
1. install the requirements.txt

Please pay attention when the test running and encountering image verifications after clicking captcha, you should complete the image puzzle/selections
   
3. to run specific file:  behave fileName.feature
4. to run all feature file: behave

Please change the "email, password, and others data in order to testing", its tested with my credents.
       
Generate Report:
1. pip install allure-behave
2. behave -f allure_behave.formatter:AllureFormatter -o reports/ features

once the directory reports is generated, then try:
3. allure serve reports/

if allure serve reports/ is not worked, try to install:
4. npm install -g allure-commandline

then back to command no 3


Link to Test case: https://docs.google.com/spreadsheets/d/1a8J6YeBcxdiaY3FtGPgF4FZhrwtJjM5WjOzU5v2_7qk/edit?usp=sharing
