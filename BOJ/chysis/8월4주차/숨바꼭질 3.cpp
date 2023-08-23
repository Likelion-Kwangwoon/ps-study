#include <iostream>
#include <queue>
using namespace std;

queue<pair<int, int>> q;
bool visited[100001];

void bfs(int target){
    while(!q.empty()){
        int cur=q.front().first;
        int cnt=q.front().second;
        q.pop();
        if(cur==target){
            cout<<cnt;
            return;
        }
        
        if(2*cur<=100000 && !visited[2*cur]){
            q.push({2*cur, cnt});
            visited[2*cur]=true;
        }
        
        if(cur-1>=0 && !visited[cur-1]){
            q.push({cur-1, cnt+1});
            visited[cur-1]=true;
        }
        
        if(cur+1<=100000 && !visited[cur+1]){
            q.push({cur+1, cnt+1});
            visited[cur+1]=true;
        }
    }
}

int main()
{
    int N, K;
    cin>>N>>K;
    q.push({N, 0});
    visited[N]=true;
    bfs(K);
}