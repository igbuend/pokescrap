# -*- coding: utf-8 -*-
"""This script defines what the scraped items (using scrapy) are.
   Scrapy items are simple containers used to collect the scraped data.
   Please refer to https://doc.scrapy.org/en/latest/topics/items.html. """

from scrapy.item import Item, Field

class PokemonSpawnItem(Item):  # pylint: disable=too-many-ancestors
    """This class defines a scraped spawn"""
    identifier = Field()
    spawn_id = Field()
    lat = Field()
    lng = Field()
    despawn = Field()
    disguise = Field()
    attack = Field()
    defence = Field()
    stamina = Field()
    move1 = Field()
    move2 = Field()
    inserted = Field()
    time = Field()

class PokemonItem(Item):   # pylint: disable=too-many-ancestors
    """This class defines an scraped pokemon"""
    pokemon_id = Field()
    name = Field()
    show_filter = Field()
