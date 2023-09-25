#include <iostream>
#include <algorithm>
#define INF 987654321
using namespace std;

int zone[101];
int adj[101][101];
int point[101];

int main()
{
    for(int i=1; i<=100; i++){
        for(int j=1; j<=100; j++){
            adj[i][j]=INF;
            if(i==j) adj[i][j]=0;
        }
    }
    
    int N, M, R, A, B, L;
    cin>>N>>M>>R;
    for(int i=1; i<=N; i++){
        cin>>zone[i];
    }
    for(int i=0; i<R; i++){
        cin>>A>>B>>L;
        adj[A][B]=L;
        adj[B][A]=L;
    }
    
    for(int k=1; k<=N; k++){
        for(int i=1; i<=N; i++){
            for(int j=1; j<=N; j++){
                adj[i][j]=min(adj[i][j], adj[i][k]+adj[k][j]);
            }
        }
    }

    int ans=-1;
    for(int i=1; i<=N; i++){
        point[i]+=zone[i];
        for(int j=1; j<=N; j++){
            if(i==j) continue;
            if(adj[i][j]<=M) point[i]+=zone[j];
        }
        ans=max(ans, point[i]);
    }
    cout<<ans;
}