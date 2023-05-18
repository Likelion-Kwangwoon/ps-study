#include <iostream>
using namespace std;

int N, M;
int arr[9];
bool visited[9];

void solve(int c){
    if(c==M){
        for(int i=0; i<M; i++){
            cout<<arr[i]<<" ";
        }
        cout<<"\n";
        return;
    }
    for(int i=0; i<N; i++){
        if(!visited[i]){
            visited[i]=true;
            arr[c]=i+1;
            solve(c+1);
            visited[i]=false;
        }
    }
}

int main()
{
    cin>>N>>M;
    solve(0);
}