var crypto = require('crypto');

function Wallet() {
    this.privateKey = crypto.randomBytes(32);
    this.publicKey = crypto.randomBytes(33);
    this.address = crypto.createHash('sha256').update(this.publicKey).digest('hex').substring(0, 40);
}

Wallet.prototype.sign = function(data) {
    return crypto.createSign('sha256').update(data).sign(this.privateKey, 'hex');
};

module.exports = Wallet;
// Updated on 2014-01-07
// Updated on 2014-01-07
// Updated on 2014-01-09
// Updated on 2014-01-09
// Updated on 2014-01-10
// Updated on 2014-01-10
// Updated on 2014-01-10
// Updated on 2014-01-14
// Updated on 2014-01-15
// Updated on 2014-01-15
// Updated on 2014-01-15
// Updated on 2014-01-15
// Updated on 2014-01-16
// Updated on 2014-01-16
// Updated on 2014-01-16
// Updated on 2014-01-20
// Updated on 2014-01-20
// Updated on 2014-01-21
// Updated on 2014-02-04
// Updated on 2014-02-04
// Updated on 2014-02-04
// Updated on 2014-02-05
// Updated on 2014-02-05
// Updated on 2014-02-06
// Updated on 2014-02-07
// Updated on 2014-02-07
// Updated on 2014-02-07
// Updated on 2014-02-13
// Updated on 2014-02-15
// Updated on 2014-02-15
// Updated on 2014-02-17
// Updated on 2014-02-17
// Updated on 2014-02-17
// Updated on 2014-02-18
// Updated on 2014-02-25
// Updated on 2014-02-25
// Updated on 2014-02-25
// Updated on 2014-02-25
// Updated on 2014-02-28
// Updated on 2014-03-11
