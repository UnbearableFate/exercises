#include<iostream>
#include<vector>
#include<algorithm>
#include<stack>
using namespace std;

bool myfunc(vector<int>& a,vector<int>& b) {
    return a[0] < b[0];
}

class Solution {
public:
    vector<vector<int>> merge(vector<vector<int>>& intervals) {
        vector<vector<int>> res;
        vector<vector<int>> log;
        for(auto i : intervals) {
            log.push_back({i[0],0});
            log.push_back({i[1],1});
        }
        sort(log.begin(), log.end(),myfunc);
        stack<int> sta;
        for(auto l : log) {
            if(l[1] == 0) {
                sta.push(l[0]);
                continue;
            }
            if(l[1] == 1) {
                if (sta.size() == 1) {
                    res.push_back({sta.top(),l[0]});
                }
                sta.pop();
            }
        }
        return res;
    }bool myfunc(vector<int>& a,vector<int>& b) {
     return a[0] < b[0];
 }

};
