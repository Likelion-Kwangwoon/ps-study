#include <iostream>
#include <algorithm>
#define INF 987654321
using namespace std;

int W[101][101];

int main()
{
    int N, M, x, y;
    cin>>N>>M;
    for(int i=1; i<=N; i++){
        for(int j=1; j<=N; j++){
            if(i==j) W[i][j]=0;
            else W[i][j]=INF;
        }
    }
    for(int i=1; i<=M; i++){
        cin>>x>>y;
        W[x][y]=1;
        W[y][x]=1;
    }
    for(int k=1; k<=N; k++){
        for(int i=1; i<=N; i++){
            for(int j=1; j<=N; j++){
                W[i][j]=min(W[i][j], W[i][k]+W[k][j]);
            }
        }
    }
    int minSum=INF;
    int ans;
    for(int i=1; i<=N; i++){
        int sum=0;
        for(int j=1; j<=N; j++){
            if(W[i][j]==INF) W[i][j]=0;
            else{
                sum+=W[i][j];
            }
        }
        if(minSum>sum) {minSum=sum; ans=i;}
    }
    cout<<ans;
}