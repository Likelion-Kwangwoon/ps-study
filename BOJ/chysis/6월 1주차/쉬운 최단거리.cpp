#include <iostream>
#include <queue>
using namespace std;

int dx[4]={-1, 1, 0, 0};
int dy[4]={0, 0, -1, 1};

int N, M;
int map[1001][1001];
int ans[1001][1001];
queue<pair<int, int>> q;

void bfs(){
    while(!q.empty()){
        pair<int, int> next = q.front();
        q.pop();
        
        for(int i=0; i<4; i++){
            int nx=next.first+dx[i];
            int ny=next.second+dy[i];
            
            if(nx>=0 && nx<N && ny>=0 && ny<M && ans[nx][ny]==-1 && map[nx][ny]==1){
                ans[nx][ny]=ans[next.first][next.second]+1;
                q.push({nx, ny});
            }
        }
    }
}

int main()
{
    cin>>N>>M;
    for(int i=0; i<N; i++){
        for(int j=0; j<M; j++){
            ans[i][j]=-1;
        }
    }
    
    for(int i=0; i<N; i++){
        for(int j=0; j<M; j++){
            cin>>map[i][j];
            if(map[i][j]==2){
                q.push({i, j});
                ans[i][j]=0;
            }
        }
    }
    bfs();
    for(int i=0; i<N; i++){
        for(int j=0; j<M; j++){
            if(map[i][j]==0) cout<<0<<" ";
            else cout<<ans[i][j]<<" ";
        }
        cout<<"\n";
    }
}