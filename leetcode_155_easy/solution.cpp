#include<vector>
using namespace std;
class MinStack {
public:
    vector<int> value;
    void myswap(size_t a, size_t b) {
        auto temp = value[a];
        value[a] = value[b];
        value[b] = temp;
    }

    void keepMin(size_t pos) {
        while(pos > 0) {
            auto parent = (pos -1)/2;
            if (value[parent] >= value[pos]) {
                myswap(pos, parent);
                pos = parent;
            } else {
                break;
            }
        }
    }
    /** initialize your data structure here. */
    MinStack() {
        
    }
    
    void push(int x) {
        value.push_back(x);
        auto pos = value.size()-1;
        keepMin(pos);
    }
    
    void pop() {
        value[0] = value[value.size()-1];
        value.erase(value.end()-1);
        auto pos = 0;
        while(pos < value.size()) {
            auto l = 2*pos +1;
            auto r = 2*pos +2;
            if(l< value.size() && value[l] < value[pos]) {
                myswap(pos,l);
                pos = l;
                continue;
            }
            if(r< value.size() && value[r] < value[pos]) {
                myswap(pos,r);
                pos = r;
                continue;
            }
            break;
        }
    }
    
    int top() {
       return value[0]; 
    }
    
    int getMin() {
        
    }
};
