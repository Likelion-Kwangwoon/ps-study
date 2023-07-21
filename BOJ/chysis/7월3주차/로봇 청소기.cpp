#include <iostream>
using namespace std;

int N, M, R, C, D;
int ans=0;
int map[51][51];
bool cleaned[51][51];
// 북동남서
int dx[4]={-1, 0, 1, 0};
int dy[4]={0, 1, 0, -1};

int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    
    cin>>N>>M>>R>>C>>D;
    for(int i=0; i<N; i++){
        for(int j=0; j<M; j++){
            cin>>map[i][j];
        }
    }
    
    while(true){
        if(!cleaned[R][C]){
            cleaned[R][C]=true;
            ans++;
        }
        
        bool flag=false;
        for(int i=0; i<4; i++){
            int nx=R+dx[i];
            int ny=C+dy[i];
            if(map[nx][ny]==0 && !cleaned[nx][ny] && nx>=0 && nx<N && ny>=0 && ny<M){
                flag=true;
                break;
            }
        }
        
        if(flag){
            D--;
            if(D<0) D=3;
            int nx=R+dx[D];
            int ny=C+dy[D];
            if(map[nx][ny]==0 && !cleaned[nx][ny] && nx>=0 && nx<N && ny>=0 && ny<M){
                R=nx;
                C=ny;
                continue;
            }
        }
        else{
            int nx=R-dx[D];
            int ny=C-dy[D];
            if(map[nx][ny]==0){
                R=nx;
                C=ny;
                continue;
            }
            else{
                break;
            }
        }
    }
    cout<<ans;
}