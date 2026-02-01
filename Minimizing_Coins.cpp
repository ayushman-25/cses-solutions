#include <bits/stdc++.h>
using namespace std;

int main() {
    int n, x;
    cin >> n >> x;
    vector<int> c(n);
    for (int &ci: c) {
        cin >> ci;
    }
    vector<long long> dp(x + 1, 1LL << 60);
    dp[0] = 0LL;
    for (int i = 1; i <= x; i++) {
        vector<long long> chck;
        for (int j: c) {
            if (i >= j) {
                chck.push_back(dp[i - j] + 1LL);
            }
        }
        long long val = 1LL << 60;
        if ((int)chck.size()) {
            val = *min_element(chck.begin(), chck.end());
        }
        dp[i] = min(dp[i], val);
    }
    if (dp[x] != 1LL << 60) {
        cout << dp[x];
    } else {
        cout << -1;
    }
}