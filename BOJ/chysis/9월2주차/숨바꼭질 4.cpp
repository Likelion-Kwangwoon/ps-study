#include <iostream>
#include <queue>
#include <vector>
using namespace std;

int N, K;
bool visited[100001];
int track[100001];
vector<int> ans;
queue<pair<int, int>> q;

void bfs(){
    while(!q.empty()){
        int now=q.front().first;
        int sec=q.front().second;
        q.pop();
        if(now==K){
            cout<<sec<<"\n";
            int idx=now;
            
            while(idx!=N){
                ans.push_back(idx);
                idx=track[idx];
            }
            ans.push_back(idx);
            for(int i=ans.size()-1; i>=0; i--){
                cout<<ans[i]<<" ";
            }
        }
        
        int move[3]={now-1, now+1, 2*now};
        for(int i=0; i<3; i++){
            int nx=move[i];
            if(nx>=0 && nx<=100000 && !visited[nx]){
                visited[nx]=true;
                q.push({nx, sec+1});
                track[nx]=now;
            }
        }
    }
}

int main()
{
    cin>>N>>K;
    visited[N]=true;
    q.push({N, 0});
    bfs();
}