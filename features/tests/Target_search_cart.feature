Feature: Target search test cases


  Scenario: user can search for a product on Target

      Given Open target main page
      When click on cart icon
      Then verify your "cart is empty message" is shown


  Scenario: user can search for a product on Target

      Given Open target main page
      When click sign in
      And From right side navigation menu,click sign in
      Then verify sign in form opened