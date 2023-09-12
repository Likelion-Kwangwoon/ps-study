#include <iostream>
#include <vector>
using namespace std;

int N, x, y, d, g;
int map[101][101];
int dx[4]={0, -1, 0, 1};
int dy[4]={1, 0, -1, 0};
vector<pair<int, int>> curve;

void makeCurve(int idx){
    if(idx>g) return;
    else if(idx==0){
        map[y][x]=1;
        curve.push_back({y, x});
        int ny=y+dx[d];
        int nx=x+dy[d];
        map[ny][nx]=1;
        curve.push_back({ny, nx});
        makeCurve(1);
    }
    else{
        int cnt=curve.size();
        int cy=curve[cnt-1].first;
        int cx=curve[cnt-1].second;
        for(int i=cnt-2; i>=0; i--){
            int newY=curve[i].second-cx+cy;
            int newX=cy+cx-curve[i].first;
            if(newX>=0 && newY>=0 && newX<=100 && newY<=100){
                curve.push_back({newY, newX});
                map[newY][newX]=1;
            }
        }
        makeCurve(idx+1);
    }
}

bool findSquare(int j, int i){
    if(map[j][i]!=1) return false;
    if(map[j+1][i]!=1) return false;
    if(map[j][i+1]!=1) return false;
    if(map[j+1][i+1]!=1) return false;
    return true;
}

int main()
{
    cin>>N;
    for(int i=0; i<N; i++){
        cin>>x>>y>>d>>g;
        makeCurve(0);
        curve.clear();
    }
    
    int ans=0;
    for(int i=0; i<100; i++){
        for(int j=0; j<100; j++){
            if(findSquare(i, j)) ans++;
        }
    }
    cout<<ans;
}