import scrapy


class DEWiktionarySpider(scrapy.Spider):
    name = 'de'

    allowed_domains = ['de.wiktionary.org'
                       ]

    start_urls = [
        'https://de.wiktionary.org/wiki/Kategorie:Substantiv_m_(Franz%C3%B6sisch)', # FR in DE
        'https://de.wiktionary.org/wiki/Kategorie:Substantiv_f_(Franz%C3%B6sisch)',

        'https://de.wiktionary.org/wiki/Kategorie:Substantiv_f_(Deutsch)', # DE in DE
        'https://de.wiktionary.org/wiki/Kategorie:Substantiv_m_(Deutsch)',
        'https://de.wiktionary.org/wiki/Kategorie:Substantiv_n_(Deutsch)',
        'https://de.wiktionary.org/wiki/Kategorie:Substantiv_zwei_Genera_(Deutsch)',
        'https://de.wiktionary.org/wiki/Kategorie:Substantiv_drei_Genera_(Deutsch)',

        'https://de.wiktionary.org/wiki/Kategorie:Substantiv_f_(Spanisch)', # ES in DE
        'https://de.wiktionary.org/wiki/Kategorie:Substantiv_m_(Spanisch)',
    ]

    def parse(self, response):

        links = response.xpath("//div[@class='mw-category-group']/ul/li/a/@href").extract()
        for link in links:
            yield response.follow(url=link, callback=self.parse_link)


        next_page = response.xpath(f"//div[@id='mw-pages']/a[text()='nächste Seite']/@href").get()
        if next_page:
            yield response.follow(next_page, callback=self.parse)

    def parse_link(self, response):
        d = {'Französisch': 'fr', 'Spanisch': 'es', 'Deutsch': 'de'}
        noun = response.xpath("//span[@class='mw-page-title-main']/text()").get()
        h2_tags = response.xpath("//h2[{}]".format(" or ".join("span[contains(@id, '({})')]".format(lang) for lang in d)))
        for h2 in h2_tags:
            language = h2.xpath(".//a[contains(@title, 'Wiktionary')]/text()").get()
            lang = d[language]
            common_noun = h2.xpath("following-sibling::h3[span[starts-with(@id, 'Substantiv')]] | following-sibling::h4[span[starts-with(@id, 'Substantiv')]]")
            gen = common_noun.xpath(".//em/text()").getall()
            if gen and noun:
                gender = list(set(gen))
                yield {
                    'noun': noun,
                    'gender': gender,
                    'lang': lang,
                }