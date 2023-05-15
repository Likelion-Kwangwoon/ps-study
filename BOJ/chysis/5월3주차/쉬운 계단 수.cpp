#include <iostream>
using namespace std;
#define MOD 1000000000

int main()
{
    int N;
    cin>>N;
    int DP[101][10]={0, 1, 1, 1, 1, 1, 1, 1, 1, 1, };

    for(int i=1; i<N; i++){
        for(int j=0; j<10; j++){
            if(j==0) DP[i][j]=DP[i-1][j+1]%MOD;
            else if(j==9) DP[i][j]=DP[i-1][j-1]%MOD;
            else DP[i][j]=(DP[i-1][j-1]+DP[i-1][j+1])%MOD;
        }
    }
    long long ans=0;
    for(int i=0; i<10; i++){
        ans+=DP[N-1][i]%MOD;
    }
    cout<<ans%MOD;
}