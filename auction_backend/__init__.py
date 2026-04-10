"""
Register PyMySQL as mysqlclient (MySQLdb) for Django's MySQL backend.

Must run before Django database code imports MySQLdb (see settings import order).
"""

import pymysql

pymysql.install_as_MySQLdb()
