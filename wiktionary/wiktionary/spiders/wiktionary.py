import scrapy



class WiktionarySpider(scrapy.Spider):
    name = 'wiktionary'

    allowed_domains = ['fr.wiktionary.org',
                       'de.wiktionary.org',
                       'pl.wiktionary.org',
                       'es.wiktionary.org',
                       'en.wiktionary.org'
                       ]

    start_urls = [
        'https://fr.wiktionary.org/wiki/Cat%C3%A9gorie:Mots_parfois_f%C3%A9minins_ou_masculins_en_fran%C3%A7ais', # FR in FR
        'https://fr.wiktionary.org/wiki/Cat%C3%A9gorie:Noms_multigenres_en_fran%C3%A7ais',
        'https://fr.wiktionary.org/wiki/Cat%C3%A9gorie:Mots_parfois_masculins_ou_f%C3%A9minins_en_fran%C3%A7ais',

        'https://en.wiktionary.org/wiki/Category:French_feminine_nouns', # FR in EN
        'https://en.wiktionary.org/wiki/Category:French_masculine_nouns',
        'https://en.wiktionary.org/wiki/Category:French_nouns_with_multiple_genders',
        'https://en.wiktionary.org/wiki/Category:French_masculine_and_feminine_nouns_by_sense',

        'https://de.wiktionary.org/wiki/Kategorie:Substantiv_m_(Franz%C3%B6sisch)', # FR in DE
        'https://de.wiktionary.org/wiki/Kategorie:Substantiv_f_(Franz%C3%B6sisch)',

        'https://es.wiktionary.org/wiki/Categor%C3%ADa:FR:Sustantivos_femeninos', # FR in ES
        'https://es.wiktionary.org/wiki/Categor%C3%ADa:FR:Sustantivos_masculinos',

        'https://pl.wiktionary.org/wiki/Kategoria:J%C4%99zyk_francuski_-_rzeczowniki_rodzaju_m%C4%99skiego', # FR in PL
        'https://pl.wiktionary.org/wiki/Kategoria:J%C4%99zyk_francuski_-_rzeczowniki_rodzaju_%C5%BCe%C5%84skiego',

        'https://de.wiktionary.org/wiki/Kategorie:Substantiv_f_(Deutsch)', # DE in DE
        'https://de.wiktionary.org/wiki/Kategorie:Substantiv_m_(Deutsch)',
        'https://de.wiktionary.org/wiki/Kategorie:Substantiv_n_(Deutsch)',
        'https://de.wiktionary.org/wiki/Kategorie:Substantiv_zwei_Genera_(Deutsch)',
        'https://de.wiktionary.org/wiki/Kategorie:Substantiv_drei_Genera_(Deutsch)',

        'https://en.wiktionary.org/wiki/Category:German_feminine_nouns', # DE in EN
        'https://en.wiktionary.org/wiki/Category:German_masculine_nouns',
        'https://en.wiktionary.org/wiki/Category:German_neuter_nouns',
        'https://en.wiktionary.org/wiki/Category:German_nouns_with_multiple_genders',

        'https://fr.wiktionary.org/wiki/Cat%C3%A9gorie:Noms_communs_f%C3%A9minins_en_allemand_au_pluriel_en_-e', # DE in FR
        'https://fr.wiktionary.org/wiki/Cat%C3%A9gorie:Noms_communs_f%C3%A9minins_en_allemand_au_pluriel_en_-en',
        'https://fr.wiktionary.org/wiki/Cat%C3%A9gorie:Noms_communs_f%C3%A9minins_en_allemand_au_pluriel_en_-innen',
        'https://fr.wiktionary.org/wiki/Cat%C3%A9gorie:Noms_communs_f%C3%A9minins_en_allemand_au_pluriel_en_-s',
        'https://fr.wiktionary.org/wiki/Cat%C3%A9gorie:Noms_communs_masculins_en_allemand_en_-el_dont_le_g%C3%A9nitif_singulier_donne_-els_et_le_datif_pluriel_-eln',
        'https://fr.wiktionary.org/wiki/Cat%C3%A9gorie:Noms_communs_masculins_en_allemand_en_-er_dont_le_g%C3%A9nitif_singulier_donne_-ers_et_le_datif_pluriel_-ern',
        'https://fr.wiktionary.org/wiki/Cat%C3%A9gorie:Noms_communs_masculins_faibles_en_allemand_ne_se_terminant_pas_par_-e_ou_-r',
        'https://fr.wiktionary.org/wiki/Cat%C3%A9gorie:Noms_multigenres_en_allemand',
        'https://fr.wiktionary.org/wiki/Cat%C3%A9gorie:Noms_communs_neutres_en_allemand_au_g%C3%A9nitif_en_-isses_et_au_pluriel_en_-isse',
        'https://fr.wiktionary.org/wiki/Cat%C3%A9gorie:Noms_communs_neutres_en_allemand_au_g%C3%A9nitif_en_-s_et_au_pluriel_en_-en',
        'https://fr.wiktionary.org/wiki/Cat%C3%A9gorie:Noms_communs_neutres_en_allemand_au_g%C3%A9nitif_en_-s_et_au_pluriel_en_-s',

        'https://es.wiktionary.org/wiki/Categor%C3%ADa:DE:Sustantivos_femeninos', # DE in ES
        'https://es.wiktionary.org/wiki/Categor%C3%ADa:DE:Sustantivos_masculinos',
        'https://es.wiktionary.org/wiki/Categor%C3%ADa:DE:Sustantivos_neutros',

        'https://pl.wiktionary.org/wiki/Kategoria:J%C4%99zyk_niemiecki_-_rzeczowniki_rodzaju_m%C4%99skiego', # DE in PL
        'https://pl.wiktionary.org/wiki/Kategoria:J%C4%99zyk_niemiecki_-_rzeczowniki_rodzaju_nijakiego',
        'https://pl.wiktionary.org/wiki/Kategoria:J%C4%99zyk_niemiecki_-_rzeczowniki_rodzaju_%C5%BCe%C5%84skiego',

        'https://pl.wiktionary.org/wiki/Kategoria:J%C4%99zyk_polski_-_rzeczowniki_rodzaju_nijakiego', # PL in PL
        'https://pl.wiktionary.org/wiki/Kategoria:J%C4%99zyk_polski_-_rzeczowniki_rodzaju_m%C4%99skiego',
        'https://pl.wiktionary.org/wiki/Kategoria:J%C4%99zyk_polski_-_rzeczowniki_rodzaju_%C5%BCe%C5%84skiego',

        'https://en.wiktionary.org/wiki/Category:Polish_feminine_nouns', # PL in EN
        'https://en.wiktionary.org/wiki/Category:Polish_masculine_nouns',
        'https://en.wiktionary.org/wiki/Category:Polish_nouns_with_multiple_genders',
        'https://en.wiktionary.org/wiki/Category:Polish_neuter_nouns',

        'https://es.wiktionary.org/wiki/Categor%C3%ADa:PL:Sustantivos_femeninos', # PL in ES
        'https://es.wiktionary.org/wiki/Categor%C3%ADa:PL:Sustantivos_masculinos',
        'https://es.wiktionary.org/wiki/Categor%C3%ADa:PL:Sustantivos_neutros',

        'https://es.wiktionary.org/wiki/Categor%C3%ADa:ES:Sustantivos_masculinos', # ES in ES
        'https://es.wiktionary.org/wiki/Categor%C3%ADa:ES:Sustantivos_femeninos',
        'https://es.wiktionary.org/wiki/Categor%C3%ADa:ES:Sustantivos_ambiguos',

        'https://en.wiktionary.org/wiki/Category:Spanish_feminine_nouns', # ES in EN
        'https://en.wiktionary.org/wiki/Category:Spanish_masculine_nouns',
        'https://en.wiktionary.org/wiki/Category:Spanish_nouns_with_multiple_genders',
        'https://en.wiktionary.org/wiki/Category:Spanish_masculine_and_feminine_nouns_by_sense',
        'https://en.wiktionary.org/wiki/Category:Spanish_gender-neutral_nouns',

        'https://de.wiktionary.org/wiki/Kategorie:Substantiv_f_(Spanisch)', # ES in DE
        'https://de.wiktionary.org/wiki/Kategorie:Substantiv_m_(Spanisch)',

        'https://fr.wiktionary.org/wiki/Cat%C3%A9gorie:Mots_parfois_masculins_ou_f%C3%A9minins_en_espagnol', # ES in FR
        'https://fr.wiktionary.org/wiki/Cat%C3%A9gorie:Mots_parfois_f%C3%A9minins_ou_masculins_en_espagnol',

        'https://pl.wiktionary.org/wiki/Kategoria:J%C4%99zyk_hiszpa%C5%84ski_-_rzeczowniki_rodzaju_m%C4%99skiego', # ES in PL
        'https://pl.wiktionary.org/wiki/Kategoria:J%C4%99zyk_hiszpa%C5%84ski_-_rzeczowniki_rodzaju_%C5%BCe%C5%84skiego',
    ]

    def parse(self, response):

        gender_dict = {'and': None, # EN
                       'masculine' : 'masculine',
                       'feminine': 'feminine',
                       'gender-neutral': None,
                       'multiple': None,
                       'neuter': 'neuter',
                       'nijakiego' : 'neuter', # PL
                       'męskiego' : 'masculine',
                       'm%C4%99skiego': 'masculine',
                       'żeńskiego': 'feminine',
                       '%C5%BCe%C5%84skiego': 'feminine',
                       'm (Deutsch)' : 'masculine', # DE
                       'f (Deutsch)': 'feminine',
                       'n (Deutsch)': 'neuter',
                       'zwei': None,
                       'drei': None,
                       'multigenres': None, # FR
                       'parfois': None,
                       'masculinos' : 'masculine', # ES
                       'femeninos': 'feminine',
                       'ambiguos': None
                       }
  
        lang_dict = {
            'fr' : 'page suivante',
            'es': 'página siguiente',
            'de': 'nächste Seite',
            'pl': 'następna strona',
            'en': 'next page'
        }
        article_lang_dict = {
            'French': 'fr', # EN
            'Spanish': 'es',
            'German': 'de',
            'Polish': 'pl',
            '(Französisch)': 'fr', # DE
            '(Franz%C3%B6sisch)': 'fr',
            '(Spanisch)': 'es',
            '(Deutsch)': 'de',
            'niemiecki': 'de', # PL
            'hiszpański': 'es',
            'francuski': 'fr',
            'polski': 'pl',
            'DE': 'de', # ES
            'PL': 'pl',
            'FR': 'fr',
            'ES': 'es',
            'fran%C3%A7ais': 'fr', # FR
            'français': 'fr',
            'allemand': 'de',
            'espagnol': 'es',
        }

        info_sentence = response.xpath("//span[@class='mw-page-title-main']/text()").get()

        for key in gender_dict:
            if key in info_sentence:
                gender = gender_dict[key]

        nouns = response.xpath("//div[@class='mw-category-group']/ul/li/a/text()").getall()
        site_lang = response.headers[b'Content-Language'].decode('utf-8')
        

        for lang_keyword in article_lang_dict:
            if lang_keyword in info_sentence:
                lang = article_lang_dict[lang_keyword]

        for noun in nouns:
            yield {
                'noun': noun,
                'gender': gender,
                'lang': lang,
                }
            
        next_page = response.xpath(f"//div[@id='mw-pages']/a[text()='{lang_dict[site_lang]}']/@href").get()
        if next_page:
            yield response.follow(next_page, callback=self.parse)