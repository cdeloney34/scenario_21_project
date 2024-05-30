# Created by cedri at 4/30/2024
Feature: Verify user can access sign in page

  Scenario: Verify user can access sign in page
    Given Open Target main page
    When Click signin button
    When click right navigation sign in
    Then Verify Sign in form opened