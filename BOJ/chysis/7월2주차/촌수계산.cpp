#include <iostream>
using namespace std;

int N, A, B, M, X, Y;
int ans=-1;
int adj[101][101];
bool visited[101];

void dfs(int node, int cnt){
    visited[node]=true;
    if(node==B){
        ans=cnt;
    }
    for(int i=1; i<=N; i++){
        if(adj[node][i] && !visited[i]){
            dfs(i, cnt+1);
        }
    }
}

int main()
{
    cin>>N>>A>>B>>M;
    for(int i=0; i<M; i++){
        cin>>X>>Y;
        adj[X][Y]=1;
        adj[Y][X]=1;
    }
    dfs(A, 0);
    cout<<ans;
}