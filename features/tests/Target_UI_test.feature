Feature: Verify UI elements on Target Help page

  Scenario: User verifies UI elements on Target Help page

    Given the user opens the Target Help page

    Then Verify the following UI elements should be present:

       |Element Name         | Element Type    |
       |  Target Help        |  text           |
       |  Search Box         |  input          |
       |  Search button      |  button         |
       |  help Section       |  button         |
       |  browse all Help pages|   text           |