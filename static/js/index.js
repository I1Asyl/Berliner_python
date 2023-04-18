import Menu from './logedin.js'; 


function changeNameForPopupButton(name) {
    let popup = document.getElementById('comment-popup');
    let popupButton = popup.getElementsByClassName('popup-button')[0];
    popupButton.name = name;
    console.log("shesesh");
}


let comments = new Menu('comment', -1, changeNameForPopupButton);

comments.onClickInfoAppear(changeNameForPopupButton);
let team_names = new Menu('team-name', 0);
team_names.onClickInfoAppear();
team_names.onHoverAppear();