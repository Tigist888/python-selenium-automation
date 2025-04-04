Feature: user can open and close terms and condition


  Scenario: User can open and close Terms and Conditions from sign in page


   Given Open sign in page
   And Store original window
   When click on Target terms and conditions link
   And Switch to the newly opened window
   Then Verify Terms and Conditions page is opened
   And User can close new window
   And return to original window