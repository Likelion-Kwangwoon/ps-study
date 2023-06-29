#include <iostream>
#define INF 987654321
using namespace std;

int arr[301][301];

int main()
{
    int N, M, T, u, v, h, s, e;
    cin>>N>>M>>T;
    
    for(int i=1; i<=N; i++){
        for(int j=1; j<=N; j++){
            if(i==j) continue;
            else arr[i][j]=INF;
        }
    }
    
    for(int i=0; i<M; i++){
        cin>>u>>v>>h;
        arr[u][v]=h;
    }
    
    for(int k=1; k<=N; k++){
        for(int i=1; i<=N; i++){
            for(int j=1; j<=N; j++){
                arr[i][j]=min(arr[i][j], max(arr[i][k], arr[k][j]));
            }
        }
    }
    
    for(int i=0; i<T; i++){
        cin>>s>>e;
        if(arr[s][e]!=INF)
            cout<<arr[s][e]<<"\n";
        else
            cout<<-1<<"\n";
    }
}