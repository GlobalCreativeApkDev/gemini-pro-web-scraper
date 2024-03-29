# gemini-pro-web-scraper

Ever wondered about scraping a website without running a single line of code? Well, **Gemini Pro Web Scraper** is the
tool to do so. This tool automatically scrapes the data you want from a website of your choice.

# Source Code

The source code of the application **Gemini Pro Web Scraper** is available in 
[Source Code](https://github.com/GlobalCreativeApkDev/gemini-pro-web-scraper/blob/master/main.py).

# Installation

```
pip install gemini-pro-web-scraper
```

# How to Use the Application?

Pre-requisites:
1. [Python](https://www.python.org/downloads/) installed in your device.
2. .env file in the same directory as <GEMINI_PRO_WEB_SCRAPER_DIRECTORY> and has the value of GEMINI_API_KEY.

First, open a Terminal or Command Prompt window and run the following command.

```
cd <GEMINI_PRO_WEB_SCRAPER_DIRECTORY>
python3 main.py
```

**Note:** Replace <GEMINI_PRO_WEB_SCRAPER_DIRECTORY> with the path to the directory of the application 
**Gemini Pro Web Scraper**.

Then, the application will start with something looking like in the screenshot below.

![Application](images/Application.png)

You will then be asked to input the following values.

1. Temperature - between 0 and 1 inclusive
2. Top P - between 0 and 1 inclusive
3. Top K - at least 1
4. Max output tokens - at least 1

The following screenshot shows what is displayed after inputting the mentioned values.

![Web Scraper](images/Web%20Scraper.png)

You will be required to input the following pieces of information.

1. The URL of the website you want to scrape (e.g., https://sandbox.oxylabs.io/products).
2. What the URL entered in step 1 contains (e.g., **games** for https://sandbox.oxylabs.io/products).
3. The number of elements you want to scrape.
4. The details of each element you want to scrape (i.e., the name and the corresponding CSS selector for each element).
5. The name of the file you want the code to be in (without the extension).

Once you enter the values mentioned above, the file containing the code will be created inside "scrapers" directory.
Moreover, the CSV file containing the scraped data will be generated inside "csvs" directory. Then, you will be asked 
whether you still want to continue unit testing or not. If you enter 'Y', you will be redirected to an application 
window like in screenshot above. Else, you will exit the application.

![Continue Scraping](images/Continue%20Scraping.png)

The Python file generated which contains the web scraping code looks like below.

![Web Scraper Code](images/Web%20Scraper%20Code.png)

Below is how the generated CSV file looks like.

![CSV File](images/CSV%20File.png)
