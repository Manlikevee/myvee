from flask import render_template, url_for, session, redirect, request

from shop import app, db


@app.route('/')
def home():
    return "homepage of your shop"





