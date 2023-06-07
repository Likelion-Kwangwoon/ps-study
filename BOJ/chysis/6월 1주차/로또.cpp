#include <iostream>
using namespace std;

int K;
int arr[13];
int ans[6];
bool visited[13];

void lotto(int num, int cnt){
    if(cnt==6){
        for(int i=0; i<6; i++){
            cout<<ans[i]<<" ";
        }
        cout<<"\n";
        return;
    }
    for(int i=0; i<K; i++){
        if(!visited[i]){
            visited[i]=true;
            if(arr[i]>num){
                ans[cnt]=arr[i];
                lotto(ans[cnt], cnt+1);
            }
            visited[i]=false;
        }
    }
}

int main(){
    while(true){
        cin>>K;
        if(K==0) break;
        for(int i=0; i<K; i++){
            cin>>arr[i];
        }
        lotto(0, 0);
        cout<<"\n";
    }
}