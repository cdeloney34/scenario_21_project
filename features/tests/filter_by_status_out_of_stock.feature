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
     # Given  Open main
     # When Log in to the webpage
    #  When Click secondary option at the left side menu page
    #  When Verify the right page open
    #  When Click on filters
     # When Filter the products by want to sell
    #  When Click on Apply filter
    #  Then Verify all cards have for sale tag


    Scenario:User can filter the Secondary deals by “want to buy” option
      Given Open Reely page
      When Log in to page
      When click on secondary page
      Then Verify page opens
      When Click on filters tab
      When Filter the products by want to buy
      When Click on Apply filter tab
      Then Verify all cards have Want to buy tag


      Scenario: Scenario 16: User can filter the Secondary deals by Unit price range
        Given open webpage
        When log into webpage
        When click on secondary webpage
        Then Verify Webpage
        When click on filter tab
        When Filter the products by price range from 1200000 to 2000000 AED
        Then Verify the price in all cards is inside the range (1200000 - 2000000)

      Scenario: Scenario 17: User can open the off plan page and go through the pagination
        Given open page
        When Log in to main page
        When Click on off plan option
        Then Verify off plan page open
        When Go to the final page using the pagination
        When Go back to the first page using the pagination


      Scenario: Scenario 18 User can filter the off plan products by Unit price range
        Given Open Reely
        When Log in to Reely
        When Click on off plan tab
        Then Verify off plan page
        When Filter the products by price range from 1200000 to 2000000 AED.
        Then Verify the price in all cards is inside the range (1200000 - 2000000).


      Scenario: Scenario 19 User can see titles and pictures on each product inside the off plan page
        Given open reely pg
        When log into Reely
        When click off plan tab
        Then verify off plan opens
        Then Verify each product on this page contains a title and picture visible


      Scenario: Scenario 20 User can filter by sale status Out of Stocks
        Given Open reely.io pg
        When Log into Reely pg
        When go to offplan page
        Then Verify offplan page
        When click filters
        When Filter by status of out-of-stock
        Then Verify each product contains the out of stock tab


        Scenario: Scenario 21  User can open product detail and see three options of visualization
          Given open reely.io
          When login to reel.io
          When click on offplan
          When click on the first product
          Then verify the two options of visualizations are architecture, interior
          Then verify the visualization options are clickable
