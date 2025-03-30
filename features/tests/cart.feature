
Feature:  cart tests

   Scenario: Display empty cart message when the cart is empty
     Given the user opens the Target main page
     When the user clicks on the cart icon
     Then the message "Your cart is empty" should be displayed