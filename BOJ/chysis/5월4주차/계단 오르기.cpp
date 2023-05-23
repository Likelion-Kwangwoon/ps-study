#include <iostream>
#include <algorithm>
using namespace std;

int stairs[301];
int DP[301];

int main()
{
    int N;
    cin>>N;
    for(int i=0; i<N; i++){
        cin>>stairs[i];
    }
    DP[0]=stairs[0];
    DP[1]=stairs[0]+stairs[1];
    DP[2]=max(stairs[1], DP[0])+stairs[2];
    for(int i=3; i<N; i++){
        DP[i]=max(DP[i-2], DP[i-3]+stairs[i-1])+stairs[i];
    }
    cout<<DP[N-1];
}