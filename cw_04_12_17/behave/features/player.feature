# Created by zarina at 04.12.17

Feature: Class Player
  # Enter feature description here

  Scenario: New Player
    Given new player
    Then it should have name
    And it should have hp
