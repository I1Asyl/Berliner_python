let teamNames = document.getElementById("application-team-names");
let members = document.getElementById("info");

let current = 0;
for (let child in teamNames.children) {
    console.log(child);
    members.children[child].style.display = "none";
    teamNames.children[child].onclick = function() {
        members.children[current].style.display = "none";
        current = child;
        members.children[current].style.display = "block";        
    }
}
