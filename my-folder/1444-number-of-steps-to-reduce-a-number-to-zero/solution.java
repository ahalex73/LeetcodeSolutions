class Solution {
    // BitWise solution
    public int numberOfSteps(int num) {
        int steps = 0;
        int bitMask = 1;

        while(num > 0){
            if((num & bitMask) == 0){
                num = num >> 1;
            }
            else{
                num -= 1;
            }


            steps += 1;
        }
        

        return steps;
    }
}


// class Solution {
//     public int numberOfSteps(int num) {
//         int steps = 0;

//         while(num > 0){
//             boolean isEven = num % 2 == 0;

//             if (isEven){
//                 num = num / 2;
//             }

//             else{
//                 num -= 1;
//             }

//             steps += 1;
//         }

//         return steps;
//     }
// }
