"""
An experiment showing how to automate testing of web page development in HTML & CSS.
Selenium webdriver for Chrome (a.k.a. the file named chromedriver) must be installed in either:
- in the same directory as chrome.exe on Windows (e.g. C:\Program Files\Google\Chrome\Application)
- in a directory that is included in the PATH on Mac OS X (e.g. /usr/local/bin)
"""
import pytest
import json
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

class Tests:

  @pytest.fixture(scope="class")
  def site_settings(self):
    """
    Make the site settings indicated in settings.json available to the tests.
    """
    settings = json.load(open('./settings.json', 'r'))
    yield settings

  @pytest.fixture(scope="class")
  def web_driver(self):
    """
    Pop open a Chrome web browser and make it available to the tests.
    """
    settings = json.load(open('./settings.json', 'r'))
    print(settings["site_url"])

    # set up the fixture
    driver = webdriver.Chrome()
    driver.get(settings["site_url"]) # load the site from the settings file
    # provide the fixture value
    yield driver  
    # now tear it down
    driver.close()

  def test_title_text(self, web_driver, site_settings):
    """
    Example of checking the page title for the correct text.
    In this case, we compare the title to the student's name in the settings file.
    """
    assert site_settings["name"] in web_driver.title

  def test_element_text(self, web_driver, site_settings):
    """
    Example of checking an element for the correct text.
    In this case, we compare the h1 elemeent to the student's name in the settings file.
    """
    target_element = "h1" # check the h1 tag
    expected_value = site_settings["name"] # pull the student's name from the settings
    elem = web_driver.find_element_by_tag_name(target_element) # find the h1 tag
    assert expected_value in elem.text # see if the student's name is in it

  def test_element_color(self, web_driver):
    """
    Example of checking an element's text color.
    In this case, we check the p.first-paragraph's color.
    """
    target_element = "p.first-paragraph"
    expected_value = 'rgba(0, 128, 0, 1)' #greem!
    elem = web_driver.find_element_by_css_selector(target_element)
    assert elem.value_of_css_property('color') == expected_value

  def test_hover_behavior(self, web_driver):
    """
    Example of checking an element's behavior on hover.
    In this case, we check that the p.second-paragraph's font changes on hover.
    """
    elem = web_driver.find_element_by_css_selector("p.second-paragraph")
    ActionChains(web_driver).move_to_element(elem).pause(0).perform()  # move cursor there
    font_family = elem.value_of_css_property('font-family').lower()
    assert font_family.startswith('helvetica') #helvetica!

  def test_link_text_exists(self, web_driver):
    """
    Example of checking a link's text.
    In this case, we check that a link with the text 'knowledge' exists somewhere on the page.
    """
    search_term = 'knowledge' # look for a link with this text in it
    elem = web_driver.find_element_by_partial_link_text(search_term)
    assert elem # check that a matching element exists

  def test_link_href_exists(self, web_driver):
    """
    Example of checking a link's href target URL
    In this case, we check that a link with the href 'https://knowledge.kitchen' exists somewhere on the page.
    """
    target_url = "https://knowledge.kitchen"
    elem = web_driver.find_element_by_xpath('//a[@href="' + target_url + '"]')
    assert elem # check that it exists

  def test_mobile_width(self, web_driver):
    """
    Example of checking the width of a page at mobile browser width.
    In this case, we check the .container width is less than the browser width at 500px.
    """
    target_element = '.container'
    browser_width = 500 # we'll set the browser to this width
    max_acceptable_width = 500 # container can't be wider than this
    min_acceptable_width = 0 # container can't be narrower than this
    web_driver.set_window_size(browser_width, 800)
    elem = web_driver.find_element_by_css_selector(target_element)
    # check that the h1 element is appropriate for mobile
    assert max_acceptable_width > elem.size["width"] > min_acceptable_width

  def test_desktop_width(self, web_driver):
    """
    Example of checking the width of a page at mobile browser width.
    In this case, we check the .container width is less than the browser width at 500px.
    """
    target_element = '.container'
    browser_width = 1200
    max_acceptable_width = 1200 # container can't be wider than this
    min_acceptable_width = 500 # container can't be narrower than this
    web_driver.set_window_size(browser_width, 800)
    elem = web_driver.find_element_by_css_selector(target_element)
    # check that the h1 element is appropriate for mobile
    assert max_acceptable_width > elem.size["width"] > min_acceptable_width

  def test_max_width(self, web_driver):
    """
    Example of checking the width of a page at mobile browser width.
    In this case, we check the .container width is less than the browser width at 500px.
    """
    target_element = '.container'
    browser_width = 2000 # a very wide browser
    max_acceptable_width = 1200 # the max container width we will accept
    web_driver.set_window_size(browser_width, 800)
    elem = web_driver.find_element_by_css_selector(target_element)
    # check that the h1 element is appropriate for mobile
    assert max_acceptable_width >= elem.size["width"]

