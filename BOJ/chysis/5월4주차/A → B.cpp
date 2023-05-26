#include <iostream>
#include <queue>
using namespace std;
typedef long long ll;

ll A, B;
queue<pair<ll, ll>> q;

int bfs(int start){
    while(!q.empty()){
        pair<ll, ll> next = q.front();
        if(next.first==B){
            return next.second+1;
        }
        q.pop();
        if(next.first*2<=B)
            q.push(make_pair(next.first*2, next.second+1));
        if(next.first*10+1<=B)
            q.push(make_pair(next.first*10+1, next.second+1));
    }
    return -1;
}

int main()
{
    cin>>A>>B;
    q.push(make_pair(A, 0));
    cout<<bfs(A);
}