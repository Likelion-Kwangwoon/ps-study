#include <iostream>
#include <vector>
using namespace std;

int main()
{
    int N;
    cin>>N;
    if(N==0 || N==1){
        cout<<N;
        return 0;
    }
    vector<int> v;
    while(N!=0 && N!=1){
        if(N%-2==-1){
            N=(N/-2)+1;
            v.push_back(1);
        }
        else{
            v.push_back(N%-2);
            N/=-2;
        }
    }
    if(N==1) v.push_back(1);
    for(int i=v.size()-1; i>=0; i--){
        cout<<v[i];
    }
}