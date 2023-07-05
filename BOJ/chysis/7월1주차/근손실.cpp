#include <iostream>
using namespace std;

int N, K;
int res=0;
int arr[9];
int ans[9];
bool visited[9];

bool promising(int cnt){
    bool flag=true;
    int start=500;
    for(int i=0; i<cnt; i++){
        start+=arr[ans[i]];
        start-=K;
        if(start<500) flag=false;
    }
    return flag;
}

void solve(int cnt){
    if(cnt==N){
        res++;
        return;
    }
    for(int i=0; i<N; i++){
        if(!visited[i]){
            visited[i]=true;
            if(promising(cnt)){
                ans[cnt]=i;
                solve(cnt+1);
            }
            visited[i]=false;
        }
    }
}

int main()
{
    cin>>N>>K;
    for(int i=0; i<N; i++){
        cin>>arr[i];
    }
    solve(0);
    cout<<res;
}