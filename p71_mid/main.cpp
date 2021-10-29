#include <iostream>
#include <string>
#include <vector>
using namespace std;
class Solution
{
public:
    string simplifyPath(string path)
    {
        vector<string> clearPath;
        auto li = split(path, "/");
        for (auto dir : li)
        {
            if (dir == ".")
            {
                continue;
            }
            if (dir == "..")
            {
                if (!clearPath.empty())
                {
                    clearPath.erase(clearPath.end() - 1);
                }
                continue;
            }
            clearPath.push_back(dir);
        }
        string res;
        for (auto i : clearPath)
        {
            res += ("/"+i);
        }
        if (res.size() == 0) {
            return "/";
        }
        return res;
    }

    vector<string> split(string s, string delimiter)
    {
        size_t pos_start = 0, pos_end, delim_len = delimiter.length();
        string token;
        vector<string> res;

        while ((pos_end = s.find(delimiter, pos_start)) != string::npos)
        {
            token = s.substr(pos_start, pos_end - pos_start);
            pos_start = pos_end + delim_len;
            if (token != "")
            {
                res.push_back(token);
            }
        }
        if (s.substr(pos_start) != "")
        {

            res.push_back(s.substr(pos_start));
        }
        return res;
    }
};

int main()
{
    auto ss = Solution();
    cout << ss.simplifyPath("/a/./b/../../c/") <<endl;
}