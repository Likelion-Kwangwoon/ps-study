function solution(bridge_length, weight, truck_weights) {
    var answer = 0;
    let bridge = Array.from({length : bridge_length},()=>0);
    let weightsum = 0
    
    answer++;
    bridge.shift();
    weightsum += truck_weights[0];
    bridge.push(truck_weights.shift());
    
    while(weightsum > 0){
        answer++;
        weightsum -= bridge.shift();
        if(truck_weights.length > 0 && weightsum+truck_weights[0] <= weight){
            weightsum += truck_weights[0];
            bridge.push(truck_weights.shift());
        } else bridge.push(0);
    }
    return answer;
}