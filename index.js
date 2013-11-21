var crypto = require('crypto');

function createWallet() {
    return {
        address: crypto.randomBytes(20).toString('hex'),
        balance: 0
    };
}

module.exports = { createWallet };
