# Issuu Scraper (Python)

Basic Issuu scraper, and since I'm not an expert at Python, this is a simple script and nothing advanced or special. It still does the trick though. :) Enter the url, and then enter the number of pages the book has. The program will then do the rest by downloading each image, compiling into a pdf, and outputting the urls and information in separate text files.

## Usage

    python3 ./issuu.py
  
The script will prompt you to enter Issuu item's URL and page count.

## Requirements

This script requires Python 3, and the packages urllib, Beautiful Soup, and wget. To install the required packages:
   
    pip install urllib3 beautifulsoup4 wget

## Credits

This script was inspired and is based on the Ruby script from pietrop: https://github.com/pietrop/issuu.com-downloader as well as dkl3's original python script: https://github.com/dkl3/py-issuu-scrape
