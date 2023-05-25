function solution(babbling) {
    const can = ['aya','ye','woo','ma'];
    let count = 0;
    
    for(let i = 0; i < babbling.length; i++){
        let b = babbling[i];
        
        for(let j = 0; j < can.length; j++){
            if(b.includes(can[j].repeat(2))){
                break;
            }
            
            b = b.split(can[j]).join(" ");
        }
        
        if(b.split(" ").join("").length === 0){
            count += 1;
        }
    }
    
    return count;
}