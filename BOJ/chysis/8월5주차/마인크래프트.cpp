#include <iostream>
using namespace std;

int map[501][501];

int main()
{
    int N, M, B;
    cin>>N>>M>>B;
    for(int i=0; i<N; i++){
        for(int j=0; j<M; j++){
            cin>>map[i][j];
        }
    }
    
    int ans=987654321;
    int height=0;
    for(int i=0; i<=256; i++){
        int add=0;
        int del=0;
        for(int j=0; j<N; j++){
            for(int k=0; k<M; k++){
                int diff=i-map[j][k];
                if(diff<0) del+=(-diff);
                else if(diff>0) add+=diff;
            }
        }
        if(del+B>=add){
            int temp=del*2+add;
            if(temp<=ans){
                ans=temp;
                height=i;
            }
        }
    }
    cout<<ans<<" "<<height;
}