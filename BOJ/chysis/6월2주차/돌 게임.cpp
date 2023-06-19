#include <iostream>
#include <algorithm>
using namespace std;

int DP[1001];

int main()
{
    int N;
    cin>>N;
    DP[0]=0;
    DP[1]=1;
    DP[2]=2;
    for(int i=3; i<=N; i++){
        DP[i]=min(DP[i-1], DP[i-3])+1;
    }
    if(DP[N]%2==0) cout<<"CY";
    else cout<<"SK";
}