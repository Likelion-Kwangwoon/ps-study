function solution(polynomial) {
    const pol = polynomial.split(" + ");
    let x_num = 0;
    let num = 0;
    let answer = [];
    
    pol.forEach((v) => {
      if (v.includes("x")) {
        const valtoNum = v.replace("x", "") || "1";
        x_num += parseInt(valtoNum, 10);
      } else {
        num += Number(v);
      }
    });
  
    if (x_num) answer.push(`${x_num === 1 ? "" : x_num}x`);
    if (num) answer.push(num);
    return answer.join(" + ");
  }