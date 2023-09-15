
import {Web3} from "web3";

const web3 = new Web3("https://polygon-mumbai-bor.publicnode.com");

// interacting with the smart contract
const abi = [
    {
        "inputs": [],
        "name": "getFlag",
        "outputs": [{"internalType": "string", "name": "", "type": "string"}],
        "stateMutability": "view",
        "type": "function",
    }
];

const address = "0xCE69Ea4901b51d0E24981be690010E48E1C6336c";

// create a new contract object, providing the ABI and address
const contract = new web3.eth.Contract(abi, address);

contract.methods
    .getFlag()
    .call()
    .then(console.log);