""" July 4, 2025
DEV NOTE
This script is a special case script. It's not supposed to be
reused on other systems or for any other. This script can and will
break in the near future due to the nature of it relying on
selenium and the front end of a website entirely.
"""


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import website_ignore as website


TEST_MODE = True


def grab_sample_filenames():
    """Return 50 samples each of movie & tv show file names."""
    driver = webdriver.Chrome()

    # Get the Movie's page links.
    page_links = get_page_links(driver, website.movies())

    # Grab each of the movie's item links.
    movie_links = grab_item_links(driver, page_links)

    # Loop through each Movie Links & get the Sample File Names.
    for movie_link in movie_links:
        driver.get(movie_link)

        # Navigate to the Files information.
        file_tab_element = driver.find_element(
            By.XPATH,
            "//div[@class='torrent-tabs']//ul//li[2]//a"
        )

        file_tab_element.click()


    input("\nPress Any Key to Close\n\n")
    driver.close()


def get_page_links(driver: webdriver, page: str) -> list:
    """Return the pages web links on a given link."""
    driver.get(page)

    # Grab the element containing the pages.
    page_list_elements = driver.find_elements(
        By.XPATH,
        "//div[@class='pagination']//ul//li//a"
    )

    # Extract the hrefs.
    page_links = [i.get_attribute('href') for i in page_list_elements][:-2]

    if TEST_MODE:
        page_links = page_links[:1]

    return page_links


def grab_item_links(driver: webdriver, page_links: list) -> list:
    """Return the list of the item's links from a given page."""
    links = []

    # Loop through each pages.
    for page in page_links:
        if driver.current_url != page:
            driver.get(page)

        # Grab Each Item
        item_elements = driver.find_elements(
            By.XPATH,
            "//div[@class='featured-list']//div//table//tbody//tr//td//a[2]"
        )

        for item_element in item_elements:
            href = item_element.get_attribute('href')
            links.append(href)

    if TEST_MODE:
        links = links[:1]

    return links


if __name__ == "__main__":
    grab_sample_filenames()
