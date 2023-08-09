#include <iostream>
#include <algorithm>
using namespace std;

int arr[1000001];
int lis[1000001];

int main()
{
    int N;
    cin>>N;
    for(int i=0; i<N; i++){
        cin>>arr[i];
    }
    
    int len=0;
    for(int i=0; i<N; i++){
        auto pos=lower_bound(lis, lis+len, arr[i]);
        *pos=arr[i];
        if(pos==lis+len) len++;
    }
    cout<<len;
}