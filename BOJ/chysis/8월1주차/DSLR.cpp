#include <iostream>
#include <string>
#include <queue>
using namespace std;

int T, A, B;
bool visited[10001];

void bfs(int start, int target){
    queue<pair<int, string>> q;
    q.push({start, ""});
    for(auto &a:visited) a=false;
    visited[start]=true;
    
    while(!q.empty()){
        int num=q.front().first;
        string cmd=q.front().second;
        q.pop();
        
        if(num==target){
            cout<<cmd<<"\n";
            break;
        }
        
        int D=(2*num)%10000;
        int S=num==0 ? 9999 : num-1;
        int L=(num%1000)*10+num/1000;
        int R=(num%10)*1000+num/10;
        
        if(!visited[D]) {q.push({D, cmd+"D"}); visited[D]=true;}
        if(!visited[S]) {q.push({S, cmd+"S"}); visited[S]=true;}
        if(!visited[L]) {q.push({L, cmd+"L"}); visited[L]=true;}
        if(!visited[R]) {q.push({R, cmd+"R"}); visited[R]=true;}
    }
}

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    
    cin>>T;
    while(T--){
        cin>>A>>B;
        bfs(A, B);
    }
}