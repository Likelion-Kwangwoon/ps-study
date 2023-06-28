#include <iostream>
#include <cmath>
using namespace std;

int T[16];
int P[16];
int DP[16];

int main()
{
    int N;
    cin>>N;
    for(int i=1; i<=N; i++){
        cin>>T[i]>>P[i];
        DP[i]=P[i];
    }
    for(int i=1; i<=N; i++){
        for(int j=1; j<=i; j++){
            if(i+T[i]<=N+1){
                if(j+T[j]<=i){
                    DP[i]=max(DP[j]+P[i], DP[i]);
                }
            }
            else{
                DP[i]=0;
            }
        }
    }
    int ans=0;
    for(int i=1; i<=N; i++){
        ans=max(ans, DP[i]);
    }
    cout<<ans;
}