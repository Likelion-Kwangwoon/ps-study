function solution(n, works) {
    if(n >= works.reduce((a,b) => a + b)) return 0;
    Math.max.apply(null, works.sort((a,b)=> b-a));
    while(n!=0){
        const maxnum = works.at(0);
        for(let i=0;i<works.length;i++){
            if(works[i]>=maxnum){
                works[i]--;
                n--;
            }
            if(!n) break;
        }
    }
    return works.reduce((a,b) => a + b**2 , 0 )    
}