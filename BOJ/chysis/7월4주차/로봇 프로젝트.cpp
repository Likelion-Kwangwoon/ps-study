#include <iostream>
#include <algorithm>
using namespace std;

int X, N;
int lego[1000001];

bool binsearch(int target){
    int s=0, e=N-1;
    while(s<=e){
        int m=(s+e)/2;
        
        if(lego[m]>target){
            e=m-1;
        }
        else if(lego[m]<target){
            s=m+1;
        }
        else{
            return true;
        }
    }
    return false;
}

int main()
{
    while(cin>>X){
        cin>>N;
        for(int i=0; i<N; i++){
            cin>>lego[i];
        }
        sort(lego, lego+N);
        X*=10000000;
        
        bool flag=false;
        for(int i=0; i<N; i++){
            int block=lego[i];
            int other=X-lego[i];
            if(block>other) continue;
            if(other==block && lego[i+1]!=other) continue;
            if(binsearch(other)){
                cout<<"yes "<<block<<" "<<other<<"\n";
                flag=true;
                break;
            }
        }
        if(!flag) cout<<"danger\n";
    }
}