function solution(priorities, location) {
    var answer = 0;
    let q = [];
    let max = Math.max.apply(null, priorities);
   
    for(let i = 0;i<priorities.length;i++){
        q.push(i)
    }

    while(priorities.length != 0){
        if(priorities[0] < max){
            priorities.push(priorities.shift());
            q.push(q.shift());
        }else {   // priorities[0] >= max
            answer+=1;
            priorities.shift();
            if(q.shift() == location)
                return answer;
            max = Math.max(...priorities);
        }
    }
 
    return answer;
}