#include <iostream>
#include <vector>
typedef long long ll;
using namespace std;


int solve(ll x, ll y){
    vector<bool> v(y-x+1, true);
    ll b=2; // basis
    
    while(b*b<=y){
        ll di=x/(b*b);
        if(x%(b*b)!=0) di++;
        
        while(di*(b*b)<=y){
            v[di*(b*b)-x]=false;
            di++;
        }
        b++;
    }
    
    int cnt=0;
    for(int i=0; i<=y-x; i++){
        if(v[i]) cnt++;
    }
    return cnt;
}

int main()
{
    ll x, y;
    cin>>x>>y;
    cout<<solve(x, y);
}