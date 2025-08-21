class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        # Time: O(m + n)
        # Space: O(1)
        
        n1p = m - 1         # Pointer to nums1 largest element
        n2p = n - 1         # Pointer to nums2 largest element
        merge_pointer = m + n - 1  # Pointer to nums1 where we need to insert largest element
        
        # Merge in reverse order
        while n2p >= 0:
            if n1p >= 0 and nums1[n1p] > nums2[n2p]:
                nums1[merge_pointer] = nums1[n1p]
                n1p -= 1
            else:
                nums1[merge_pointer] = nums2[n2p]
                n2p -= 1
            
            merge_pointer -= 1
