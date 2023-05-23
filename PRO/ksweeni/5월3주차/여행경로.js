function solution(tickets) {
    var answer = [];
    var queue = [];
    const len = tickets.length;
    const visited = Array.from( { length : len }, () => false);
    
	tickets.sort();
   
    function dfs(str,count) {
        queue.push(str);
        if(count === len) {
            answer = queue;
            return true;
    }
         for(let i = 0; i < len; i++) {
		      if(!visited[i] && tickets[i][0] === str) {
			        visited[i] = true;
			        if(dfs(tickets[i][1], count+1)) return true;
			        visited[i] = false;
			      }
			    }
    
		    queue.pop();
		    return false;
  }
    dfs("ICN", 0);
    return answer;
}