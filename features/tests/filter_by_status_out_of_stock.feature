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


    Scenario: User can filter the Secondary deals by “want to sell” option
      Given  Open main page
      When Log in to the webpage
      When Click secondary option at the left side menu page
      When Verify the right page open
      When Click on filters
      When Filter the products by want to sell
      When Click on Apply filter
      Then Verify all cards have for sale tag
