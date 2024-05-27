# Created by cedri at 4/11/2024
Feature: Add items to Target Cart.
  # Enter feature description here

  Scenario: Very User can add an item to Target Cart
  Given Open Target main webpage.
  When Type basketball into search field.
  When Click on the search button.
  When Click on the add to cart button.
  When Click on second cart button.
  Then Verify item was added to cart.

  Scenario: 'Your cart is empty' is displayed.
    Given Open Target main page
    When Click on Cart icon
    Then Verify'Your cart is empty' message.