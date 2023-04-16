import Menu from './logedin.js'; 

let comments = new Menu('comment', -1);
comments.onClickInfoPopUp();
let team_names = new Menu('team-name', 0);
team_names.onClickInfoPopUp();
team_names.onHoverPopUp();