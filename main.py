from flask import Flask, render_template, redirect
import requests
import json

app: Flask = Flask( __name__ )


@app.route( "/" )
def index():
    cotacao = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")
    cotacao = cotacao.json()
    cotacao_bit = cotacao['BTCBRL']['bid']
    cotacao_euro = cotacao['EURBRL']['bid']
    cotacao_real = cotacao['USDBRL']['bid']

    return render_template('index.html', bit=cotacao_bit, euro=cotacao_euro,
                           real=cotacao_real)


if __name__ != "__name__":
    app.run()
