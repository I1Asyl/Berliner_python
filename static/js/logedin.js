
class Menu {
    constructor(className, defaultPosition) {
        this.menu = document.getElementsByClassName(className);
        this.hideByDetailsName(this.menu);

        if(defaultPosition !== -1) {
            console.log(defaultPosition);
            this.current = this.menu[defaultPosition]; 
            this.showElement(this.current);
        }
        else {
            this.current = -1;
        }
    }

    
    hideElement = function(element){
        this.hideByClassName(element.dataset.details);
        element.style.backgroundColor = "transparent";    
    }

    showElement = function(element){
        console.log(element);
        console.log("element");

        this.showByClassName(element.dataset.details);

        element.style.backgroundColor = "#b7bcbdd5";
    }

    hideByClassName = function(className){
        let elements = document.getElementsByClassName(className);
        for (let element of elements) {
            element.style.display = "none";
        }
    }

    showByClassName = (className) => {

        let elements = document.getElementsByClassName(className);

        for (let element of elements) {
            console.log(element);

            element.style.display = "block";

        }
    }
    hideByDetailsName = (className) => {
        for (let child of className) {
            this.hideByClassName(child.dataset.details);
        } 
    }
    onClickInfoPopUp =() => {
        var self = this; 
        for (let child of self.menu) {
            console.log(child.dataset.details);
            console.log(child);
            console.log("child");
            child.onclick = function() {
                if(self.current != -1){
                    console.log(this);
                    console.log("this");

                    console.log(self.current);
                    console.log("self.current");
                    self.hideElement(self.current);
                    
                }
                self.current = (child === self.current) ? -1 : child;

                if(self.current != -1){
                    self.showElement(self.current);
            
                }
            }
        }
    }
    onHoverPopUp() {
        for (let child of self.menu) {
            child.addEventListener(
                "mouseenter",
                (event) => {
                    // highlight the mouseenter target
                    if(self.current == -1)
                        self.showByClassName(event.target.dataset.details);
                    },
                    false
                );  

            child.addEventListener(
                "mouseleave",
                (event) => {
                    // highlight the mouseenter target
                    if(self.current != event.target)
                        self.hideByClassName(event.target.dataset.details);
                    },
                    false
                );  
        }
    }
}

//let teams = new Menu('team-name', 0);

let comments = new Menu('comment', -1);
comments.onClickInfoPopUp();


let team_names = new Menu('team-name', 0);
team_names.onClickInfoPopUp();
team_names.onHoverPopUp();