#include <iostream>
#define INF 987654321
using namespace std;

int arr[1001][1001];

int main()
{
    int N, M, X, a, b, c;
    cin>>N>>M>>X;
    for(int i=1; i<=N; i++){
        for(int j=1; j<=N; j++){
            if(i==j) arr[i][j]=0;
            else arr[i][j]=INF;
        }
    }
    
    for(int i=0; i<M; i++){
        cin>>a>>b>>c;
        arr[a][b]=c;
    }
    
    for(int k=1; k<=N; k++){
        for(int i=1; i<=N; i++){
            for(int j=1; j<=N; j++){
                arr[i][j]=min(arr[i][j], arr[i][k]+arr[k][j]);
            }
        }
    }
    
    for(int i=1; i<=N; i++){
        for(int j=1; j<=N; j++){
            if(arr[i][j]==INF){
                arr[i][j]=0;
            }
        }
    }
    
    int ans=-1;
    for(int i=1; i<=N; i++){
        if(i==X) continue;
        int tmp=arr[i][X]+arr[X][i];
        ans=max(ans, tmp);
    }
    cout<<ans;
}