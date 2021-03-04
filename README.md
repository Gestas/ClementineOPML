# Simple OPML exporter for the Clementine Player
http://www.clementine-player.org/
Tested with Python3.8 on Ubuntu 20.04.

### Install
**NOTE:** Using `pipx` is strongly recommended, https://pypi.org/project/pipx/.
Pipx will create the required virtualenv and ensure that `ClementineOPML` is in your path. 
```
$ pipx install https://github.com/Gestas/ClementineOPML
```
### Usage - 
```
# Can be run without any arguments - 
$ ClementineOPML

$ ClementineOPML -h
usage: ClementineOPML [-h] [--clementine-db-path CLEMENTINE_DB_PATH] [--output-path OUTPUT_PATH]

Export podcast subscriptions from Clementine.

optional arguments:
  -h, --help            show this help message and exit
  --clementine-db-path CLEMENTINE_DB_PATH
                        Path to the Clementine database. Defaults to the Clementine default.
  --output-path OUTPUT_PATH
                        Path to export the OPML file to. Defaults to ~/Clementine-Podcasts.opml
```

