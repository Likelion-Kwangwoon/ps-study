#include <iostream>
#include <algorithm>
using namespace std;

int N, M;
int ans[8];
int sets[8];

void solve(int num, int cnt){
    if(cnt==M){
        for(int i=0; i<M; i++){
            cout<<ans[i]<<" ";
        }
        cout<<"\n";
        return;
    }
    int prev=-1;
    for(int i=0; i<N; i++){
        if(sets[i]>=num && prev!=sets[i]){
            ans[cnt]=sets[i];
            prev=ans[cnt];
            solve(ans[cnt], cnt+1);
        }
    }
}

int main()
{
    cin>>N>>M;
    for(int i=0; i<N; i++){
        cin>>sets[i];
    }
    sort(sets, sets+N);
    solve(0, 0);
}