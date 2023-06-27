#include <iostream>
#include <cmath>
#define INF 987654321
using namespace std;

int arr[301][301];
int L[301];
int R[301];

int main()
{
    int N;
    cin>>N;
    for(int i=0; i<N; i++){
        for(int j=0; j<N; j++){
            if(i!=j) arr[i][j]=INF;
        }
    }
    for(int i=0; i<N; i++){
        cin>>L[i]>>R[i];
    }
    for(int i=0; i<N; i++){
        for(int j=0; j<N; j++){
            if(i==j){
                arr[i][j]=0;
                continue;
            }
            if(R[i]>=L[j] && R[j]>=L[i]){
                arr[i][j]=1;
                arr[j][i]=1;
            }
        }
    }
    for(int k=0; k<N; k++){
        for(int i=0; i<N; i++){
            for(int j=0; j<N; j++){
                arr[i][j]=min(arr[i][j], arr[i][k]+arr[k][j]);
            }
        }
    }
    for(int i=0; i<N; i++){
        for(int j=0; j<N; j++){
            if(arr[i][j]==INF) arr[i][j]=0;
        }
    }
    
    int Q, A, B;
    cin>>Q;
    for(int i=0; i<Q; i++){
        cin>>A>>B;
        if(arr[A-1][B-1]!=0) cout<<arr[A-1][B-1]<<"\n";
        else cout<<-1<<"\n";
    }
}