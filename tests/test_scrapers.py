"""Unit tests for scraping modules."""

from scraping.selenium_scraper import SeleniumScraper
from scraping.requests_scraper import RequestsScraper


def test_selenium_scraper() -> None:
    """Test Selenium scraper returns results."""
    scraper = SeleniumScraper()
    results = scraper.search("OpenAI")
    scraper.close()
    assert isinstance(results, list)
    assert results, "Selenium scraper retornou lista vazia."


def test_requests_scraper() -> None:
    """Test requests scraper returns results."""
    scraper = RequestsScraper()
    results = scraper.search("OpenAI")
    assert isinstance(results, list)
    assert results, "Requests scraper retornou lista vazia."
