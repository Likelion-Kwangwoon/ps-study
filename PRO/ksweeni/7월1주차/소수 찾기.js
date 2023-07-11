function isPrime(n) {
    if (n <= 1) {
      return false;
    }
    for (let i = 2; i <= Math.sqrt(n); i++) {
      if (n % i === 0) {
        return false;
      }
    }
    return true;
  }
  
  function solution(numbers) {
      let count = 0;
      numbers = numbers.split('');

      var set = new Set();
      permutation(numbers,"");
      
      function permutation(num,str){
      if(str.length > 0){
          if(!set.has(Number(str))){
              set.add(Number(str))
              if(isPrime(Number(str))) count++;
          }
      }
          if(num.length > 0){
              for(var i = 0 ; i < num.length; i++){
                  var s = num.slice(0);
                  s.splice(i,1)
                  //console.log('slicing',t,str+num[i])
                  permutation(s,str+num[i]);
              }
          }
      }
      return count;
  }