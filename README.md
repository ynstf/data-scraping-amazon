# Data Scraping Amazon
 Python script that scrapes data from Amazon product pages and saves the information into a CSV file. The script uses the BeautifulSoup library for web scraping and the os module for file operations and extracts product titles, prices, page URLs, and image URLs.

Here's a brief overview of what the script does:

 1.   It first retrieves a list of files in the "the pages" directory.
 1.   It then iterates through the HTML pages found in that directory.
 1.   For each page, it uses BeautifulSoup to parse the HTML content.
 1.   It extracts product information such as title, price, page URL, and image URL from the parsed HTML.
 1.   The script then formats this information and saves it to a CSV file called "produits.csv."
