#include <iostream>
using namespace std;

int main()
{
    int N;
    cin>>N;
    int dp[1001][10]={1, 1, 1, 1, 1, 1, 1, 1, 1, 1,};
    for(int i=1; i<N; i++){
        for(int j=0; j<10; j++){
            dp[i][j]=dp[i-1][j];
        }
        for(int j=1; j<10; j++){
            dp[i][j]+=dp[i][j-1]%10007;
        }
    }
    int ans=0;
    for(int i=0; i<10; i++){
        ans+=dp[N-1][i]%10007;
    }
    cout<<ans%10007;
}