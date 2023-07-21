function phone(key) {
    let ph = [[1, 2, 3], [4, 5, 6], [7, 8, 9], ['*', 0, '#']];
    for (let i = 0; i < 4; i++) {
        for (let j = 0; j < 3; j++) {
            if (ph[i][j] === key) {
                return [i, j];
            }
        }
    }
}

function solution(numbers, hand) {
const right = [3, 6, 9];
const left = [1, 4, 7];
var answer = '';
var lhand = '*';
var rhand = '#';
numbers.forEach((v => {
    if (right.includes(v)){
        answer+='R';
        rhand = v;
    }
    else if (left.includes(v)){
        answer+='L';
        lhand = v;
    }
    else{
        let r = phone(rhand);
        let l = phone(lhand);
        let now = phone(v);
        let rd = Math.abs(r[0] - now[0]) + Math.abs(r[1] - now[1]);
        let ld = Math.abs(l[0] - now[0]) + Math.abs(l[1] - now[1]);
        if( rd === ld) {
            hand === "right" ? (answer+='R', rhand = v) : (answer+='L', lhand = v)
        }else if(rd > ld) {
            answer += 'L';
            lhand = v;
        }else { 
            answer += 'R';
            rhand = v;
        }
    }
}))
return answer;
}