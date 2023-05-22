function solution(word) {
    const result = [];
    const words = "";
  
    const dfs = (word, length, result) => {
        const alpha = [..."AEIOU"];
  
        if (length === word.length) {
            result.push(word);
            return;
        }
      
        alpha.forEach((alpha) => {
            dfs(word + alpha, length, result);
        });
    };
    for (let i = 1; i <= 5; i++) dfs(words, i, result);
    return result.sort().indexOf(word) + 1;
  }