import sys
from pathlib import Path

from bottle import Bottle

from project.app.app import App


def main():
    host = 'localhost'
    port = 8080
    if len(sys.argv) > 2:
        host = sys.argv[1]
        port = int(sys.argv[2])
    db_path = Path('./db/main.db')
    App(Bottle(autojson=False), host, port, db_path).launch()


main()
