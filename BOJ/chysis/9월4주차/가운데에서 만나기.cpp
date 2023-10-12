#include <iostream>
#include <vector>
#include <algorithm>

#define INF 987654321
using namespace std;

int adj[201][201];
int home[201];
vector<int> ans;

int main()
{
    for(int i=1; i<=200; i++){
        for(int j=1; j<=200; j++){
            if(i==j) adj[i][j]=0;
            else adj[i][j]=INF;
        }
    }
    
    int N, M, A, B, T, K;
    cin>>N>>M;
    for(int i=0; i<M; i++){
        cin>>A>>B>>T;
        adj[A][B]=T;
    }
    cin>>K;
    for(int i=0; i<K; i++){
        cin>>home[i];
    }
    
    for(int k=1; k<=N; k++){
        for(int i=1; i<=N; i++){
            for(int j=1; j<=N; j++){
                adj[i][j]=min(adj[i][j], adj[i][k]+adj[k][j]);
            }
        }
    }
    
    for(int i=1; i<=N; i++){
        for(int j=1; j<=N; j++){
            if(adj[i][j]==INF) adj[i][j]=0;
        }
    }
    
    int minDist=INF;
    for(int i=1; i<=N; i++){
        int temp=-1;
        for(int j=0; j<K; j++){
            temp=max(temp, adj[home[j]][i]+adj[i][home[j]]);
        }
        if(minDist>temp){
            minDist=temp;
            ans.clear();
            ans.push_back(i);
        }
        else if(minDist==temp) ans.push_back(i);
    }
    
    for(auto i: ans) cout<<i<<" ";
}