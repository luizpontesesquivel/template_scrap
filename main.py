"""Main entry point to run scrapers."""

from scraping.selenium_scraper import SeleniumScraper
from scraping.requests_scraper import RequestsScraper
from utils.logger import get_logger

logger = get_logger(__name__)


def run_selenium() -> None:
    """Run Selenium-based scraping."""
    logger.info("Executando scraping com Selenium...")
    scraper = SeleniumScraper()
    results = scraper.search("OpenAI")
    scraper.close()
    for url in results:
        print(f"Selenium: {url}")


def run_requests() -> None:
    """Run requests-based scraping."""
    logger.info("Executando scraping com requests...")
    scraper = RequestsScraper()
    results = scraper.search("OpenAI")
    for url in results:
        print(f"Requests: {url}")


if __name__ == "__main__":
    run_selenium()
    run_requests()
