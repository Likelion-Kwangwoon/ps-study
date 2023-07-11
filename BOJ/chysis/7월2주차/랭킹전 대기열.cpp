#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

bool comp(pair<int, string>& a, pair<int, string>& b){
    return a.second<b.second;
}

int main(){
    int p, m, l;
    string s;
    cin>>p>>m;
    vector<pair<int, string>> player;
    vector<vector<pair<int, string>>> rooms;
    for(int i=0; i<p; i++){
        cin>>l>>s;
        player.push_back({l, s});
    }
    
    for(int i=0; i<player.size(); i++){
        int roomNum=rooms.size();
        bool flag=false;
        
        if(roomNum>0){
            for(int j=0; j<roomNum; j++){
                if(abs(player[i].first-rooms[j][0].first)<=10 && rooms[j].size()<m){
                    rooms[j].push_back(player[i]);
                    flag=true;
                    break;
                }
            }
        }
        if(!flag){
            vector<pair<int, string>> temp;
            temp.push_back(player[i]);
            rooms.push_back(temp);
        }
    }
    for(int i=0; i<rooms.size(); i++){
        sort(rooms[i].begin(), rooms[i].end(), comp);
        if(rooms[i].size()==m){
            cout<<"Started!\n";
            for(int j=0; j<rooms[i].size(); j++){
                cout<<rooms[i][j].first<<" "<<rooms[i][j].second<<"\n";
            }
        }
        else{
            cout<<"Waiting!\n";
            for(int j=0; j<rooms[i].size(); j++){
                cout<<rooms[i][j].first<<" "<<rooms[i][j].second<<"\n";
            }
        }
    }
}