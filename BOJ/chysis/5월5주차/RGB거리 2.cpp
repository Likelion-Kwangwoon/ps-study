#include <iostream>
#include <algorithm>
#define INF 987654321;
using namespace std;

int arr[1001][3];
int DP[1001][3];

int main()
{
    int N, ans;
    cin>>N;
    for(int i=0; i<N; i++){
        for(int j=0; j<3; j++){
            cin>>arr[i][j];
        }
    }

    DP[0][0]=arr[0][0];
    DP[0][1]=INF;
    DP[0][2]=INF;
    
    for(int i=1; i<N; i++){
        DP[i][0]=min(DP[i-1][1], DP[i-1][2])+arr[i][0];
        DP[i][1]=min(DP[i-1][0], DP[i-1][2])+arr[i][1];
        DP[i][2]=min(DP[i-1][0], DP[i-1][1])+arr[i][2];
    }
    ans=min(DP[N-1][1], DP[N-1][2]);
    
    DP[0][1]=arr[0][1];
    DP[0][0]=INF;
    DP[0][2]=INF;
    
    for(int i=1; i<N; i++){
        DP[i][0]=min(DP[i-1][1], DP[i-1][2])+arr[i][0];
        DP[i][1]=min(DP[i-1][0], DP[i-1][2])+arr[i][1];
        DP[i][2]=min(DP[i-1][0], DP[i-1][1])+arr[i][2];
    }
    ans=min(ans, min(DP[N-1][0], DP[N-1][2]));
    
    DP[0][2]=arr[0][2];
    DP[0][0]=INF;
    DP[0][1]=INF;
    
    for(int i=1; i<N; i++){
        DP[i][0]=min(DP[i-1][1], DP[i-1][2])+arr[i][0];
        DP[i][1]=min(DP[i-1][0], DP[i-1][2])+arr[i][1];
        DP[i][2]=min(DP[i-1][0], DP[i-1][1])+arr[i][2];
    }
    ans=min(ans, min(DP[N-1][0], DP[N-1][1]));
    cout<<ans;
}