#include <iostream>
#include <algorithm>
using namespace std;

int N, M;
int set[9];
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
            arr[c]=set[i];
            solve(c+1);
            visited[i]=false;
        }
    }
}

int main()
{
    int num;
    cin>>N>>M;
    for(int i=0; i<N; i++){
        cin>>set[i];
    }
    sort(set, set+N);
    solve(0);
}