# Crypto XP Prototype

Experimental cryptocurrency prototype with blockchain and wallet functionality.

## Features

- Blockchain implementation with proof-of-work
- Digital wallet with key management
- Transaction creation and verification
- Block mining and validation
- Peer-to-peer network simulation
- Merkle tree for transaction integrity
- Address generation and signing

## Structure

```
src/
├── blockchain/    - Blockchain class and block validation
├── wallet/        - Wallet class, keys, and transaction signing
├── network/       - P2P networking and peer management
└── mining/        - Mining algorithms and difficulty adjustment
```

## Installation

Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

Create a blockchain and mine a block:
```python
from src.blockchain.chain import Blockchain

blockchain = Blockchain()
blockchain.add_transaction('Alice', 'Bob', 50)
blockchain.mine_pending_transactions('Miner1')
```

Create a wallet:
```python
from src.wallet.wallet import Wallet

wallet = Wallet()
print(f"Address: {wallet.address}")
print(f"Balance: {blockchain.get_balance(wallet.address)}")
```

## Requirements

- Python 3.6 or higher
- cryptography library
- hashlib for hashing

## License

MIT
