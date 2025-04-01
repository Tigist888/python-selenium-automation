
  Feature: User Login

  Scenario: Successful login to Target website

         Given open target main page
         When Click Sign In
         And From side navigation, click sign in
         And Input email and password on SignIn page
         And Click Sign In
         Then Verify login success
