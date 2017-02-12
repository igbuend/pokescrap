# -*- coding: utf-8 -*-
"""Definition of our Spider"""

import json
import logging
import time
from urllib.parse import urljoin, urlparse
from scrapy.exceptions import DontCloseSpider
import scrapy
from pokescrap.items import PokemonItem
from pokescrap.items import PokemonSpawnItem

class PokemapSpider(scrapy.Spider):
    """Our Pokemap Spider definition"""
    name = "pokemap"
    mons = ('1,2,3,4,5,6,7,8,9,10,'
            '11,12,13,14,15,16,17,18,19,20,'
            '21,22,23,24,25,26,27,28,29,30,'
            '31,32,33,34,35,36,37,38,39,40,'
            '41,42,43,44,45,46,47,48,49,50,'
            '51,52,53,54,55,56,57,58,59,60,'
            '61,62,63,64,65,66,67,68,69,70,'
            '71,72,73,74,75,76,77,78,79,80,'
            '81,82,83,84,85,86,87,88,89,90,'
            '91,92,93,94,95,96,97,98,99,100,'
            '101,102,103,104,105,106,107,108,109,110,'
            '111,112,113,114,115,116,117,118,119,120,'
            '121,122,123,124,125,126,127,128,129,130,'
            '131,132,133,134,135,136,137,138,139,140,'
            '141,142,143,144,145,146,147,148,149,150,'
            '151')

    def __init__(self, config_settings):  # could use some sanity checks
        """Needed to set variables from settings"""
        self.scope_url = config_settings['pokescrap_scope']
        self.bounds = config_settings['pokescrap_bounds']
        self.db_path = config_settings['pokescrap_db']
        self.force_refresh = urljoin(self.scope_url, '/?forcerefresh')
        parsed_domain = urlparse(self.scope_url)
        self.allowed_domains = [parsed_domain.netloc]
        self.start_urls = [self.force_refresh]

    @classmethod
    def from_crawler(cls, crawler):
        """Convoluted method to read settings"""
        crawler_scope = crawler.settings['POKESCRAP_SCOPE']
        crawler_bounds = crawler.settings['POKESCRAP_BOUNDS']
        crawler_dbpath = crawler.settings['POKESCRAP_DB']
        config_settings = dict(pokescrap_scope=crawler_scope,
                               pokescrap_bounds=crawler_bounds,
                               pokescrap_db=crawler_dbpath)
        return cls(config_settings)

    def _spider_idle(self, spider): # pylint: disable=unused-argument
        """Added this because sometimes unexpected exit"""
        yield scrapy.Request(url=self.force_refresh,
                             headers={'Referer': self.scope_url},
                             meta={'dont_merge_cookies': True},
                             callback=self.parse,
                             errback=self.handle_error)
        raise DontCloseSpider("Should not happen, \
        spider idle, \
        starting over")  # prevent closing spider

    def parse_pokescrap(self, response):
        """Handling the spawns"""
        logging.debug("Requesting latest spawns")

        try:
            json_response = json.loads(response.body_as_unicode())

            for k, val in json_response.items():
                if k == "meta":
                    dumpmeta = json.dumps(val)
                    meta = json.loads(dumpmeta)
                    answer_inserted = meta.get('inserted')
                    answer_time = meta.get('time')
                if k == "pokemons":
                    dumppokes = json.dumps(val)
                    pokes = json.loads(dumppokes)

            for i in pokes:
                new_spawn = PokemonSpawnItem()
                identifier = ""
                for k, val in i.items():
                    if k == "pokemon_id":
                        new_spawn['spawn_id'] = val
                        identifier = identifier + val
                    if k == "lat":
                        new_spawn['lat'] = val
                        identifier = identifier + val
                    if k == "lng":
                        new_spawn['lng'] = val
                        identifier = identifier + val
                    if k == "despawn":
                        new_spawn['despawn'] = val
                        identifier = identifier + val
                    if k == "disquise":
                        new_spawn['disguise'] = val
                        identifier = identifier + val
                    if k == "attack":
                        new_spawn['attack'] = val
                    identifier = identifier + val
                    if k == "defence":
                        new_spawn['defence'] = val
                        identifier = identifier + val
                    if k == "stamina":
                        new_spawn['stamina'] = val
                        identifier = identifier + val
                    if k == "move1":
                        new_spawn['move1'] = val
                        identifier = identifier + val
                    if k == "move2":
                        new_spawn['move2'] = val
                        identifier = identifier + val
                    new_spawn['inserted'] = answer_inserted
                    new_spawn['time'] = answer_time
                    new_spawn['identifier'] = identifier
                yield new_spawn
            time.sleep(60)
            spawn_list = urljoin(self.scope_url, \
            '/query2.php?since=0' + \
            '&' + \
            'mons=' + \
            self.mons + \
            '&' + \
            'bounds=' + \
            self.bounds)
            yield scrapy.Request(url=spawn_list, \
            dont_filter=True, \
            headers={'X-Requested-With':'XMLHttpRequest', \
            'Referer':self.force_refresh}, \
            callback=self.parse_pokescrap)
        except ValueError:  # TO DO - could be other errors, but this one needed for json.loads()
            logging.warn("Error requesting JSON data, re-starting after 60 seconds")
            time.sleep(60)
            yield scrapy.Request(url=self.force_refresh,
                                 headers={'Referer': self.scope_url},
                                 meta={'dont_merge_cookies': True},
                                 callback=self.parse,
                                 errback=self.handle_error)

    def parse_pokemons(self, response):
        """Getting the list of spawns"""
        logging.debug("Requesting list of pokemons")
        json_response = json.loads(response.body_as_unicode())
        for item in json_response:
            current_poke = PokemonItem()
            current_poke['pokemon_id'] = item.get('id')
            current_poke['name'] = item.get('name')
            current_poke['show_filter'] = item.get('show_filter')
            yield current_poke
        spawn_list = urljoin(self.scope_url, \
        '/query2.php?since=0' + \
        '&' + \
        'mons=' + \
        self.mons + \
        '&' + \
        'bounds=' + \
        self.bounds)
        yield scrapy.Request(url=spawn_list,
                             dont_filter=True,
                             headers={'X-Requested-With':'XMLHttpRequest',
                                      'Referer':self.force_refresh},
                             callback=self.parse_pokescrap,
                             errback=self.handle_error)

    def parse(self, response):
        """This gets the list of existing Pokemons"""
        logging.debug("Requesting initial URL")
        pokemon_list = urljoin(self.scope_url, '/pokemon_list.json?ver320')
        yield scrapy.Request(url=pokemon_list,
                             dont_filter=True,
                             headers={'Referer':self.force_refresh},
                             callback=self.parse_pokemons,
                             errback=self.handle_error)

    def handle_error(self, response): # pylint: disable=unused-argument
        """Called when error in HTTP request"""
        logging.warn("Error executing HTTP request, re-starting after 60 seconds")
        time.sleep(60)
        yield scrapy.Request(url=self.force_refresh,
                             headers={'Referer': self.scope_url},
                             meta={'dont_merge_cookies': True},
                             callback=self.parse,
                             errback=self.handle_error)
