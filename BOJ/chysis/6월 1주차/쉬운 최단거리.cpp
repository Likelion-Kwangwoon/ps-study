#include <iostream>
#include <queue>
using namespace std;

int dx[4]={-1, 1, 0, 0};
int dy[4]={0, 0, -1, 1};

int N, M;
int map[1001][1001];
queue<pair<int, int>> q;

void bfs(int x, int y){
    while(!q.empty()){
        pair<int, int> next = q.front();
        q.pop();
        
        for(int i=0; i<4; i++){
            int nx=next.first+dx[i];
            int ny=next.second+dy[i];
            
            if(nx>=0 && nx<N && ny>=0 && ny<M && map[nx][ny]==1){
                map[nx][ny]=map[next.first][next.second]+1;
                q.push({nx, ny});
            }
        }
    }
}

int main()
{
    int x, y;
    cin>>N>>M;
    for(int i=0; i<N; i++){
        for(int j=0; j<M; j++){
            cin>>map[i][j];
            if(map[i][j]==2){
                x=i; y=j;
                q.push({x, y});
                map[i][j]=0;
            }
        }
    }   
    bfs(x, y);
    for(int i=0; i<N; i++){
        for(int j=0; j<M; j++){
            cout<<map[i][j]<<" ";
        }
        cout<<"\n";
    }
}