#include <vector>
#include <unordered_set>

using namespace std;

class Solution {
public:
    bool containsNearbyDuplicate(vector<int>& nums, int k) {
        unordered_set<int> window;
        int l = 0;
        
        for (int r = 0; r < nums.size(); r++) {
            // .count() returns 1 if the element is in the set, 0 otherwise
            if (window.count(nums[r])) {
                return true;
            } else {
                window.insert(nums[r]);
            }
            
            // Check if our window has exceeded the allowed distance
            if (r >= k) {
                window.erase(nums[l]);
                l++;
            }
        }
        
        return false;
    }
};