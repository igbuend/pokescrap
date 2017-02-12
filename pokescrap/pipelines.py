# -*- coding: utf-8 -*-
"""Define your item pipelines here
Don't forget to add your pipeline to the ITEM_PIPELINES setting.
See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html"""

import sqlite3
import os
from scrapy.exceptions import DropItem
from pokescrap.items import PokemonItem
from pokescrap.items import PokemonSpawnItem

# import requests

class PokescrapPipeline(object):
    """Our pipeline for our Pokescrap spider"""
    def __init__(self):
        self.conn = None
        self.cur = None

    def open_spider(self, spider): # pylint: disable=unused-argument
        """Create - if needed - and open the database"""
        db_path = spider.db_path
        if os.path.isfile(db_path):
            self.conn = sqlite3.connect(db_path)
            self.cur = self.conn.cursor()
        else:
            self.conn = sqlite3.connect(db_path)
            self.cur = self.conn.cursor()
            self.cur.execute('CREATE TABLE pokemon (pokemon_id text unique, \
            name text, \
            show_filter text)')
            self.cur.execute('CREATE TABLE spawn (identifier text unique, \
            spawn_id text, \
            lat text, \
            lng text, \
            despawn text, \
            disguise text, \
            attack text, \
            defence text, \
            stamina text, \
            move1 text, \
            move2 text, \
            inserted text, \
            time text)')
            self.conn.commit()

    def close_spider(self, spider): # pylint: disable=unused-argument
        """Close the spider and clean-up"""
        self.conn.commit()
        self.conn.close()

    def process_item(self, item, spider): # pylint: disable=unused-argument
        """Put Pokemon in DB"""
        if isinstance(item, PokemonSpawnItem):
            try:
                self.cur.execute('''INSERT INTO spawn VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)''',
                                 (item.get('identifier'),
                                  item.get('spawn_id'),
                                  item.get('lat'),
                                  item.get('lng'),
                                  item.get('despawn'),
                                  item.get('disquise'),
                                  item.get('attack'),
                                  item.get('defence'),
                                  item.get('stamina'),
                                  item.get('move1'),
                                  item.get('move2'),
                                  item.get('inserted'),
                                  item.get('time')))
                self.conn.commit()

            except sqlite3.IntegrityError:
#                raise DropItem("Duplicate pokemon spawn item found: %s" % item)
                pass
        else:
            if isinstance(item, PokemonItem):
                try:
                    self.cur.execute('''INSERT INTO pokemon VALUES (?,?,?)''',
                                     (item.get('pokemon_id'),
                                      item.get('name'),
                                      item.get('show_filter')))
                    self.conn.commit()

                except sqlite3.IntegrityError:
 #                  raise DropItem("Duplicate pokemon item found: %s" % item)
                    pass
            else:
                raise DropItem("Unknown item type, %s" % type(item))
        return item
