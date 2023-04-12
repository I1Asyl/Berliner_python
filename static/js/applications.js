let teamNames = document.getElementById("applications");
let members = document.getElementById("members");

let current = -1;
for (let child of teamNames.children) {
    let details = document.getElementById(child.dataset.details);
    details.style.display = "none";
    child.onclick = function() {
        if(current != -1){
            details = document.getElementById(current.dataset.details);
            details.style.display = "none";
            current.style.backgroundColor = "transparent";
        }
        current = child;
        console.log(current);

        details = document.getElementById(current.dataset.details);
        details.style.display = "block"; 
        current.style.backgroundColor = "#b7bcbdd5";
        
    }

    child.addEventListener(
        "mouseenter",
        (event) => {
            // highlight the mouseenter target
            if(current == -1)
                document.getElementById(event.target.dataset.details).style.display = "block";
    
        },
        false
        );  

        child.addEventListener(
            "mouseleave",
            (event) => {
                // highlight the mouseenter target
                if(current != event.target)
                    document.getElementById(event.target.dataset.details).style.display = "none";
        
            },
            false
            );  
}
