class Solution {
public:
    int max_m(int a, int b)
    {
        return a >b ?a:b;
    }
    int min_m(int a, int b)
    {
        return a <b ?a:b;
    }

    int maxProfit(vector<int>& prices) {
        if(!prices.size())
            return 0;
        int max_pro = 0, min_pri = prices[0];
        for(int i=1;i<prices.size();i++){
            min_pri = min_m(min_pri, prices[i-1]);
            max_pro = max_m(max_pro, prices[i] - min_pri);
        }
        return max_pro;
    }
};
