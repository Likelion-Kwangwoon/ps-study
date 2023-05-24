#include <iostream>
#include <algorithm>
using namespace std;

int DP[101][100001];
int wei[101];
int pri[101];

int main()
{
    int N, K;
    cin>>N>>K;
    for(int i=1; i<=N; i++){
        cin>>wei[i]>>pri[i];
    }

    for(int i=0; i<=N; i++){
        for(int w=0; w<=K; w++){
            if(i==0 || w==0){
                DP[i][w]=0;
            }
            else if(wei[i]<=w){
                DP[i][w]=max(DP[i-1][w], DP[i-1][w-wei[i]]+pri[i]);   
            }
            else{
                DP[i][w]=DP[i-1][w];
            }
        }
    }
    cout<<DP[N][K];
}