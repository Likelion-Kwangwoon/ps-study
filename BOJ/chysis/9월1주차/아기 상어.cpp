#include <iostream>
#include <queue>
#include <vector>
#include <memory.h>
using namespace std;

int N;
int sharkSize=2, xp=0;
int ans=0;
int curX, curY;
int map[21][21];
bool visited[21][21];
int dx[4]={-1, 1, 0, 0};
int dy[4]={0, 0, -1, 1};
queue<pair<pair<int, int>, int>> q;
vector<pair<pair<int, int>, int>> v;

void moveShark(int x, int y, int dist){
    map[curX][curY]=0;
    map[x][y]=9;
    curX=x;
    curY=y;
    ans+=dist;
    xp++;
    if(xp==sharkSize){
        sharkSize++;
        xp=0;
    }
}

int bfs(int x, int y){
    while(!q.empty()){
        auto f=q.front();
        q.pop();
        if(f.first==make_pair(x, y)) return f.second;
        
        for(int i=0; i<4; i++){
            int nx=f.first.first+dx[i];
            int ny=f.first.second+dy[i];
            
            if(nx>=0 && ny>=0 && nx<N && ny<N && map[nx][ny]<=sharkSize && !visited[nx][ny]){
                q.push({{nx, ny}, f.second+1});
                visited[nx][ny]=true;
            }
        }
    }
    return -1;
}

void solve(){
    int temp=0;
    for(int i=0; i<N; i++){
        for(int j=0; j<N; j++){
            if(map[i][j]!=0 && map[i][j]!=9 && map[i][j]<sharkSize){
                temp++;
                
                memset(visited, false, sizeof(visited));
                while(!q.empty()) q.pop();
                
                for(int k=0; k<N; k++){
                    for(int l=0; l<N; l++){
                        if(map[k][l]!=9 && map[k][l]>sharkSize) visited[k][l]=true;
                    }
                }
                q.push({{curX, curY}, 0});
                visited[curX][curY]=true;
                int shortest=bfs(i, j);
                if(shortest==-1){
                    temp--;
                    continue;
                }
                else{
                    v.push_back({{i, j}, shortest});
                }
            }
        }
    }
    
    if(temp==0) return;
    else if(temp==1) moveShark(v[0].first.first, v[0].first.second, v[0].second);
    else if(temp>=2){
        int tarX, tarY, tarD=987654321;
        for(int i=0; i<v.size(); i++){
            if(v[i].second<tarD){
                tarX=v[i].first.first;
                tarY=v[i].first.second;
                tarD=v[i].second;
            }
        }
        moveShark(tarX, tarY, tarD);
    }
}

bool gameContinue(){
    for(int i=0; i<N; i++){
        for(int j=0; j<N; j++){
            memset(visited, false, sizeof(visited));
            while(!q.empty()) q.pop();
            
            q.push({{curX, curY}, 0});
            visited[curX][curY]=true;
            if(map[i][j]!=0 && map[i][j]!=9 && map[i][j]<sharkSize)
                if(bfs(i, j)!=-1) return true;
        }
    }
    return false;
}

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    
    cin>>N;
    for(int i=0; i<N; i++){
        for(int j=0; j<N; j++){
            cin>>map[i][j];
            if(map[i][j]==9){
                curX=i;
                curY=j;
            }
        }
    }
    
    while(true){
        if(!gameContinue()) break;
        
        solve();
        v.clear();
    }
    cout<<ans;
}