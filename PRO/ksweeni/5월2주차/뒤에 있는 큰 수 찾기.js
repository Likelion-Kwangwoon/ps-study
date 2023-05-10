function solution(numbers) {
    
    let arr = new Array(numbers.length).fill(-1);
    let stack = [];
    
    for(let i=0; i<numbers.length;i++){
        let num = numbers[i];
        while(stack && numbers[stack.at(-1)]<numbers[i]){
            arr[stack.pop()] = num
           
        }
        stack.push(i);
    }
    
    return arr;
}