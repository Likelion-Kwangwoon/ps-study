function solution(fees, records) {
    const car_info = {}; // 딕셔너리 선언
    records.forEach(r => {
        let [time, car, state] = r.split(' ');
        let [h, m] = time.split(':');
        time = (h * 1) * 60 + (m*1); // 시간을 분으로 환산
        if (!car_info[car]) car_info[car] = 0;
        if (state === 'IN') car_info[car] += (1439 - time);
        if (state === 'OUT') car_info[car] -= (1439 - time);
    });
    const answer = [];
    for (let [car, time] of Object.entries(car_info)) { // 딕셔너리 내부 객체 순환
        if (time <= fees[0]) time = fees[1];
        else time = Math.ceil((time - fees[0]) / fees[2]) * fees[3] + fees[1]
        answer.push([car, time]);
    }
    return answer.sort((a, b) => a[0] - b[0]).map(v => v[1]);
}