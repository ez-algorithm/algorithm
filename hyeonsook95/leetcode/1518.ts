function numWaterBottles(numBottles: number, numExchange: number): number {
    var drink = 0;
    while (numBottles >= numExchange) {
        if (Math.floor(numBottles/numExchange) > 0) {
            var exchanged = Math.floor(numBottles/numExchange);
            var nonExchanged = numBottles%numExchange;
            numBottles = exchanged + nonExchanged;
            
            drink += exchanged * numExchange;
        }
    }
    return drink + numBottles;
};