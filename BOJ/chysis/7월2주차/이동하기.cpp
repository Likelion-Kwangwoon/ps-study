#include <iostream>
using namespace std;

int arr[1001][1001];

int main()
{
    int N, M;
    cin>>N>>M;
    for(int i=0; i<N; i++){
        for(int j=0; j<M; j++){
            cin>>arr[i][j];
        }
    }
    for(int i=0; i<N; i++){
        for(int j=0; j<M; j++){
            if(i-1>=0 && j-1>=0){
                arr[i][j]+=max(max(arr[i-1][j], arr[i][j-1]), arr[i-1][j-1]);
            }
            else if(i-1>=0 && j-1<0){
                arr[i][j]+=arr[i-1][j];
            }
            else{
                arr[i][j]+=arr[i][j-1];
            }
        }
    }
    cout<<arr[N-1][M-1];
}