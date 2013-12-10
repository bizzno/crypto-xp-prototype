var crypto = require('crypto');

function createWallet() {
    return {
        address: crypto.randomBytes(20).toString('hex'),
        balance: 0
    };
}

module.exports = { createWallet };
// Updated on 2013-11-22
// Updated on 2013-11-23
// Updated on 2013-11-25
// Updated on 2013-11-27
// Updated on 2013-11-29
// Updated on 2013-11-29
// Updated on 2013-11-29
// Updated on 2013-11-29
// Updated on 2013-11-29
// Updated on 2013-12-01
// Updated on 2013-12-01
// Updated on 2013-12-01
// Updated on 2013-12-01
// Updated on 2013-12-01
// Updated on 2013-12-02
// Updated on 2013-12-10
// Updated on 2013-12-10
