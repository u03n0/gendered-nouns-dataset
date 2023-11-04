# gendered-nouns-dataset

A collection of labeled nouns (gendered) for a few languages (French, German, Polish, Spanish)

## Goal

The goal is to build a dataset of as many (all) nouns that exist in the target languages (en, fr, de, pl) and are labeled
accordingly with their gender (masculine, feminine, neuter).

## Stats

Currently there are 517, 176 examples in the dataset. With some [caveats](/#caveats).

## How to Use

Simply download any of the `csv` files and use it in your project.<br />

Or, if you would like to run the web scraper you must have `pipenv` installed on your system.
1. clone/download the repo.
2. `cd` into the repo.
3. Activate the virtual enviroment with `pipenv shell`.
4. `cd` into `wiktionary`.
5. Feel free to modify/comment any urls in `/wiktionary/spiders/wiktionary.py`, or skip step.
6. run the following command `scrapy wiktionary.py -O <name_of_output_file>.csv` (must be in `/wiktionary/`).



## Sources

1. The first source is pulled via a web scaper (Scrapy) from Wiktionary.org
  * Each languages was searched in:
      * English (en.wiktionary.org)
      * Its target language Ex: French (fr.wiktionary.org)
      * In each other language EX: PL (pl.wiktionary.org ) searching for French nouns, ES (ex.wiktionary.org) searching German nouns etc.

## Saved format

The data is saved into a `csv` file with the following headers (columns): `noun`, `gender`, and `lang`


## Caveats

* There are plenty of duplications in the dataset. An easy fix with Pandas to remove them.
* When a noun was both feminine and masculine, it was entered  as `None` for its `gender`. The rational was:
    * These can be used to remove nouns from dataset that might obscure your research. Filtering out undesirable nouns.
    * Can be later added as both masculine and feminine into the dataset.
    * Kept in for training purposes.
* Nouns can be proper nouns (names, place names, etc) which might not be desirable for your research.
* Nouns may contain: numbers, hypens, spaces.

## To Do

- [x] Scrape wiktionary.org
- [ ] Clean data (removing duplicates)
- [ ] Separate each language into its on data file
- [ ] Gather from other sources


## Academic Use

The integrity of this dataset is only as good as the sources used, and methods of filtering/gathering.
Please refer to the `wiktionary -> wiktionary -> spiders -> wiktionary,py` file to form a judgment on the intergrity of the scraper.


## Legal/Ethical

Web scraping may or may not be regulated/legal in your country. <br />
`robots.txt` is a file on websites that dictate how web scrapers should behave on the site, e.g how many requests can be made, etc. <br /> <br />
Within the `settings.py` the following code was modified to `ROBOTSTXT_OBEY = False` which does **not** follow the rules from said `robots.txt`.
This was necesary in order for the the `spider` to crawl multiple pages on a site by following the link to the pagination.<br />
With `ROBOTSTXT_OBEY` set to `True` then only the first page of a url will be scraped, drastically reducing the amount of data retrieved.
