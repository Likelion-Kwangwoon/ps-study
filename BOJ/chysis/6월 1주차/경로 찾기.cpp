#include <iostream>
#include <algorithm>
#define INF 987654321
using namespace std;

int W[101][101];

int main()
{
    int N;
    cin>>N;
    for(int i=0; i<N; i++){
        for(int j=0; j<N; j++){
            cin>>W[i][j];
            if(W[i][j]==0) W[i][j]=INF;
        }
    }
    
    for(int k=0; k<N; k++){
        for(int i=0; i<N; i++){
            for(int j=0; j<N; j++){
                W[i][j]=min(W[i][j], W[i][k]+W[k][j]);
            }
        }
    }
    for(int i=0; i<N; i++){
        for(int j=0; j<N; j++){
            if(W[i][j]!=INF && W[i][j]!=0)
                cout<<1<<" ";
            else cout<<0<<" ";
        }
        cout<<"\n";
    }
}