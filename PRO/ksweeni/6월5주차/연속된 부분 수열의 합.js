function sorting(a,b){
    const diff = Math.abs(a[1]-a[0]) - Math.abs(b[1]-b[0]);
    if(diff === 0) return a[0] - b[0];
    else return diff;
}

function solution(sequence, k) {
  let left = 0;
  let right = 0;
  let sum = sequence[0];
    
  const answer = [];

  while (right < sequence.length) {
    if (sum < k) {
      right++;
      sum += sequence[right];
    } else if (sum > k) {
      sum -= sequence[left];
      left++;
    } else {
      answer.push([left, right]);
      right++; 
      sum += sequence[right];
    }
  }

    return answer.sort(sorting)[0];
}