#include <iostream>
#define INF 987654321
using namespace std;

int arr[51][51];
int candi[51];

int main()
{
    int N, a, b;
    cin>>N;
    for(int i=1; i<=N; i++){
        for(int j=1; j<=N; j++){
            if(i==j) arr[i][j]=0;
            else arr[i][j]=INF;
        }
    }
    while(true){
        cin>>a>>b;
        if(a==-1 && b==-1) break;
        arr[a][b]=1;
        arr[b][a]=1;
    }
    for(int k=1; k<=N; k++){
        for(int i=1; i<=N; i++){
            for(int j=1; j<=N; j++){
                arr[i][j]=min(arr[i][j], arr[i][k]+arr[k][j]);
            }
        }
    }
    int sco=INF;
    int cnt=0;
    for(int i=1; i<=N; i++){
        int temp=-1;
        for(int j=1; j<=N; j++){
            temp=max(temp, arr[i][j]);
        }
        candi[i]=temp;
        sco=min(sco, candi[i]);
    }
    for(int i=1; i<=N; i++){
        if(sco==candi[i]) cnt++;
    }
    cout<<sco<<" "<<cnt<<"\n";
    for(int i=1; i<=N; i++){
        if(sco==candi[i]) cout<<i<<" ";
    }
}