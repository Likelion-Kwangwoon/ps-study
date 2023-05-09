#include <iostream>
using namespace std;

int dp[501][501];

int main()
{
    int N;
    cin>>N;
    for(int i=0; i<N; i++){
        for(int j=0; j<i+1; j++){
            cin>>dp[i][j];
        }
    }
    for(int i=1; i<N; i++){
        for(int j=0; j<i+1; j++){
            if(j==0){
                dp[i][j]=dp[i][j]+dp[i-1][j];
            }
            else if(j==i){
                dp[i][j]=dp[i][j]+dp[i-1][j-1];
            }
            else{
                dp[i][j]=max(dp[i][j]+dp[i-1][j-1], dp[i][j]+dp[i-1][j]);
            }
        }
    }
    
    int ans=dp[N-1][0];
    for(int i=0; i<N; i++){
        if(ans<dp[N-1][i]) ans=dp[N-1][i];
    }
    cout<<ans;
}