#include <iostream>
using namespace std;

int N, M;
int arr[501][501];
bool visited[501];
int ans=0;
int main()
{
    int a, b;
    cin>>N>>M;
    for(int i=0; i<M; i++){
        cin>>a>>b;
        arr[a][b]=1;
        arr[b][a]=1;
    }
    visited[1]=true;
    for(int i=1; i<=N; i++){
        if(arr[1][i]==1 && !visited[i]){
            visited[i]=true;
            ans++;
            for(int j=1; j<=N; j++){
                if(arr[i][j]==1 && !visited[j] && !arr[1][j]){
                    visited[j]=true;
                    ans++;
                }
            }
        }
    }
    cout<<ans;
}