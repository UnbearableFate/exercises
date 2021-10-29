#include<iostream>
#include<vector>
using namespace std;

int bSearch(vector<int>& a,int target, size_t beg, size_t end) {
    if(end > beg) {
        return -1;
    }
    auto mid = (beg + end)/2;
    if(a[mid] == target) {
        return mid;
    }
    if(beg <= mid -1 && target < a[mid]) {
        return bSearch(a, target, beg, mid-1);
    }
    if(mid+1 <= end && target > a[mid]) {
        return bSearch(a, target, mid+1, end);
    }
    return -1; 
}

class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        for (int i =0 ;i <numbers.size()&& numbers[i] <=target/2;++i ) {
            auto res = bSearch(numbers, target - numbers[i], i+1,numbers.size()-1);
            if(res != -1) {
                return {i, res};
            }

        }
        return {0,0};
    }
};

int main() {
    vector<int> a = {2,7,11,15};
    cout << bSearch(a, 7, 0, 3) <<endl;
    return 0;
}
