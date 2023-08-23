#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

int main()
{
    vector<string> v;
    int N;
    cin>>N;
    for(int i=0; i<N; i++){
        string str;
        cin>>str;
        v.push_back(str);
    }
    sort(v.begin(), v.end());
    int cnt=N;
    for(int i=1; i<N; i++){
        if(v[i].substr(0, v[i-1].length())==v[i-1]) cnt--;
    }
    cout<<cnt;
}