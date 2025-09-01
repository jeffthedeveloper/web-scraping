# SEO Web Scraper API

This project is a Python-based web scraping tool built with Flask and BeautifulSoup, designed to analyze the on-page SEO metrics of any given website.

The application exposes a simple REST API endpoint that receives a URL, scrapes it to extract key SEO information—such as titles, meta descriptions, headings (H1, H2), and keyword density—and saves the analysis into a database.

This tool serves as a practical example of how web scraping can be leveraged to gather actionable data for optimizing organic traffic and search engine performance, a core challenge in the digital marketing and content creation space.

## Features

-   **RESTful API**: Simple endpoint to trigger SEO analysis.
-   **On-Page SEO Scraping**: Extracts crucial SEO elements:
    -   Page Title (`<title>`)
    -   Meta Description (`<meta name="description">`)
    -   H1 and H2 headings
    -   Word count and basic keyword analysis
-   **Data Persistence**: Saves scraped data into a SQLite database for future reference.
-   **Scalable Structure**: Built with Flask, allowing for easy expansion with new features or integrations.

## Tech Stack

-   **Backend**: Flask, Python
-   **Scraping**: BeautifulSoup, Requests
-   **Database**: SQLite, SQLAlchemy

## How to Use

1.  **Clone the repository and install dependencies:**
    ```bash
    git clone https://github.com/jeffthedeveloper/web-scraping
    cd web-scraping
    pip install -r requirements.txt
    ```

2.  **Run the Flask application:**
    ```bash
    python app.py
    ```
    This will initialize the database and start the server.

3.  **Send a POST request to the `/scrape` endpoint:**
    Use a tool like Postman, Insomnia, or a simple `curl` command to send a URL to be analyzed.

    ```bash
    curl -X POST -H "Content-Type: application/json" -d '{"url": "https://www.example.com"}' http://127.0.0.1:5000/scrape
    ```

4.  **Check the results:**
    The API will return a JSON object with the scraped SEO data. You can also use the `/results` endpoint to view all historical analyses stored in the database.

    ```bash
    curl http://127.0.0.1:5000/results
    ```
