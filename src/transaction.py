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
Update 47 on 2013-12-09 14:43:04
Update 49 on 2013-12-11 13:19:20
Update 58 on 2013-12-18 08:50:24
Update 61 on 2013-12-18 23:42:39
Update 63 on 2013-12-18 22:37:34
Update 64 on 2013-12-18 10:50:44
Update 67 on 2013-12-18 06:30:54
Update 71 on 2013-12-19 11:50:02
Update 73 on 2013-12-19 00:26:30
Update 82 on 2013-12-21 20:46:25
Update 83 on 2013-12-21 21:33:13
Update 87 on 2013-12-23 15:47:50
Update 88 on 2013-12-23 01:18:50
Update 91 on 2013-12-23 11:32:17
Update 93 on 2013-12-23 19:53:16
Update 97 on 2013-12-26 13:48:18
Update 108 on 2013-12-27 22:10:16
Update 109 on 2013-12-27 18:14:36
Update 113 on 2013-12-28 13:53:24
Update 116 on 2013-12-28 15:12:20
Update 120 on 2014-01-01 02:03:37
Update 121 on 2014-01-01 21:13:55
Update 127 on 2014-01-04 16:03:46
Update 129 on 2014-01-04 06:13:51
Update 140 on 2014-01-06 04:25:42
Update 142 on 2014-01-07 16:10:09
Update 145 on 2014-01-07 09:34:20
Update 152 on 2014-01-07 00:35:55
Update 155 on 2014-01-13 18:17:39
Update 162 on 2014-01-13 00:53:10
Update 166 on 2014-01-17 12:02:46
