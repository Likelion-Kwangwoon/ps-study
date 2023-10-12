#include <iostream>
#include <vector>
#include <string.h>
#include <algorithm>
using namespace std;

int N, num;
int ans=-1, tem=0;
int graph[101];
bool visited[101];
bool matched[101];
vector<int> elem;
vector<int> temp;

void dfs(int start){
    visited[start]=true;
    int next=graph[start];
    
    if(!visited[next]){
        dfs(next);
    } else if(!matched[next]){
        for(int i=next; i!=start; i=graph[i]){
            tem++;
            temp.push_back(i);
        }
        tem++;
        temp.push_back(start);
    }
    matched[start]=true;
}

int main()
{
    cin>>N;
    for(int i=1; i<=N; i++){
        cin>>graph[i];
    }
    
    for(int i=1; i<=N; i++){
        for(int j=1; j<=N; j++){
            if(matched[j]) continue;
            dfs(j);
        }
        
        if(tem>ans){
            ans=tem;
            elem.clear();
            for(int j=0; j<temp.size(); j++){
                elem.push_back(temp[j]);
            }
        }
        tem=0;
        memset(visited, false, sizeof(visited));
        memset(matched, false, sizeof(matched));
        temp.clear();
    }
    
    cout<<ans<<"\n";
    sort(elem.begin(), elem.end());
    for(int i=0; i<elem.size(); i++){
        cout<<elem[i]<<"\n";
    }
}