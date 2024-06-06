from flask import Flask, render_template, request
from web3 import Web3

app = Flask(__name__)

# Connect to your Ethereum node or an Ethereum provider like Infura
web3 = Web3(Web3.HTTPProvider('https://mainnet.infura.io/v3/YOURAPIKEYHERE'))


def get_latest_block():
    return web3.eth.getBlock('latest')


def get_block_by_number(block_number):
    return web3.eth.getBlock(block_number)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        block_number = int(request.form['block_number'])
        block = get_block_by_number(block_number)
        return render_template('index.html', latest_block=get_latest_block(), block=block)
    else:
        latest_block = get_latest_block()
        return render_template('index.html', latest_block=latest_block)



if __name__ == '__main__':
    app.run(debug=True)
