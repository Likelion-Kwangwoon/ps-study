#include <iostream>
#include <queue>
using namespace std;

int F, S, G, U, D;
int ans=-1;
queue<pair<int, int>> q;
bool visited[1000001];

void bfs(int target){
    while(!q.empty()){
        int stair=q.front().first;
        int count=q.front().second;
        q.pop();
        if(stair==G){
            ans=count;
            return;
        }
         
        if(stair+U<=F && !visited[stair+U]){
            q.push({stair+U, count+1});
            visited[stair+U]=true;
        }
        if(stair-D>=1 && !visited[stair-D]){
            q.push({stair-D, count+1});
            visited[stair-D]=true;
        }
    }
}

int main() {
    cin>>F>>S>>G>>U>>D;
    if(S==G) {
        cout<<0;
        return 0;
    }
    q.push({S, 0});
    visited[S]=true;
    bfs(G);
    if(ans==-1){
        cout<<"use the stairs\n";
    }
    else{
        cout<<ans<<'\n';
    }
}