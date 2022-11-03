Feature: OrangeHRM Login
  Background: Common Steps
    Given I launch Chrome Browser
    When I open orange HRM Homepage

  Scenario: Login to OrangeHRM with Valid Parameters
    Then Enter username "admin" and password "admin123"
    And Click on Login button
    Then User must successfully login to the Dashboard page
#
  Scenario: Login to OrangeHRM with InValid Parameters
    Then Enter username "invalid" and password "admin123"
    And Click on Login button
    Then User must get Invalid Credentials error

#  Scenario: Navigate to Recruitmen2

  Scenario: Validate that correct entries are listed for valid search
    Then Enter username "admin" and password "admin123"
    And Click on Login button
    When Navigate to page "Recruitment"
    Then Recruitment page should display
    When User selects "Vacancy" filter as "Senior QA Lead"
    And Click on Search button
    Then Verify only "Senior QA Lead" vacancies are listed


