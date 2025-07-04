class Solution {
    // In place method
    // Time: O(n)
    // Space: O(1)
    public int removeElement(int[] nums, int val) {
        int lp = 0;
        int i = 0;

        while(lp < nums.length){
            if(nums[lp] != val){
                nums[i++] = nums[lp++];
            }

            else{
                lp++;
            }
        }
        return i;
    }
}

