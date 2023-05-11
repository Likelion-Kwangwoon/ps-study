#include <iostream>
using namespace std;

long long dp[1000001];

int main()
{
    int T, N;
    cin>>T;
    dp[0]=1;
    dp[1]=1;
    dp[2]=2;
    for(int i=3; i<=1000001; i++){
        dp[i]=(dp[i-1]+dp[i-2]+dp[i-3])%1000000009;
    }
    for(int i=0; i<T; i++){
        cin>>N;
        cout<<dp[N]<<"\n";
    }
}