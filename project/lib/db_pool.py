import sqlite3

from cuttlepool import CuttlePool


class DbConnectionPool(CuttlePool):
    """https://pypi.org/project/cuttlepool/"""

    def __init__(self, database, capacity, **kwargs):
        super().__init__(factory=sqlite3.connect, database=database, capacity=capacity, **kwargs)

    def normalize_resource(self, resource):
        resource.row_factory = None

    def ping(self, resource):
        try:
            selection = resource.execute('SELECT 1').fetchall()
            return selection == [(1,)]
        except sqlite3.Error:
            return False
