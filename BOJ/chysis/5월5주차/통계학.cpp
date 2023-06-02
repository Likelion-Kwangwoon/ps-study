#include <iostream>
#include <algorithm>
#include <cmath>
using namespace std;

int arr[500001];
int num[8001];

int main()
{
    int N;
    double sum;
    double mean;
    bool ok=true;
    cin>>N;
    for(int i=0; i<N; i++){
        cin>>arr[i];
        sum+=arr[i];
        num[(int)arr[i]+4000]++;
    }
    sort(arr, arr+N);
    int freq=-1;
    int ans;
    for(int i=0; i<8001; i++){
        if(num[i]>0){
            if(freq<num[i]) {
                freq=num[i];
                ans=i-4000;
                ok=true;
            }
            else if(freq==num[i] && ok){
                ans=i-4000;
                ok=false;
            }
        }
    }
    mean=sum/N;
    cout<<(round(mean)==0 ? 0 : round(mean))<<"\n";
    cout<<arr[N/2]<<"\n";
    cout<<ans<<"\n";
    cout<<arr[N-1]-arr[0];
}