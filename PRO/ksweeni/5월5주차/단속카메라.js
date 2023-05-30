function solution(routes) {
    routes.sort(function compare(a, b) {
       return a[0] - b[0];
    });
    console.log(routes)
    var cam = 1;
    let min = routes[0][0];
    let max = routes[0][1];
    
    for(let i=1;i<routes.length;i++){
        if(routes[i][0] >= min && routes[i][1] <=max){
            min = routes[i][0];
            max = routes[i][1];
            continue;
        }
        else if (routes[i][0] >= min && routes[i][0] <= max) continue;
        else{
            console.log(min, max)
            min = routes[i][0];
            max = routes[i][1];
            console.log(min, max)
            cam ++;
        }
    }
    return cam;
}