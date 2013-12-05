"""Blockchain implementation for cryptocurrency"""
import hashlib
import json
from time import time

class Blockchain:
    def __init__(self):
        self.chain = []
        self.pending_transactions = []
        # Create genesis block
        self.new_block(previous_hash='1', proof=100)

    def new_block(self, proof, previous_hash=None):
        """Create a new block in the blockchain"""
        block = {
            'index': len(self.chain) + 1,
            'timestamp': time(),
            'transactions': self.pending_transactions,
            'proof': proof,
            'previous_hash': previous_hash or self.hash(self.chain[-1]),
        }
        self.pending_transactions = []
        self.chain.append(block)
        return block

    @staticmethod
    def hash(block):
        """Hash a block"""
        block_string = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()
Update 6 on 2013-11-20 02:25:57
Update 9 on 2013-11-22 11:50:25
Update 16 on 2013-11-28 07:56:11
Update 19 on 2013-11-28 04:57:34
Update 29 on 2013-12-04 05:18:58
Update 34 on 2013-12-05 21:21:30
