## Simple OPML exporter for the Clementine Player
http://www.clementine-player.org/

Tested with Python3.9 on Ubuntu 20.04. Will likely work with earlier versions.

### Usage - 
```usage: ClementineOPML.py [-h] [--clementine-db-path CLEMENTINE_DB_PATH] [--output-path OUTPUT_PATH]

Export podcast subscriptions from Clementine.

optional arguments:
  -h, --help            show this help message and exit
  --clementine-db-path CLEMENTINE_DB_PATH
                        Path to the Clementine database. Defaults to the Clementine default.
  --output-path OUTPUT_PATH
                        Path to export the OPML file to. Defaults to ~/Clementine-Podcasts.opml
```

### Install - 
**NOTE:** This example uses `pipx` to `virtualenv` because it's better. See [installing with pip](https://virtualenv.pypa.io/en/latest/installation.html#via-pip) if required.
```
pipx install virtualenv
git clone https://github.com/Gestas/ClementineOPML
cd ClementineOPML
virtualenv venv --python $(which python3.9)
chmod +x ClementineOPML.py
./ClementineOPML.py
```