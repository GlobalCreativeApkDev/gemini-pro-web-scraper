"""
This file contains code for the application "Gemini Pro Web Scraper".
Author: GlobalCreativeApkDev

The code in this file is inspired by the following source.
https://oxylabs.io/blog/chatgpt-web-scraping
"""


# Importing necessary libraries
import google.generativeai as gemini
import os
from dotenv import load_dotenv
from mpmath import mp, mpf

mp.pretty = True


# Creating static functions to be used in this application.


def is_number(string: str) -> bool:
    try:
        mpf(string)
        return True
    except ValueError:
        return False


def list_to_words(a_list: list) -> str:
    if len(a_list) == 0:
        return ""
    elif len(a_list) == 1:
        return str(a_list[0])
    elif len(a_list) == 2:
        return str(a_list[0]) + " and " + str(a_list[1])
    else:
        return ", ".join(a_list[:-1]) + ", and " + a_list[-1]


# Creating main function used to run the application.


def main() -> int:
    """
    This main function is used to run the application.
    :return: an integer
    """

    load_dotenv()
    gemini.configure(api_key=os.environ['GEMINI_API_KEY'])

    # Asking user input values for generation config
    temperature: str = input("Please enter temperature (0 - 1): ")
    while not is_number(temperature) or float(temperature) < 0 or float(temperature) > 1:
        temperature = input("Sorry, invalid input! Please re-enter temperature (0 - 1): ")

    float_temperature: float = float(temperature)

    top_p: str = input("Please enter Top P (0 - 1): ")
    while not is_number(top_p) or float(top_p) < 0 or float(top_p) > 1:
        top_p = input("Sorry, invalid input! Please re-enter Top P (0 - 1): ")

    float_top_p: float = float(top_p)

    top_k: str = input("Please enter Top K (at least 1): ")
    while not is_number(top_k) or int(top_k) < 1:
        top_k = input("Sorry, invalid input! Please re-enter Top K (at least 1): ")

    float_top_k: int = int(top_k)

    max_output_tokens: str = input("Please enter maximum input tokens (at least 1): ")
    while not is_number(max_output_tokens) or int(max_output_tokens) < 1:
        max_output_tokens = input("Sorry, invalid input! Please re-enter maximum input tokens (at least 1): ")

    int_max_output_tokens: int = int(max_output_tokens)

    # Set up the model
    generation_config = {
        "temperature": float_temperature,
        "top_p": float_top_p,
        "top_k": float_top_k,
        "max_output_tokens": int_max_output_tokens,
    }

    safety_settings = [
        {
            "category": "HARM_CATEGORY_HARASSMENT",
            "threshold": "BLOCK_MEDIUM_AND_ABOVE"
        },
        {
            "category": "HARM_CATEGORY_HATE_SPEECH",
            "threshold": "BLOCK_MEDIUM_AND_ABOVE"
        },
        {
            "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
            "threshold": "BLOCK_MEDIUM_AND_ABOVE"
        },
        {
            "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
            "threshold": "BLOCK_MEDIUM_AND_ABOVE"
        },
    ]

    model = gemini.GenerativeModel(model_name="gemini-pro",
                                  generation_config=generation_config,
                                  safety_settings=safety_settings)

    convo = model.start_chat(history=[
    ])

    while True:
        url: str = input("Please enter the URL of the website you want to scrape: ")
        contents: str = input("What does the URL contain: ")
        elements: list = []  # initial value
        selectors: list = []  # initial value
        element_plurals: list = []  # initial value
        num_elements: str = input("How many elements do you want to scrape (at least 1)? ")
        while not is_number(num_elements) or int(num_elements) < 1:
            num_elements = input("Sorry, invalid input! How many elements do you want to scrape (at least 1)? ")

        for i in range(int(num_elements)):
            element: str = input("Name the element you want to scrape: ")
            selector: str = input("What is the CSS selector of the element " + str(element) + "? ")
            elements.append(element)
            selectors.append(selector)
            convo.send_message("What is the plural of \"" + str(element)
                               + "\" (one word response only, no punctuation)?")
            element_plurals.append(str(convo.last.text))

        prompt: str = """
Write a web scraper using Python and BeautifulSoup (please include code only in your response)!

Sample Target: """ + str(url) + """
Rationale: Scrape the """ + str(list_to_words(element_plurals)) + """ of all the """ + str(contents) + """ on the target page.

CSS selectors are as follows:
"""

        for i in range(len(elements)):
            prompt += """
""" + str(i + 1) + """. """ + str(elements[i]) + """: """ + str(selectors[i]) + """
"""

        prompt += """
Output: Save all the """ + str(list_to_words(element_plurals)) + """ of all the """ + str(contents) + """ in a CSV file.
Place the CSV file inside "csvs" directory. Include the """ + str(list_to_words(element_plurals)) + """ as the headers of
the table in the CSV file.

Additional Instructions: Handle character encoding and only include the code in your response.
"""

        convo = model.start_chat(history=[
        ])
        print("Prompt:\n" + str(prompt))
        convo.send_message(prompt)
        code: str = '\n'.join(str(convo.last.text).split('\n')[1:-1])
        file_name: str = input("Please enter the name of the file you want the code to be in (no extension please): ")

        # Writing the code to a file
        code_file = open(os.path.join("scrapers", str(file_name) + ".py"), "w")
        code_file.write(code)
        code_file.close()

        # Executing the dynamically generated file.
        os.system("python3 " + str(os.path.join("scrapers", str(file_name) + ".py")))

        print("Enter 'Y' for yes.")
        print("Enter anything else for no.")
        continue_scraping: str = input("Do you want to continue scraping a website? ")
        if continue_scraping != "Y":
            return 0


if __name__ == '__main__':
    main()
