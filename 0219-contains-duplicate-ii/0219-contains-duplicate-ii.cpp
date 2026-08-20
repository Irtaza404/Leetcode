#include <vector>
#include <unordered_set>

using namespace std;

class Solution {
public:
    bool containsNearbyDuplicate(vector<int>& nums, int k) {
        // Edge case: if k is 0, distance must be 0, which means no distinct indices can match
        if (k == 0) return false; 
        
        unordered_set<int> window;
        
        // OPTIMIZATION 1: Pre-allocate memory. 
        // This stops the set from pausing to resize and rehash memory as it grows.
        window.reserve(k + 1); 
        
        for (int r = 0; r < nums.size(); r++) {
            
            // Check if we need to shrink FIRST, so we don't exceed size K
            if (r > k) {
                window.erase(nums[r - k - 1]);
            }
            
            // OPTIMIZATION 2: The '.insert()' trick.
            // window.insert() actually returns a pair. The second value is a boolean 
            // that is 'false' if the item was ALREADY in the set.
            // Doing it this way means C++ only has to calculate the hash ONCE per number, 
            // instead of calculating it once for .count() and again for .insert().
            if (!window.insert(nums[r]).second) {
                return true;
            }
        }
        
        return false;
    }
};