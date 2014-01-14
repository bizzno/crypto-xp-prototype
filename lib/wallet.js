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
