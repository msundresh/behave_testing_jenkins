# Created by msundresh at 2/12/2019
Feature: login
  # login to the application to test python framewrok

  @GLSWW-1603
  Scenario: login
    Given I navigate to the URL
    When I login to the application
    Then the application should enter accounts page
