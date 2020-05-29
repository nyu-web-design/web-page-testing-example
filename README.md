## Example automated testing of web page

This repository shows how to perform automated testing of a web page, including:

- testing the text in the page title
- testing the text in an element
- testing the color of text in an element
- testing the hover behavior of an element
- testing whether a link with given text exists
- testing whether a link with given href exists
- testing the responsive page width at different browser widths

It does so by popping open a web browser, loading the target page, and testing it through browser automation.

## Dependencies

The automated tests in this example are written in Python, and require the following Python modules:

- pytest
- selenium

Additional, to run these tests, you must separately install:

- the [selenium driver](https://sites.google.com/a/chromium.org/chromedriver/downloads) suitable for your local version of Google Chrome
- the location of the selenium driver you download must be added to your system's PATH variable.... instructions for doing this are readily available.
- alternatively, simply place the selenium driver into a directory that is already in your PATH variable.
