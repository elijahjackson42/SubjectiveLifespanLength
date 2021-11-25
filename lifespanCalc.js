/** 
let totalSpan=125;
let compareYear=18;
const calcLifespan = (totalSpan, compareYear) =>{
    let subjectiveYear=1/compareYear
    let total=0;
    for(let i = 0; i<totalSpan; i++){
        total+=1/i;
        console.log(1/i);
    }
    console.log(total);
    console.log(total/subjectiveYear);
}
calcLifespan(totalSpan,compareYear);
*/