#include <iostream>
using namespace std;

int DP[1001];

int main()
{
    int N;
    cin>>N;
    DP[1]=1;
    DP[2]=2;
    DP[3]=1;
    DP[4]=1;
    DP[5]=1;
    for(int i=6; i<=N; i++){
        if(DP[i-1]==2 || DP[i-3]==2 || DP[i-4]==2) DP[i]=1;
        else DP[i]=2;
    }
    if(DP[N]==2) cout<<"CY";
    else cout<<"SK";
}