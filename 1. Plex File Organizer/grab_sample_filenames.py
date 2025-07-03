from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import website_ignore as website


def grab_sample_filenames():
    """Return 50 samples each of movie & tv show file names."""
    driver = webdriver.Chrome()
    driver.get(website.root())
    input("Press Any Key to Close")
    driver.close()


if __name__ == "__main__":
    grab_sample_filenames()
