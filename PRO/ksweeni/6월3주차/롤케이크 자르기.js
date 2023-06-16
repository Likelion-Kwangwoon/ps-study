function solution(topping) {
    var answer = 0;
    if(topping.length===1) return answer;
    
    let topp=new Set();
    let sliceTopp=new Set();
    let counter=new Array(10001).fill(0);
    

    topping.map(v=>{
        topp.add(v);
        counter[v]++;
    })
    
    topping.map(v=>{
        if(counter[v]>=1){
            counter[v]--;
        }
        if(counter[v]===0){
            topp.delete(v);
        }    
        sliceTopp.add(v);    
        if(sliceTopp.size===topp.size) answer++;
    })
    
    return answer;
}