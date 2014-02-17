function Transaction(from, to, amount) {
    this.from = from;
    this.to = to;
    this.amount = amount;
    this.timestamp = Date.now();
}

Transaction.prototype.hash = function() {
    return require('crypto').createHash('sha256')
        .update(this.from + this.to + this.amount + this.timestamp)
        .digest('hex');
};

module.exports = Transaction;
// Updated on 2014-02-17
// Updated on 2014-02-17
