#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int arr[1000001];
int lis[1000001];
int elem[1000001];

void backtrack(int idx, int num){
    if(idx==0) return;
    if(elem[idx]==num){
        backtrack(idx-1, num-1);
        cout<<arr[idx]<<" ";
    }
    else{
        backtrack(idx-1, num);
    }
}

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);
    
    int N;
    cin>>N;
    for(int i=1; i<=N; i++){
        cin>>arr[i];
    }
    
    int len=0;
    for(int i=1; i<=N; i++){
        auto pos=lower_bound(lis+1, lis+len+1, arr[i]);
        *pos=arr[i];
        elem[i]=pos-lis;
        if(pos==lis+len+1) {
            len++;
        }
    }
    cout<<len<<"\n";
    backtrack(N, len);
}