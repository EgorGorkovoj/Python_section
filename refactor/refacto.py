import datetime
import logging
from typing import Optional

from bs4 import BeautifulSoup, Tag

logger = logging.getLogger(__name__)


BASE_URL = "https://spimex.com"
HTML = """"""


def parse_links(html: str) -> list[Tag]:
    soup = BeautifulSoup(html, "html.parser")
    links: list[Tag] = soup.find_all(  # type: ignore
        "a", class_="accordeon-inner__item-title link xls"
    )
    return links


def extract_time(href: str) -> datetime.date:

    date_in_href = href.split("oil_xls_")[1][:8]
    file_date: datetime.date = datetime.datetime.strptime(
        date_in_href, "%Y%m%d"
    ).date()
    return file_date


def validate_date_range(
    file_date: datetime.date,
    start_date: datetime.date,
    end_date: datetime.date,
) -> bool:
    if start_date >= file_date >= end_date:
        return False
    return True


def get_links(
    links: list[Tag], start_date: datetime.date, end_date: datetime.date
) -> list[tuple[str, datetime.date]]:

    results = []

    for link in links:
        href: Optional[str] = link.get("href")
        if not href:
            continue

        href = href.split("?")[0]
        if (
            "/upload/reports/oil_xls/oil_xls_" not in href
            or not href.endswith(".xls")
        ):
            continue

        try:
            file_date = extract_time(href=href)
            if validate_date_range(file_date, start_date, end_date):
                u = href if href.startswith("http") else f"{BASE_URL}{href}"
                results.append((u, file_date))
            else:
                logging.info(f"Ссылка {href} вне диапазона дат({file_date})")
        except Exception as e:
            logging.warning(f"Не удалось извлечь дату из ссылки {href}: {e}")
    return results


def main():
    logging.basicConfig(
        level=logging.INFO, format="%(asctime)s %(levelname)s: %(message)s"
    )
    links = parse_links(html=HTML)
    get_links(links=links)


if __name__ == "__main__":
    main()
