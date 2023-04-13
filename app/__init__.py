"""Setup at app startup"""
from flask import Flask
import psycopg2


app = Flask(__name__)
postgres = psycopg2.connect(
        host="dpg-cgrq2dhmbg5e4khq7kf0-a.oregon-postgres.render.com",
        database="todo_y8z0",
        user="root",
        password="MTTgrnuO0oxLy85zHxeed5YFw4GV8vGh")
# To prevent from using a blueprint, we use a cyclic import
# This also means that we need to place this import here
# pylint: disable=cyclic-import, wrong-import-position
from app import routes
