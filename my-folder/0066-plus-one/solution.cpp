class Solution {
public:
    vector<int> plusOne(vector<int>& digits) {
        // Reverse Traversal
        // Time: O(n)
        // Space: O(1) because .insert is considered to be in-place storage 

        int i = digits.size() - 1; 
        
        while(i >= 0){
            // Check for an overflow
            if(digits[i] == 9){
                digits[i] = 0;
                i--;

            }

            // Else the element is able to be incremented without an overflow, return result.
            else{
                digits[i] += 1;
                return digits;
            }
        } 
        // If we made have overflows the entire time I.E array = [9,9,9]
        // We need to pre-append a 1. Such that [9,9,9] becomes [1,0,0,0]
        digits.insert(digits.begin(), 1);

        return digits;
    }
};
