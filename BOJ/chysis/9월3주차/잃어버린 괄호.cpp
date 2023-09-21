#include <iostream>
#include <vector>
#include <string>
using namespace std;

vector<int> v;

int main()
{
    bool plus=false;
    string str;
    cin>>str;
    int idx=0;
    int temp=0;
    while(idx<=str.length()){
        if(str[idx]-'0'>=0 && str[idx]-'0'<=9){
            temp=temp*10+str[idx]-'0';
        }
        else{
            if(plus){
                int num=v.back()+temp;
                v.pop_back();
                v.push_back(num);
                temp=0;
                plus=false;
            }
            else{
                v.push_back(temp);
                temp=0;
            }
            
            if(str[idx]=='+') plus=true;
        }
        idx++;
    }
    if(plus){
        int num=v.back()+temp;
        v.pop_back();
        v.push_back(num);
        temp=1;
        plus=false;
    }
    
    int ans=v[0];
    for(int i=1; i<v.size(); i++){
        ans-=v[i];
    }
    cout<<ans;
}