#include <iostream>
#include <queue>
#include <tuple>
using namespace std;

int M,N,H;
queue<tuple<int, int, int>> q;
int box[101][101][101];
int dx[6]={-1, 1, 0, 0, 0, 0};
int dy[6]={0, 0, -1, 1, 0, 0};
int dz[6]={0, 0, 0, 0, 1, -1};

void bfs(){
    while(!q.empty()){
        int zz=get<0>(q.front());
        int xx=get<1>(q.front());
        int yy=get<2>(q.front());
        q.pop();
        
        for(int i=0; i<6; i++){
            int nx=xx+dx[i];
            int ny=yy+dy[i];
            int nz=zz+dz[i];
            
            if(nx>=0 && nx<N && ny>=0 && ny<M && nz>=0 && nz<H && box[nz][nx][ny]==0){
                box[nz][nx][ny]=box[zz][xx][yy]+1;
                q.push(make_tuple(nz, nx, ny));
            }
        }
    }
}

int main()
{
    cin>>M>>N>>H;
    for(int i=0; i<H; i++){
        for(int j=0; j<N; j++){
            for(int k=0; k<M; k++){
                cin>>box[i][j][k];
                if(box[i][j][k]==1){
                    q.push(make_tuple(i, j, k));
                }
            }
        }
    }
    bfs();
    int max=-2;
    for(int i=0; i<H; i++){
        for(int j=0; j<N; j++){
            for(int k=0; k<M; k++){
                if(box[i][j][k]==0){
                    cout<<-1;
                    return 0;
                }
                if(max<box[i][j][k])
                    max=box[i][j][k];
            }
        }
    }
    cout<<max-1;
}