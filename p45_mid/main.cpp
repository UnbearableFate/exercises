#include <vector>
#include <iostream>
using namespace std;
class Solution
{
public:
    int jump(vector<int> &nums)
    {
        if (nums.size() <= 1)
        {
            return 0;
        }
        int start = 0;
        int end = nums[0];
        int time = 1;
        int maxJump = nums[0];
        if (end >= nums.size() - 1)
        {
            return 1;
        }
        while (true)
        {
            ++time;
            for (int i = start; i <= end; ++i)
            {
                maxJump = max(maxJump, i + nums[i]);
            }
            if (maxJump >= nums.size() - 1)
            {
                return time;
            }
            else
            {
                start = end;
                end = maxJump;
                if (end >= nums.size() - 1)
                {
                    return time + 1;
                }
            }
        }
        return time;
    }
};

int main()
{
    auto ss = Solution();
    vector<int> test = {1, 1, 1, 1, 1};
    cout << ss.jump(test) << endl;
}