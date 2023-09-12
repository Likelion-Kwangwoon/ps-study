#include <iostream>
#include <algorithm>
using namespace std;

int ans=0;
int map[4][4];
pair<pair<int, int>, int> fish[17];
int dx[8]={-1, -1, 0, 1, 1, 1, 0, -1};
int dy[8]={0, -1, -1, -1, 0, 1, 1, 1};

bool isValid(int x, int y){
    if(x>=0 && x<4 && y>=0 && y<4) return true;
    return false;
}

void solve(int map[4][4], pair<pair<int, int>, int> fish[17], int x, int y, int dir, int sum){
    int tempMap[4][4];
    pair<pair<int, int>, int> tempFish[17];
    
    for(int i=0; i<4; i++){
        for(int j=0; j<4; j++){
            tempMap[i][j]=map[i][j];
        }
    }
    for(int i=1; i<=16; i++){
        tempFish[i]=fish[i];
    }
    
    int curIdx=tempMap[x][y];
    dir=tempFish[curIdx].second;
    sum+=curIdx;
    ans=max(ans, sum);
    tempFish[curIdx].second=-1;
    tempMap[x][y]=0;
    
    for(int i=1; i<=16; i++){
        if(tempFish[i].second==-1) continue;
        
        for(int d=0; d<8; d++){
            int nextDir=(tempFish[i].second+d)%8;
            int nextX=tempFish[i].first.first+dx[nextDir];
            int nextY=tempFish[i].first.second+dy[nextDir];
            if(isValid(nextX, nextY) && !(nextX==x && nextY==y)){
                if(tempMap[nextX][nextY]!=0){
                    // 물고기랑 자리 교체 
                    int temp=tempMap[nextX][nextY];
                    tempMap[nextX][nextY]=i;
                    tempMap[tempFish[i].first.first][tempFish[i].first.second]=temp;
                    tempFish[temp].first=tempFish[i].first;
                    
                    tempFish[i].first={nextX, nextY};
                    tempFish[i].second=nextDir;
                }
                else{
                    // 빈 칸으로 이동
                    tempMap[nextX][nextY]=i;
                    tempMap[tempFish[i].first.first][tempFish[i].first.second]=0;
                    tempFish[i].first={nextX, nextY};
                    tempFish[i].second=nextDir;
                }
                break;
            }
        }  
    }
    
    for(int i=1; i<=3; i++){
        int nextX=x+dx[dir]*i;
        int nextY=y+dy[dir]*i;
        if(isValid(nextX, nextY)){
            if(tempMap[nextX][nextY]!=0 && tempFish[tempMap[nextX][nextY]].second!=-1){
                solve(tempMap, tempFish, nextX, nextY, dir, sum);
            }
        }
    }
}

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    
    int a, b;
    for(int i=0; i<4; i++){
        for(int j=0; j<4; j++){
            cin>>a>>b;
            map[i][j]=a;
            fish[a]={{i, j}, b-1};
        }
    }
    solve(map, fish, 0, 0, fish[map[0][0]].second, 0);
    cout<<ans;
}