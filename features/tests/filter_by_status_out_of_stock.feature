# Created by cedri at 5/28/2024
Feature: Test case scenerios for Reelly website
  # Enter feature description here

  #Scenario: User can filter by status Out of Stocks
    #Given Open Reely main page
    #When Log in to the page
    #Then Verify the right page opens.
    #When Filter by status of "Out of Stock".
    #Then Verify each product contains the Out of Stock tag

    Scenario: User can open the Secondary deals page and go through pagination #(Scenario-13).
      Given Open the main page
      When Log in
      When Click secondary option at the left side menu
      Then Verify the secondary page opens
      When Go to the final page using the pagination button
      When Go back to the first page using the pagination button


