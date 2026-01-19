"""
scraper.py
Extracts basic public profile information using requests + BeautifulSoup
"""

import requests
from bs4 import BeautifulSoup


def scrape_profile(profile_url):
    """
    Scrapes basic public information from a social media profile
    Returns a dictionary with extracted data
    """

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    result = {
        "bio_present": False,
        "suspicious": False,
        "reasons": []
    }

    try:
        response = requests.get(profile_url, headers=headers, timeout=10)

        if response.status_code != 200:
            result["suspicious"] = True
            result["reasons"].append("Profile page not accessible")
            return result

        soup = BeautifulSoup(response.text, "html.parser")

        bio_tags = soup.find_all("meta")

        for tag in bio_tags:
            if tag.get("name") == "description":
                content = tag.get("content", "")
                if len(content.strip()) > 0:
                    result["bio_present"] = True

        if not result["bio_present"]:
            result["suspicious"] = True
            result["reasons"].append("Bio missing or empty")

        return result

    except Exception as e:
        result["suspicious"] = True
        result["reasons"].append(f"Error scraping profile: {str(e)}")
        return result
