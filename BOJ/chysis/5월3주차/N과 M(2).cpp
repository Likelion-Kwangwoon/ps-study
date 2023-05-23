#include <iostream>
using namespace std;

int N, M;
int arr[9];
bool visited[9];

void solve(int n, int c){
    if(c==M){
        for(int i=0; i<M; i++){
            cout<<arr[i]<<" ";
        }
        cout<<"\n";
        return;
    }
    for(int i=1; i<=N; i++){
        if(!visited[i] && n<i){
            visited[i]=true;
            arr[c]=i;
            solve(i, c+1);
            visited[i]=false;
        }
    }
}

int main()
{
    cin>>N>>M;
    solve(0, 0);
}