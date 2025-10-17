"""Module for scraping Google search results using Selenium."""

from typing import List
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException
from time import sleep
from utils.logger import get_logger
from utils.config import Config

logger = get_logger(__name__)


class SeleniumScraper:
    """Scrapes Google search results using Selenium."""

    def __init__(self) -> None:
        """Initialize Selenium WebDriver with options."""
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--log-level=3")

        try:
            self.driver = webdriver.Chrome(
                service=Service(), options=chrome_options
            )
        except WebDriverException as error:
            logger.error("Erro ao iniciar WebDriver: %s", error)
            raise

    def search(self, query: str) -> List[str]:
        """
        Performs a Google search and extracts non-ad links.

        Args:
            query (str): Search query.

        Returns:
            List[str]: List of result URLs.
        """
        try:
            self.driver.get("https://www.google.com")
            sleep(1)
            search_box = self.driver.find_element(By.NAME, "q")
            search_box.send_keys(query)
            search_box.send_keys(Keys.RETURN)
            sleep(Config.SEARCH_WAIT_TIME)

            results = self.driver.find_elements(By.CSS_SELECTOR, "div.g")
            links = []

            for result in results:
                link_tag = result.find_element(By.TAG_NAME, "a")
                href = link_tag.get_attribute("href")
                if href and "google.com" not in href:
                    links.append(href)

            return links

        except Exception as error:
            logger.error("Erro durante scraping com Selenium: %s", error)
            return []

    def close(self) -> None:
        """Close the WebDriver session."""
        self.driver.quit()
