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
Update 40 on 2013-12-06 00:58:02
Update 41 on 2013-12-09 08:01:19
Update 46 on 2013-12-09 12:59:31
Update 55 on 2013-12-16 04:54:47
Update 75 on 2013-12-19 07:49:38
Update 85 on 2013-12-21 17:05:07
Update 90 on 2013-12-23 22:32:06
Update 94 on 2013-12-23 23:12:02
Update 100 on 2013-12-26 14:48:04
Update 105 on 2013-12-26 20:21:01
Update 115 on 2013-12-28 16:50:29
Update 117 on 2013-12-28 17:01:41
Update 122 on 2014-01-01 18:11:17
Update 130 on 2014-01-04 10:34:42
Update 133 on 2014-01-04 01:06:03
Update 138 on 2014-01-06 00:43:09
Update 139 on 2014-01-06 10:28:50
Update 146 on 2014-01-07 15:01:52
Update 147 on 2014-01-07 17:11:49
Update 158 on 2014-01-13 21:08:33
Update 161 on 2014-01-13 11:43:14
Update 165 on 2014-01-17 05:20:12
Update 167 on 2014-01-17 18:43:45
Update 174 on 2014-01-17 04:03:48
Update 176 on 2014-01-17 17:30:10
Update 181 on 2014-01-18 22:55:13
Update 183 on 2014-01-19 19:16:20
Update 187 on 2014-01-23 02:54:18
Update 189 on 2014-01-23 07:14:16
Update 195 on 2014-01-25 20:24:49
Update 212 on 2014-01-31 15:49:42
Update 213 on 2014-01-31 03:34:12
Update 215 on 2014-01-31 16:30:05
Update 224 on 2014-02-16 12:27:58
Update 226 on 2014-02-16 19:15:54
Update 235 on 2014-02-17 13:12:23
Update 240 on 2014-02-18 08:14:58
Update 245 on 2014-02-20 02:30:31
Update 246 on 2014-02-20 23:36:22
Update 252 on 2014-02-25 22:44:11
Update 263 on 2014-02-25 01:19:00
Update 269 on 2014-02-27 19:22:59
Update 280 on 2014-03-03 05:47:15
Update 293 on 2014-03-11 18:19:29
Update 299 on 2014-03-13 03:41:59
Update 301 on 2014-03-13 08:39:56
Update 304 on 2014-03-13 03:46:57
Update 317 on 2014-03-20 07:43:07
Update 323 on 2014-03-21 12:49:15
Update 324 on 2014-03-21 03:34:14
Update 330 on 2014-03-21 09:09:21
Update 334 on 2014-03-21 20:44:53
Update 335 on 2014-03-21 10:27:36
Update 340 on 2014-03-23 10:30:18
Update 341 on 2014-03-23 07:38:41
Update 350 on 2014-03-25 21:27:53
Update 358 on 2014-03-26 05:41:56
Update 363 on 2014-03-26 17:38:46
Update 373 on 2014-03-30 14:09:58
Update 377 on 2014-03-30 18:22:07
Update 380 on 2014-03-31 02:49:59
Update 381 on 2014-03-31 21:14:35
Update 388 on 2014-04-07 13:06:20
