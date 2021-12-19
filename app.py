#!/usr/bin/env python3

from flask import Flask, request
import yfinance as yf
import os
import signal
import sys

app = Flask(__name__)
app_host = os.getenv("APP_HOST") or "0.0.0.0"
app_port = os.getenv("APP_PORT") or "8000"

@app.route("/download/<string:symbol>/<string:start>/<string:end>", methods=["GET"])
def download(symbol, start, end):
    interval = request.args.get("interval", default="1d", type=str)
    group_by = request.args.get("group_by", default="ticker", type=str)

    data = yf.download(symbol, start=start, end=end, interval=interval, prepost=True, group_by=group_by)
    return data.to_json()


@app.route("/info/<string:symbol>", methods=["GET"])
def info(symbol):
    return yf.Ticker(symbol).info

@app.route("/analysis/<string:symbol>", methods=["GET"])
def analysis(symbol):
    return yf.Ticker(symbol).analysis.to_json()

@app.route("/healthcheck", methods=["GET"])
def healthcheck():
    return "OK"

def signal_handler(sig, frame):
    print('Shutting down.')
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

if __name__ == "__main__":
    app.run(host=app_host, port=app_port)
