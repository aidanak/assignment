# -*- coding: utf-8 -*-
from scrapy.exceptions import CloseSpider
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor


class WordSearcherSpider(CrawlSpider):
    name = 'word_searcher'
    allowed_domains = ['www.amazon.com']
    start_urls = ['https://www.amazon.com/']
    searched_words = ["Virtue", "signalling", "is", "society", "version",
                      "of", "Proof", "Stake"]
    found_words = []
    rules = [
        Rule(LinkExtractor(allow=()),
             callback='detail', follow=True)
    ]

    def detail(self, response):
        for word in self.searched_words:
            if word.lower() in self.found_words:
                continue
            if word.lower() in str(response.body):
                print("Found word {0} at url {1}".format(word.lower(),
                      response.url))
                self.found_words.append(word.lower())

        if len(self.found_words) == len(self.searched_words):
            raise CloseSpider('Found all words')


