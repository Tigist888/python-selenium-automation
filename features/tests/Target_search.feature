Feature: Target search test cases

#
   Scenario: User can search for a tea on Target
    Given Open target main page
    When Search for tea
    Then Verify correct search results shown for tea
     And verify tea in URL



   Scenario: user can verify at least 10 benefit cells on the Target Circle page

      Given open the Target Circle page
      Then verify there are at least 10 benefit cells






