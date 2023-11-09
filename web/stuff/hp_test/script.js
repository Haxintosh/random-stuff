const root = document.documentElement;
hp = 100;
function pctChange(){
    event.preventDefault();
    let pct = document.getElementById("pct").value;
    root.style.setProperty("--bar", pct + "%");
}

function damage(){
    dmgToDeal = 20*Math.random();
    if (dmgToDeal >= 10){
        alert("critical");
    }
    hp = hp - dmgToDeal;
    dmgChange(hp);
}

function dmgChange(hp){
    event.preventDefault();
    root.style.setProperty("--bar", hp + "%");
    hp = 100;
}


