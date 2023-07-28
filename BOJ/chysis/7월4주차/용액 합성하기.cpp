#include <iostream>
#include <algorithm>
using namespace std;

int N;
int arr[100001];

int main()
{
    cin>>N;
    for(int i=0; i<N; i++){
        cin>>arr[i];
    }
    sort(arr, arr+N);
    int s=0, e=N-1, best=arr[s]+arr[e];
    while(s<e){
        int temp=arr[s]+arr[e];
        
        if(abs(temp)<abs(best)){
            best=temp;
        }
        
        if(temp<0){
            s++;
        }
        else if(temp>0){
            e--;
        }
        else{
            break;
        }
    }
    cout<<best;
}