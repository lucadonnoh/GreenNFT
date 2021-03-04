import os
import urllib.request

import json
import numpy as np
from web3 import Web3

from dotenv import load_dotenv

load_dotenv()
etherscan_token = os.environ['ETHERSCAN_TOKEN']
infura_token = os.environ['INFURA_TOKEN']

w3 = Web3(Web3.HTTPProvider(f'https://mainnet.infura.io/v3/{infura_token}'))
print(w3.eth.block_number())


def get_gas(address, start_block, requested_names=['mint']):
    address = Web3.toChecksumAddress(address)

    contract_info_url = f'https://api.etherscan.io/api?module=contract&action=getabi&address={address}&apikey={etherscan_token}'
    contents = urllib.request.urlopen(contract_info_url).read()
    contract_info = json.loads(contents)
    abi = json.loads(contract_info['result'])

    transactions_info_url = f'https://api.etherscan.io/api?module=account&action=txlist&address={address}&startblock={start_block}&endblock=99999999&sort=asc&apikey={etherscan_token}'
    transactions_info = json.loads(urllib.request.urlopen(transactions_info_url).read())


    gas_results = {}
    for name in requested_names:
        gas_results[name] = []

    contract = w3.eth.contract(address=address, abi=abi)

    for transaction in transactions_info['result']:
        if transaction['to'].lower() == address.lower() and transaction['txreceipt_status'] == '1':
            transaction_input = transaction['input']
            transaction_input = contract.decode_function_input(transaction_input)
            function_name = transaction_input[0].fn_name

            if function_name in requested_names:
                gas_results[function_name].append(int(transaction['gasUsed']))

    return gas_results


global_names = ['mint']

nfts = json.load(open('nfts.json'))


results = []

for nft in nfts:
    required_names = []
    for name in global_names:
        if name in nft.keys():
            required_names.append(nft[name])
        else:
            required_names.append(name)
    
    gas_results = get_gas(nft['address'], 0, required_names)

    gas_info = {
        'name' : nft['name'],
        'address' : nft['address']
    }

    reverse_dict = {v: k for k, v in nft.items()}

    for name in required_names:
        if name in reverse_dict.keys():
            true_name = reverse_dict[name]
        else:
            true_name = name
        values = np.array(gas_results[name])
        gas_info[true_name] = {
            'mean' : np.mean(values),
            'median' : np.median(values)
        }

    results.append(gas_info)

file_ = open('results.json', 'w')
json.dump(results, file_)