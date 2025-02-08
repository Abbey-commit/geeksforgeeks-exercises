Feature: Acquire data from Kaggle API

  Scenario: Download Anscombe's quartet dataset from Kaggle
    Given proper keys are in "kaggle.json"
    When we run the kaggle download command
    Then log has INFO line with "Dataset download to"