#include <iostream>
using namespace std;

int main()
{
    int C, N;
    cin>>C;
    for(int i=0; i<C; i++){
        cin>>N;
        double sum=0;
        double cnt=0;
        int arr[1001];
        for(int j=0; j<N; j++){
            cin>>arr[j];
            sum+=arr[j];
        }
        for(int j=0; j<N; j++){
            if(arr[j]>sum/N) cnt++;
        }
        cout<<fixed;
        cout.precision(3);
        cout<<cnt/N*100<<"%\n";
    }
}