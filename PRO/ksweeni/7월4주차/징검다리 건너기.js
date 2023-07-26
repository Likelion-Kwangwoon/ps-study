const binarySearch = (stones, mid, k) => {
    let cnt = 0;
    for(let i = 0; i < stones.length; i++){
        if(stones[i] - mid <= 0) cnt++;
        else cnt = 0;
        
        if(cnt >= k) return true;
    }
    return false;
}

function solution(stones, k) {
    let start = 0;
    let end = 200000000;
    while(start <= end){
        let mid = Math.floor((start + end) /2);
        if(binarySearch(stones,mid,k)) end = mid - 1;
        else start = mid+1; 
        }
    return start;
}