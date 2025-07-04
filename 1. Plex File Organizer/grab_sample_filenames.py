from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import website_ignore as website


def grab_sample_filenames():
    """Return 50 samples each of movie & tv show file names."""
    driver = webdriver.Chrome()

    # Get Page Links
    driver.get(website.movies())

    page_list_elements = driver.find_elements(
        By.XPATH,
        "//div[@class='pagination']//ul//li//a"
    )

    page_links = [i.get_attribute('href') for i in page_list_elements][:-2]

    # Loop Through Web Pages
    movie_links = []

    for page in page_links:
        driver.get(page)

        # Get Movies Links
        movies_elements = driver.find_elements(
            By.XPATH,
            # "//th[@class='coll-1 name']"
            "//div[@class='featured-list']//div//table//tbody//tr//td//a[2]"
        )

        for movie_element in movies_elements:
            href = movie_element.get_attribute('href')
            movie_links.append(href)

    # movies_hrefs = [i.get_attribute('href') for i in movies_elements]

    [print(i) for i in movie_links]



    input("\nPress Any Key to Close\n\n")
    driver.close()


if __name__ == "__main__":
    grab_sample_filenames()
