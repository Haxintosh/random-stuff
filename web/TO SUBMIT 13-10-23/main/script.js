const root = document.documentElement;
const red = "#ff5555";
const green = "#44da6a";


if (localStorage.getItem('UUIDs') === null) {
  localStorage.setItem('UUIDs', JSON.stringify(["uwu"]));
}

let uuidList = JSON.parse(localStorage.getItem('UUIDs'));

let sessionCookie = getCookie("sessionUUIDOHNO").split(":");
let sessionID;
let sessionUsername;
console.log(sessionUUID = sessionCookie[0]);

if (sessionCookie) {
  sessionUUID = sessionCookie[0];
  sessionUsername = sessionCookie[1];
  console.log(sessionUUID);
  console.log(sessionUsername);
} else {
  invalidSession();
}

if (uuidList.includes(sessionUUID)) {
  validSession();
} else {
  invalidSession();
}

function validSession () {
  let notifTitle = document.getElementById("notif-title");
  let notifText = document.getElementById("notif-text");
  root.style.setProperty('--notif-color', green);
  notifTitle.innerHTML = "Welcome!";
  notifText.innerHTML = "Hi " + sessionUsername + "!"
}

function invalidSession () {
  let notifTitle = document.getElementById("notif-title");
  let notifText = document.getElementById("notif-text");
  root.style.setProperty('--notif-color', red);
  notifTitle.innerHTML = "Unauthorized!";
  notifText.innerHTML = "User not authenticated!"
}

function getCookie(cname) {
  let name = cname + "=";
  let decodedCookie = decodeURIComponent(document.cookie);
  let ca = decodedCookie.split(';');
  for(let i = 0; i <ca.length; i++) {
    let c = ca[i];
    while (c.charAt(0) == ' ') {
      c = c.substring(1);
    }
    if (c.indexOf(name) == 0) {
      return c.substring(name.length, c.length);
    }
  }
  return "";
}
