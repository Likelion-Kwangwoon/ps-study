#include <iostream>
#include <algorithm>
using namespace std;

int DP[1001][1001];

int main()
{
    int ans=0;
    int N,M;
    char c;
    cin>>N>>M;
    for(int i=0; i<N; i++){
        for(int j=0; j<M; j++){
            cin>>c;
            DP[i][j]=c-'0';
            if(DP[i][j]==1) ans=1; 
        }
    }
    for(int i=0; i<N; i++){
        for(int j=0; j<M; j++){
            if(DP[i][j]){
                if(i>0 && j>0){
                    DP[i][j]=min(min(DP[i-1][j], DP[i][j-1]), DP[i-1][j-1])+1;
                }
            }
            ans=max(ans, DP[i][j]);
        }
    }
    cout<<ans*ans;
}