import re
import requests
from bs4 import BeautifulSoup as Sp
from src import utils
from collections import Counter


class Scrape:
    def __init__(self):
        self.enter = ''
        self.word_list = []
        self.top_words = {}
        self.x = self.top_words.keys()
        self.y = self.top_words.values()

    def check_url(self):
        while True:
            # the url is crosschecked here with regex pattern matching
            self.enter = input("Enter the URL you'd like to scrape here: ")
            regex = re.compile(r'https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+')
            regex_check = re.match(regex, self.enter)
            if regex_check:
                break
            else:
                print("Wrong url format. Please re-enter a correct url format")

        return self.enter

    def scrape_website(self):
        # the website is scrapped with beautifulsoup below
        response = requests.get(self.enter)
        soup = Sp(response.content, 'html.parser')

        # unwanted characters are filtered out with regex pattern matching
        content = soup.find('body').text.strip().replace('\'', ' ')
        reg = re.compile(r'[0-9#)($%&\-~*:/\-\'_=\[\]<.≡>,=+\\©▼!@?▲]*[//]*[>>>]*[:]*')
        filtered_content = re.sub(reg, '', content)
        words = filtered_content.lower().split()
        self.word_list = Counter(words)

        # unwanted words are filtered out here using the util resources as a filter
        for item in utils.common_words:
            if item in self.word_list:
                del self.word_list[item]
        top_words = dict(self.word_list.most_common(7)) # only the 7 top most words are returned here
        return top_words
