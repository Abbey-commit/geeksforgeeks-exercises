Feature: Scrape data from a web page

  Scenario: Scrape data from Anscombe's quartet table
    Given an HTML page "example_1.html"
    """
    <!DOCTYPE html>
    <html>
    <body>
    <table>
        <caption>Anscombe's quartet</caption>
        <tr><td>10.0</td><td>8.04</td></tr>
        <tr><td>8.0</td><td>6.95</td></tr>
    </table>
    </body>
    </html>
    """

    When we run the html extract command
    Then log has INFO line with "header: ['10.0', '8.04']"
    And log has INFO line with "count: 1"