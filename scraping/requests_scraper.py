"""Module for scraping Google results using HTTP requests."""

from typing import List
import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
from urllib.parse import quote_plus
from utils.logger import get_logger
from utils.config import Config

logger = get_logger(__name__)


class RequestsScraper:
    """Scrapes Google search results using requests and BeautifulSoup."""

    def __init__(self) -> None:
        """Initialize user agent for requests."""
        self.user_agent = UserAgent()

    def search(self, query: str) -> List[str]:
        """
        Performs a search query using requests and parses results.

        Args:
            query (str): Search term.

        Returns:
            List[str]: List of non-ad URLs.
        """
        headers = {"User-Agent": self.user_agent.random}
        search_url = f"https://www.google.com/search?q={quote_plus(query)}"

        try:
            response = requests.get(search_url, headers=headers, timeout=10)
            response.raise_for_status()

            soup = BeautifulSoup(response.text, "html.parser")
            result_divs = soup.select("div.g")

            links = []
            for div in result_divs:
                anchor = div.find("a", href=True)
                href = anchor["href"]
                if "google.com" not in href:
                    links.append(href)

            return links

        except requests.RequestException as error:
            logger.error("Erro ao buscar resultados com requests: %s", error)
            return []
