from web3 import Web3

polygon_rpc_url = Web3(Web3.HTTPProvider('https://polygon-mumbai-bor.publicnode.com'))
web = Web3(Web3.HTTPProvider(polygon_rpc_url))

contract_abi = [
    {
        "inputs": [],
        "name": "getFlag",
        "outputs": [{"internalType": "string", "name": "", "type": "string"}],
        "stateMutability": "view",
        "type": "function",
    }
]
contract_address = "0xCE69Ea4901b51d0E24981be690010E48E1C6336c"
contract = web.eth.contract(address=contract_address, abi=contract_abi)
flag = contract.functions.getFlag().call()

print("Flag:", flag)