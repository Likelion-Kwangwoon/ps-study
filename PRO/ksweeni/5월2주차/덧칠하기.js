function solution(n, m, section) {
    let answer = 0;
    let max = 0;
    // 배열 객체 내부를 순환하며 max를 변경, answer 증가
    section.forEach((sec) => {
      if (sec > max) {
        max = sec + m - 1;
        answer++;
      }
    });
    return answer;
  }