# ADS-B Feeder Image Web Sources

This repo contains the html, css, and static resources used for the [ADS-B Feeder Image web site](https://adsb.im/home).

Contributions, suggestions, corrections, and additions are welcome.

## Local testing

The local testing needs some work for developer convenience, but is usable.

`$ docker-compose up` spins up a python instance with a web server listening at `http://localhost:8000/`. [`/web/app.py`](/web/app.py) contains the respective glue code that renders the templates.

While developing, have an eye on the console where `docker-compose` runs since syntax errors might crash the script and need a restart.
