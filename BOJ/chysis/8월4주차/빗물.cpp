#include <iostream>
using namespace std;

int arr[501][501];

int main()
{
    int H, W, N;
    cin>>H>>W;
    for(int i=0; i<W; i++){
        cin>>N;
        for(int j=1; j<=N; j++){
            arr[H-j][i]=1;
        }
    }
    int ans=0;
    for(int i=0; i<H; i++){
        int one=-1, two=-1;
        for(int j=0; j<W; j++){
            if(arr[i][j]==1){
                if(one==-1) one=j;
                else if(two==-1){
                    two=j;
                    ans+=two-one-1;
                    one=two;
                    two=-1;
                }
            }
        }
    }
    cout<<ans;
}