#include <iostream>
using namespace std;

int N, M;
int arr[8];
bool visited[8];

void solve(int c){
    if(c==M){
        for(int i=0; i<M; i++){
            cout<<arr[i]<<" ";
        }
        cout<<"\n";
        return;
    }
    for(int i=1; i<=N; i++){
        arr[c]=i;
        solve(c+1);
    }
}

int main()
{
    cin>>N>>M;
    solve(0);
}