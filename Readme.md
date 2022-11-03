pytest-bdd-allure
--------------------
Automation framework using pytest with Behavior driver approach (BDD) using allure reporting to automate sample web application(chrome).




To install dependent packages execute below command:

    - pip install -r /path/to/requirements.txt

Command to Run Test suites with Allure reporting

    - behave -f allure_behave.formatter:AllureFormatter -o reports/ ./features/orangehrmlogin.feature

Report Generation

    - allure serve reports/

Framework Structure:

    --features
        --steps  # steps file
            -- orangehrmloginsteps.py
            -- orangehrmsteps.py
        --orangehrmlogin.feature  # feature file
    -- Library
        -- Functions.py # having all common functions/keywords
    -- Locators
        -- HomePage.py  # Page Locator file
    -- reports  # allure reports folder
    requirements.txt
