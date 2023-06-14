function solution(numbers) {
    var answer = [];
    for(let i = 0;i<numbers.length;i++){
        if(numbers[i]%2===0){
            answer.push(numbers[i]+1);
        }
        else{
            let str = '0'+numbers[i].toString(2);
            const index = str.lastIndexOf('01');
            str = str.substring(0,index) + '10' + str.substring(index+2, str.length);
            answer.push(parseInt(str,2))
            
        }
    }
    return answer;
}