  Scenario: user can add  any Target's product into cart

      Given Open target main page
      When Search for camera
      And Click on Add to cart
      And Click on Add to cart from side navigation
      And open the cart page
      Then verify cart has one item
