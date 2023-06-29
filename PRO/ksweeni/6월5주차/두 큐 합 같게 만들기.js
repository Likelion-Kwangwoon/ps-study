function getSum(arr) {
    return arr.reduce((acc, cur) => acc + cur, 0);
  }
  
  function solution(queue1, queue2) {
      var count = 0;
      var target = [...queue1, ...queue2]
      let begin = 0;
      let end = queue1.length;
      
      let headSum = getSum(target.slice(begin,end));
      let sum = getSum(target)/2;
      while(count < target.length*2 && headSum!==sum){
          if(headSum < sum){
              headSum+=target[end++];
              //end++;
          } else{
              headSum-=target[begin++];
              //begin++;
          }
          count++;
      }
      if(headSum !== sum) return -1;
      return count;
  }