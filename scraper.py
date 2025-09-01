import requests
from bs4 import BeautifulSoup

def scrape_seo_data(url):
    """
    Scrapes a given URL to extract on-page SEO metrics.

    Args:
        url (str): The URL of the website to scrape.

    Returns:
        dict: A dictionary containing the extracted SEO data.
              Returns None if the request fails.
    """
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()  # Raise an exception for bad status codes
    except requests.RequestException as e:
        print(f"Error fetching the URL: {e}")
        return None

    soup = BeautifulSoup(response.text, 'html.parser')

    # --- Extract SEO Data ---
    
    # 1. Title Tag
    title = soup.find('title').get_text(strip=True) if soup.find('title') else 'No title found'

    # 2. Meta Description
    meta_desc = soup.find('meta', attrs={'name': 'description'})
    meta_description = meta_desc['content'] if meta_desc else 'No meta description found'

    # 3. H1 Header
    h1 = soup.find('h1').get_text(strip=True) if soup.find('h1') else 'No H1 header found'

    # 4. H2 Headers
    h2_tags = [h2.get_text(strip=True) for h2 in soup.find_all('h2')]
    h2_headers_str = ','.join(h2_tags) if h2_tags else 'No H2 headers found'

    # 5. Word Count
    body_text = soup.find('body').get_text(strip=True) if soup.find('body') else ''
    word_count = len(body_text.split())

    seo_data = {
        "url": url,
        "title": title,
        "meta_description": meta_description,
        "h1_header": h1,
        "h2_headers": h2_headers_str,
        "word_count": word_count
    }

    return seo_data
