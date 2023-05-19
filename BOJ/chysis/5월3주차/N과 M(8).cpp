#include <iostream>
#include <algorithm>
using namespace std;

int M, N;
int set[8];
int ans[8];

void solve(int n, int cnt){
    if(cnt==M){
        for(int i=0; i<M; i++){
            cout<<ans[i]<<" ";
        }
        cout<<"\n";
        return;
    }
    else {
        for(int j=0; j<N; j++){
            if(set[j]>=n){
                ans[cnt]=set[j];
                solve(set[j], cnt+1);
            }
        }
    }
}

int main()
{
    cin>>N>>M;
    for(int i=0; i<N; i++){
        cin>>set[i];
    }
    sort(set, set+N);
    solve(0, 0);
}