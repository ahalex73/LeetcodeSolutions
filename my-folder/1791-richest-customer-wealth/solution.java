class Solution {
    public int maximumWealth(int[][] accounts) {
        int max_wealth = 0;
        for(int[] customer: accounts){
            int curr_wealth = 0;

            for(int bank : customer){
                curr_wealth += bank;
            }

            max_wealth = java.lang.Math.max(curr_wealth, max_wealth);
        }

        return max_wealth;
    }
}

// class Solution {
//     public int maximumWealth(int[][] accounts) {
//         int max_wealth = 0;

//         for(int i = 0; i < accounts.length; i++){
//             // each customer
//             int curr_wealth = 0;

//             for(int j = 0; j < accounts[i].length; j++){
//                 // each customer account
//                 curr_wealth += accounts[i][j];
//             }

//             max_wealth = java.lang.Math.max(curr_wealth, max_wealth);
//         }
    
//     return max_wealth;
//     }
// }
