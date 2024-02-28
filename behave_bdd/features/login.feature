@login_test
Feature: Debug feature

  Background:
    Given browser is opened

  Scenario: Successfull login
    When I go on page "https://lb11.mojosells.com/login/"
    And fill "g.torosyan@g-sg.net" in field "Email"
    And fill "password1" in field "Password"
    And click "Submit"
    Then I should be logged in

  Scenario: Unsuccessfull login
    When I go on page "https://lb11.mojosells.com/login/"
    And fill "g.torosyan@g-sg.net" in field "Email"
    And fill "invalid_password" in field "Password"
    And click "Submit"
    Then "Invalid login/password" should be displayed