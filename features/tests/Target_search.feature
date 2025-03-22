Feature: Target search test cases


  Scenario: user can search for a product on Target

      Given Open target main page
      When click on cart icon
      Then verify your "cart is empty message" is shown


  Scenario: user can search for a product on Target

      Given open target main page
      When click sign in
      And From right side navigation menu,click sign in
      Then verify sign in form opened


   Scenario: user can verify at least 10 benefit cells on the Target Circle page

      Given open the Target Circle page
      Then verify there are at least 10 benefit cells



  Scenario: user can add  any Target's product into cart

      Given Open target main page
      When Search for camera
      And Click on Add to cart
      And Click on Add to cart from side navigation
      And open the cart page
      Then verify cart has one item



