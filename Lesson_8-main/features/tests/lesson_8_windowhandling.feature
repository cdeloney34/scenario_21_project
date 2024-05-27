# Created by cedri at 5/1/2024
Feature: Create a window handling test case
and verify that a user can open Terms and Conditions


  Scenario: User can open and close Terms and Conditions from sign in page.
    Given Open sign in page
    And Store original window
    When Click on Target terms and condition link
    Then Verify Terms and Conditions page is opened
    When User can close new window
    When Close current page
    Then switch back to original