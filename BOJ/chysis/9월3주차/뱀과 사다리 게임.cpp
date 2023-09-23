#include <iostream>
#include <queue>
using namespace std;

int ans=987654321;
int ladder[101];
int snake[101];
bool visited[101];
queue<pair<int, int>> q;

int bfs(){
    while(!q.empty()){
        int cur=q.front().first;
        int cnt=q.front().second;
        q.pop();
        if(cur==100) return cnt;
        
        for(int i=1; i<=6; i++){
            if(cur+i>100) break;
            if(visited[cur+i]) continue;
            
            if(ladder[cur+i]){
                if(visited[ladder[cur+i]]) continue;
                q.push({ladder[cur+i], cnt+1});
                visited[cur+i]=true;
                visited[ladder[cur+i]]=true;
            }
            else if(snake[cur+i]){
                if(visited[snake[cur+i]]) continue;
                q.push({snake[cur+i], cnt+1});
                visited[cur+i]=true;
                visited[snake[cur+i]]=true;
            }
            else{
                q.push({cur+i, cnt+1});
                visited[cur+i]=true;
            }
        }
    }
    return 0;
}

int main()
{
    int N, M, x, y;
    cin>>N>>M;
    for(int i=0; i<N; i++){
        cin>>x>>y;
        ladder[x]=y;
    }
    for(int i=0; i<M; i++){
        cin>>x>>y;
        snake[x]=y;
    }
    q.push({1, 0});
    cout<<bfs();
}