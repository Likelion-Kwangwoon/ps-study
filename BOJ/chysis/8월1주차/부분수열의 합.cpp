#include <iostream>
using namespace std;

int N;
int arr[21];
int ans[21];
bool visited[21];
bool calc[100000*20+1];

void solve(int cnt, int idx){
    int sum=0;
    for(int i=0; i<cnt; i++){
        sum+=ans[i];
    }
    calc[sum]=true;
    
    for(int i=idx; i<N; i++){
        if(!visited[i]){
            visited[i]=true;
            ans[cnt]=arr[i];
            solve(cnt+1, i);
            visited[i]=false;
        }
    }
}

int main()
{
    cin>>N;
    for(int i=0; i<N; i++){
        cin>>arr[i];
        calc[arr[i]]=true;
    }
    solve(0, 0);
    for(int i=1; i<=100000*20; i++){
        if(!calc[i]){
            cout<<i;
            break;
        }
    }
}