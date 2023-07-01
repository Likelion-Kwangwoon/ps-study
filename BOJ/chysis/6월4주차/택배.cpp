#include <iostream>
#include <algorithm>
#define INF 987654321
using namespace std;

int arr[201][201];
int P[201][201];

int main()
{
    int N, M, a, b, c;
    cin>>N>>M;
    for(int i=0; i<=N; i++){
        for(int j=0; j<=N; j++){
            if(i!=j) arr[i][j]=INF;
        }
    }
    for(int i=0; i<M; i++){
        cin>>a>>b>>c;
        arr[a][b]=c;
        P[a][b]=b;
        arr[b][a]=c;
        P[b][a]=a;
    }
    
    for(int k=1; k<=N; k++){
        for(int i=1; i<=N; i++){
            for(int j=1; j<=N; j++){
                if(arr[i][j]>arr[i][k]+arr[k][j]){
                    arr[i][j]=arr[i][k]+arr[k][j];
                    P[i][j]=P[i][k];
                }
            }
        }
    }
    
    for(int i=1; i<=N; i++){
        for(int j=1; j<=N; j++){
            if(P[i][j]==0) cout<<"- ";
            else cout<<P[i][j]<<" ";
        }
        cout<<"\n";
    }
}