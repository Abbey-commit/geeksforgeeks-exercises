Feature: Extract four data series from a CSV file with peculiar Ascombe Quartet format.
    Scenario: When requested, the application extract all four series.
    Given the "data/Ascombe_quartet_data.csv" source file exists
    And the "output" directory exists
    When I run the command "python src/data_acuisition/main.py -o output data/Ascombe'_quartet_data.csv"
    Then the "output/series_1.json" file exists
    And the "output/series_2.json" file exists
    And the "output/series_3.json" file exists
    And the "output/series_4.json" file exists
    And the "quartet/series_1.json" file starts with '{"x": "10.0", "y": "8.04"}'