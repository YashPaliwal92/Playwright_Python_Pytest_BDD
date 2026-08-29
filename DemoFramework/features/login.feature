Feature: Validate login scenarios

  Scenario: Verify user is able to login with valid credentials
    Given a valid user logs in
    Then user should login successfully

  Scenario: Verify locked user is not allowed to login
    Given a locked user tries to login
    Then locked user should not be allowed to login

  Scenario: Verify invalid user is not allowed to login
    Given an invalid user tries to login
    Then invalid user should not be allowed to login

