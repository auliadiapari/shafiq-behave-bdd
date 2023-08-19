Feature: Shafiq Login
  
  Scenario: successfully Login with valid credentials
    Given user launch Chrome Browser
    When user open shafiq home page and go to login page
    And user enter email "aulia.diapari@gmail.com" and password "Riverdale06!"
    And user click on login button
    Then user must successfully login to the dashboard page
  
  Scenario: successfully Logout from dashboard profile
    When user perform logout
    Then user redirected to home page

  Scenario: successfully Forgot Password
    Then user navigate to forgot password page
    When user enter email "aulia.diapari@gmail.com" and submit
    Then user will notify the validation message