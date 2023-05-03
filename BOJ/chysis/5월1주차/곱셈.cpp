#include <iostream>
using namespace std;
typedef long long ll;

int main()
{
    ll A, B, C;
    cin>>A>>B>>C;
    
    ll ans=1;
    while(B){
        if(B&1){
            ans=(ans*A)%C;
        }
        A = ((A%C)*(A%C))%C;
        B/=2;
    }
    cout<<ans;
}