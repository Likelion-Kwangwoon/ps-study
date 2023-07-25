#include <iostream>
#include <vector>
#include <algorithm>
#define INF 987654321
using namespace std;

int N, M;
int map[51][51];
int ans=INF;
vector<pair<int, int>> house;
vector<pair<int, int>> chicken;
vector<pair<int, int>> survive;
bool visited[51];

int distance(pair<int, int>& a, pair<int, int>& b){
    return abs(a.first-b.first)+abs(a.second-b.second);
}

void solve(int idx, int cnt){
    if(cnt==M){
        int temp=0;
        for(auto& h : house){
            int dist=INF;
            for(auto& c : survive){
                dist=min(dist, distance(h, c));
            }
            temp+=dist;
        }
        ans=min(ans, temp);
    }
    for(int i=idx; i<chicken.size(); i++){
        if(!visited[i]){
            visited[i]=true;
            survive.push_back(chicken[i]);
            solve(i, cnt+1);
            visited[i]=false;
            survive.pop_back();
        }
    }
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    
    cin>>N>>M;
    for(int i=0; i<N; i++){
        for(int j=0; j<N; j++){
            cin>>map[i][j];
            if(map[i][j]==1) house.push_back({i, j});
            else if(map[i][j]==2) chicken.push_back({i, j});
        }
    }
    solve(0, 0);
    cout<<ans;
}