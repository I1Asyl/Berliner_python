var menu = document.getElementById("menu");
var current = menu.children[0];

function hide(element) {
    hideByClassName(element.dataset.details);
    element.style.backgroundColor = "transparent";    
}

function show(element) {
    showByClassName(current.dataset.details);
    current.style.backgroundColor = "#b7bcbdd5";
}

function hideByClassName(className) {
    let elements = document.getElementsByClassName(className);
    for (let element of elements) {
        element.style.display = "none";
    }
}

function showByClassName(className) {
    let elements = document.getElementsByClassName(className);
    for (let element of elements) {
        element.style.display = "block";
    }
}

for (let child of menu.children) {
    hideByClassName(child.dataset.details)

    child.onclick = function() {
        if(current != -1)
            hide(current);

        current = (child === current) ? -1 : child;
        show(current);
    }

    child.addEventListener(
        "mouseenter",
        (event) => {
            // highlight the mouseenter target
            if(current == -1)
                showByClassName(event.target.dataset.details);
    
        },
        false
        );  

        child.addEventListener(
            "mouseleave",
            (event) => {
                // highlight the mouseenter target
                if(current != event.target)
                    hideByClassName(event.target.dataset.details);
        
            },
            false
            );  
}
// Show first menu element
show(current);