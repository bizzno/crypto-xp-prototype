"""Transaction handling for cryptocurrency"""

class Transaction:
    def __init__(self, sender, recipient, amount):
        self.sender = sender
        self.recipient = recipient
        self.amount = amount

    def to_dict(self):
        return {
            'sender': self.sender,
            'recipient': self.recipient,
            'amount': self.amount
        }
Update 10 on 2013-11-26 21:17:17
Update 13 on 2013-11-28 09:30:57
Update 15 on 2013-11-28 17:13:28
Update 18 on 2013-11-28 12:23:16
Update 26 on 2013-12-03 16:46:02
Update 35 on 2013-12-05 20:39:03
Update 36 on 2013-12-06 00:16:54
