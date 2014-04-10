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
// Updated on 2014-02-17
// Updated on 2014-02-18
// Updated on 2014-02-18
// Updated on 2014-02-25
// Updated on 2014-02-28
// Updated on 2014-03-11
// Updated on 2014-03-11
// Updated on 2014-03-16
// Updated on 2014-03-16
// Updated on 2014-03-16
// Updated on 2014-03-16
// Updated on 2014-03-17
// Updated on 2014-03-18
// Updated on 2014-03-18
// Updated on 2014-03-21
// Updated on 2014-03-21
// Updated on 2014-03-21
// Updated on 2014-03-21
// Updated on 2014-03-24
// Updated on 2014-03-25
// Updated on 2014-03-27
// Updated on 2014-04-02
// Updated on 2014-04-06
// Updated on 2014-04-06
// Updated on 2014-04-07
// Updated on 2014-04-07
// Updated on 2014-04-07
// Updated on 2014-04-10
