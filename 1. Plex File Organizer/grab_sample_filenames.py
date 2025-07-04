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

    # Get Page Links
    page_links = get_page_links(driver, website.movies())

    # Loop Through Web Pages & Get Links
    movie_links = []
    for page in page_links:
        driver.get(page)

        # Grab Movie Links
        movies_elements = driver.find_elements(
            By.XPATH,
            # "//th[@class='coll-1 name']"
            "//div[@class='featured-list']//div//table//tbody//tr//td//a[2]"
        )

        for movie_element in movies_elements:
            href = movie_element.get_attribute('href')
            movie_links.append(href)

    # Loop through each Movie Links & get the Sample File Names.
    for movie_link in movie_links:
        driver.get(movie_link)

        file_tab_element = driver.find_element(
            By.XPATH,
            "//div[@class='tab-nav clearfix']//ul//li[2]"
        )

        # Extract File Name
        file_tab_element.click()


    input("\nPress Any Key to Close\n\n")
    driver.close()


def get_page_links(driver: webdriver, link: str) -> list:
    """Return the pages web links on a given link."""
    driver.get(link)

    page_list_elements = driver.find_elements(
        By.XPATH,
        "//div[@class='pagination']//ul//li//a"
    )

    page_links = [i.get_attribute('href') for i in page_list_elements][:-2]

    if TEST_MODE:
        page_links = page_links[:1]

    return page_links



if __name__ == "__main__":
    grab_sample_filenames()
