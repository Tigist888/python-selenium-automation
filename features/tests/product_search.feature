 Feature: Test Scenarios for Search functionality

  Scenario: User can search for a productGiven Open Google page
    Given Open target main page
    When Input Car into search field
    And Click on search icon
    Then Product results for Car are shown

 Feature: Cart tests

   Scenario: 'Your cart is empty' message is shown for empty cart
     Given Open target main page
     When Click on Cart icon
     Then Verify 'Your cart is empty' message is shown