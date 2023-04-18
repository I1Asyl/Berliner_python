
export default class Menu {
    constructor(className, defaultPosition, func = false) {
        this.menu = document.getElementsByClassName(className);
        this.hideByDetailsName(this.menu);
        this.func = func;
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
    onClickInfoAppear = () => {
        var self = this; 
        for (let child of self.menu) {
            child.onclick = function() {
                if(self.current != -1){
                    self.hideElement(self.current);
                    
                }
                self.current = (child === self.current) ? -1 : child;

                if(self.current != -1){
                    self.showElement(self.current);
                    console.log(self.func);
                    console.log("aha")
                    if(self.func != false)
                        self.func(self.current.id)
                }
            }
        }    
    }
    onClickInfoPopUp =() => {

    }
    onHoverAppear() {
        self = this;
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

