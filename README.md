# About pokescrap

**Pokescrap** enables anyone to scrape the data from the many real-time PokeMaps available (such as https://sgpokemap.com) and store it in a SQLite database for further exploration.

Please use this software responsible.  The default configuration does not generate more data traffic than a regular browser.  Limit the area scanned to a sensible default (please refer to the section regarding configuration).

## Installation

###Prerequisites

Any relatively sane development environment with Python 3.x should work.  **Pokescrap** uses *Scrapy* (https://scrapy.org/) and - when hiding behind proxies is necessary - *scrapy-proxies*.  **Pokescrap** also uses SQLite3.

Install as follows:

```
apt-get install sqlite3
pip install scrapy
pip install scrapy_proxies
```
Install **Pokescrap** from github:

```
git clone https://github.com/jeerbees/pokescrap.git
cd pokescrap
```

## Configuration

Edit *pokescrap/settings.py*. Everything should be pretty much self-explanatory.  Especially review these settings:

* POKESCRAP_SCOPE: the map you want to scrape
* POKESCRAP_BOUNDS: the area you want to scrape (latitude and longitude)

After editing the configuration, run Scrapy from the top directory:

```scrapy crawl pokemap```

This should create the database (*db/pokescrap.sqlite*).  End the running program by hitting CTRL-C in the console.

In case this works, you might want to disable logging by modifying the standard configuration to:

``````
LOG_ENABLED = '0'
``````

## Additional

In case you want to hide behind proxies, please configure (un-comment) the settings at the end of *settings.py*.

## SSL connection problems

This might be caused by an incompatibility with OpenSSL, used by the Twisted package. 
Try upgrading Python to the latest version. Upgrade Twisted.

## Python2 compatibility

Modify (in *pokescrap/spiders/pokemap.py*)

```
from urllib.parse import urljoin, urlparse
```

to

```
from urlparse import urljoin, urlparse
```

## More information

Visit my website at https://www.jeerbees.com



## Disclaimer

Pokémon and all respective names are trademark and/or © of Nintendo 1996-2017.  Pokémon GO is trademark and © of Niantic, Inc.  

Jeerbees is not affiliated with Niantic Inc., The Pokemon Company, or Nintendo. 