function solution(record) {
    const info = {};
    var answer = [];
    record.forEach(r => {
        let [op,id,name] = r.split(' ');
        if(op === 'Enter' || op === 'Change') info[id]= name;
    });
    for (let i=0;i<record.length;i++){
        record[i] = record[i].split(' ')
        if(record[i][0] === "Enter") answer.push(info[record[i][1]]+"님이 들어왔습니다.");
        else if(record[i][0] === "Leave") answer.push(info[record[i][1]]+"님이 나갔습니다.");
    }
    return answer;
}