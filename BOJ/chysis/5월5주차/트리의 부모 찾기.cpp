#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

vector<int> v[100001];
bool visited[100001];
int ans[100001]; // 부모 노드 저장장

void dfs(int start, int parent){
    visited[start]=true;
    ans[start]=parent;
    for(int i=0; i<v[start].size(); i++){
        if(!visited[v[start][i]]){
            dfs(v[start][i], start);
        }
    }
}

int main()
{
    int N, a, b;
    cin>>N;
    for(int i=0; i<N-1; i++){
        cin>>a>>b;
        v[a].push_back(b);
        v[b].push_back(a);
    }
    for(int i=1; i<=N; i++){
        sort(v[i].begin(), v[i].end());
    }
    dfs(1, 1);
    for(int i=2; i<=N; i++){
        cout<<ans[i]<<"\n";
    }
}