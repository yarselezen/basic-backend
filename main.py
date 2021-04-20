
import sys
from pathlib import Path

from bottle import Bottle

from project.app.app import App

allowed_hosts = {'localhost', '127.0.0.1', '0.0.0.0'}


def main():
    host = 'localhost'
    port = '8080'
    arg_len = len(sys.argv)
    if arg_len == 2:
        port = sys.argv[1]
    if arg_len > 2:
        host = sys.argv[1]
        port = sys.argv[2]
    if host not in allowed_hosts:
        raise ValueError("Host '{}' is not allowed".format(host))
    if not port.isdigit():
        raise ValueError("Port '{}' is invalid".format(port))
    App(Bottle(autojson=False), host, int(port), Path('./db/main.db')).launch()


main()
