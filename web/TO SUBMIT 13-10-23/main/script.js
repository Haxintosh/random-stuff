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

console.log(getCookie("sessionUUIDOHNO"));
sessionID = getCookie("sessionUUIDOHNO").split(";");

if (localStorage.getItem('UUIDs') === null) {
    localStorage.setItem('UUIDs', JSON.stringify(["uwu"]));
}

let uuidList = JSON.parse(localStorage.getItem('UUIDs'));

