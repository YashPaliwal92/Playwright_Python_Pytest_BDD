Feature: Shopping

  Background: Valid user logins
    Given a valid user logs in

  Scenario: Verify user is able to successfully buy an item
    When user selects the product 'Sauce Labs Backpack'
    Then product should be added to cart
    When user fills following details to checkout
     | Name | Last Name | Zip |
     | John | Doe       | 123 |
    Then user reviews the product detail
    When user finishes checking out
    Then user should successfully buy the product

  Scenario: Verify user can remove item from cart
    When user selects the product 'Sauce Labs Backpack'
    Then product should be added to cart
    When user removes the product from cart
    Then product should be removed

