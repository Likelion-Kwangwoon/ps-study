#include <iostream>
#include <queue>
using namespace std;

int box[1001][1001];
queue<pair<int, int>> q;
int dx[4]={-1, 1, 0, 0};
int dy[4]={0, 0, -1, 1};
int M,N;

bool check(){
    for(int i=0; i<N; i++)
        for(int j=0; j<M; j++)
            if(box[i][j]==0)
                return false;
    return true;
}

void bfs(){
    while(!q.empty()){
        pair<int, int> next=q.front();
        q.pop();
        
        for(int i=0; i<4; i++){
            int nx=next.first+dx[i];
            int ny=next.second+dy[i];
            
            if(nx>=0 && nx<N && ny>=0 && ny<M && box[nx][ny]==0){
                box[nx][ny]=box[next.first][next.second]+1;
                q.push(make_pair(nx, ny));
            }
        }
    }
}

int main()
{
    cin>>M>>N;
    for(int i=0; i<N; i++){
        for(int j=0; j<M; j++){
            cin>>box[i][j];
            if(box[i][j]==1){
                q.push(make_pair(i, j));
            }
        }
    }
    bfs();
    int max=-2;
    for(int i=0; i<N; i++){
        for(int j=0; j<M; j++){
            if(box[i][j]==0){
                cout<<-1;
                return 0;
            }
            if(max<box[i][j])
                max=box[i][j];
        }
    }
    cout<<max-1;
}
