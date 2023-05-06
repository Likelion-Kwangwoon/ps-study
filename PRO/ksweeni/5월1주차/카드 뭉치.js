function solution(cards1, cards2, goal) {
    let temp = [];
    for(let i=0;i<goal.length;i++){
        if(cards1[0]===goal[i]){
            temp.push(cards1.shift());
        }
        else if(cards2[0] === goal[i]){
            temp.push(cards2.shift());
        }
    }
    if(JSON.stringify(temp) === JSON.stringify(goal)) return 'Yes';
    else return 'No';
}