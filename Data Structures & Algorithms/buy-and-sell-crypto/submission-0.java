class Solution {
    public int maxProfit(int[] prices) {

        // handle empty/single/null array
        if (prices == null || prices.length <= 1) {
            return 0;
        }
        
        // this is a variable to keep track of minimum buy price
        int minBuyPrice = prices[0];

        // keep track of the max profit possible
        int maxProfit = 0;


        for (int i = 1; i < prices.length; i++) {
            // variable to keep track of the current price
            int currPrice = prices[i];

            // if the current price is less that the min buy price, replace
            // that price because we ideally want to buy the stock when it 
            // is at its lowest price
            if (currPrice < minBuyPrice) {
                minBuyPrice = currPrice;
            }
            else {

                // store the current profit (which could be the potential
                // max profit)
                int currProfit = currPrice - minBuyPrice;

                // if this profit is greater, replace max profit
                if (currProfit > maxProfit) {
                    maxProfit = currProfit;
                }
            }

            // this is sliding window because we calculate the current profit
            // with every potential entry after the minBuyPrice


        }

        return maxProfit;
    }
}
