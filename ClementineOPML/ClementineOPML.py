#!/usr/bin/env python
# Export podcast subscriptions from Clementine in OPML format.
# OPML spec - http://dev.opml.org/spec2.html

import argparse
import sqlite3
import sys
from datetime import datetime, timezone
from pathlib import Path

from lxml.etree import Comment, Element, ElementTree, ParseError, SubElement


def main():
    parser = argparse.ArgumentParser(
        description="Export podcast subscriptions from Clementine.",
    )
    parser.add_argument(
        "--clementine-db-path",
        type=Path,
        default=None,
        help="Path to the Clementine database. Defaults to the Clementine default.",
    )
    parser.add_argument(
        "--output-path",
        type=Path,
        default=None,
        help="Path to export the OPML file to. Defaults to ~/Clementine-Podcasts.opml",
    )
    args = parser.parse_args()
    export(args=args)


def export(args):
    db_path = args.clementine_db_path
    output_path = args.output_path

    db_path = db_path or find_db()
    output_path = output_path or Path("~/Clementine-Podcasts.opml")

    db_path = Path(db_path).expanduser()
    output_path = Path(output_path).expanduser()

    if not db_path.exists():
        print(f"File not found: {str(db_path)}.")
        sys.exit(1)

    podcasts = get_podcasts(db_path=db_path)
    xml = build_xml(podcasts=podcasts)
    write_to_disk(xml=xml, output_path=output_path)
    print(f"Done -> {str(output_path)}")


def get_podcasts(db_path):
    _db_conn = None
    try:
        _db_conn = sqlite3.connect(db_path)
        _db_conn.execute("pragma query_only = ON")
    except Exception as e:
        print(e)
        sys.exit(1)

    _cursor = _db_conn.cursor()
    _cursor.execute(
        "SELECT url AS xmlURL, title, description AS text, link AS htmlUrl FROM podcasts"
    )
    _podcasts = _cursor.fetchall()
    return _podcasts


def find_db():
    _db_path = Path("~/.config/Clementine/clementine.db").expanduser()
    _windows_db_path = Path(
        "~/Library/Application Support/Clementine/clementine.db"
    ).expanduser()
    if _db_path.exists():
        return _db_path
    elif _windows_db_path.exists():
        return _windows_db_path
    else:
        print(
            "ERROR: Could not locate the Clementine DB. Specify its location with `--clementine-db-path`"
        )
        sys.exit(1)


def build_xml(podcasts):
    _created_date = datetime.now(timezone.utc).astimezone()
    _created_date.isoformat()

    _opml = Element("opml")
    _opml.set("version", "2.0")
    _comment = Comment("Podcasts exported from Clementine.")
    _opml.append(_comment)
    _head = SubElement(_opml, "head")
    _title = SubElement(_head, "title")
    _date_created = SubElement(_head, "dateCreated")
    _title.text = "Podcasts Exported from Clementine."
    _date_created.text = str(_created_date)
    _body = SubElement(_opml, "body")

    for _podcast in podcasts:
        _xmlUrl = _podcast[0]
        _title = _podcast[1]
        _text = _podcast[2]
        _htmlUrl = _podcast[3]

        _text = _text or ""
        _htmlUrl = _htmlUrl or ""

        _outline = SubElement(_body, "outline")
        _outline.set("xmlUrl", _xmlUrl)
        _outline.set("title", _title)
        _outline.set("text", _text)
        _outline.set("htmlUrl", _htmlUrl)
        _outline.set("type", "rss")
    return _opml


def write_to_disk(xml, output_path):
    try:
        _output_file = open(output_path, "wb")
    except OSError as e:
        print(e)
        sys.exit(1)
    try:
        ElementTree(xml).write(
            _output_file, encoding="utf-8", xml_declaration=True, pretty_print=True
        )
    except ParseError as e:
        print(f"Could not parse the output XML: {str(e)}.")


if __name__ == "__main__":
    main()
