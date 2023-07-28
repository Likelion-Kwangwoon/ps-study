#include <iostream>
#include <queue>
using namespace std;

int N, M;
int cnt=0;
int dx[4]={-1, 1, 0, 0};
int dy[4]={0, 0, -1, 1};
queue<pair<int, int>> q;
char campus[610][610];
bool visited[610][610];

void bfs(){
    while(!q.empty()){
        int x=q.front().first;
        int y=q.front().second;
        q.pop();
        for(int i=0; i<4; i++){
            int nx=x+dx[i];
            int ny=y+dy[i];
            if(nx>=0 && nx<N && ny>=0 && ny<M && campus[nx][ny]!='X' && !visited[nx][ny]){
                q.push({nx, ny});
                visited[nx][ny]=true;
                if(campus[nx][ny]=='P') cnt++;
            }
        }
    }
}

int main()
{
    char c;
    cin>>N>>M;
    for(int i=0; i<N; i++){
        for(int j=0; j<M; j++){
            cin>>c;
            campus[i][j]=c;
            if(c=='I'){
                q.push({i, j});
                visited[i][j]=true;
            }
        }
    }
    bfs();
    if(cnt==0) cout<<"TT";
    else cout<<cnt;
}