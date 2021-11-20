
#include <string>
using namespace std;

class Solution {
public:
    string replaceSpace(string s) {
        while(string::npos != s.find(' ')){
            int i = s.find(' ');
            s.replace(i,1, "%20");
        }
        return s;
    }
};