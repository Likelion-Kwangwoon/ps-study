const solution = (n, stations, w) => {
    let fiveG = 0, i = 0 , begin = 1;
    while(begin <= n){
        if(begin >= stations[i] - w && begin <= stations[i] + w){
            begin = stations[i] + w;
            i++;
        } else{
            begin += 2 * w;
            fiveG++;
        }
        begin++;
    }
    
    return fiveG;
}