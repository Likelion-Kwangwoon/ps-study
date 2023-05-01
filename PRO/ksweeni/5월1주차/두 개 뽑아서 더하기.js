function solution(numbers) {
    const arr= [];

    for(let i=0;i<numbers.length;i++){
        for(let j=i+1;j<numbers.length;j++){
            arr.push(numbers[i]+numbers[j]);
        }
    }
    const answer = [...new Set(arr)] // 중복이 제거된 집합
    return answer.sort((a,b) => { return a-b});
}