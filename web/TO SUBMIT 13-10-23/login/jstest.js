
function themechange() {
    let themeIcon = document.getElementById("theme-icon");
    let themeButton = document.getElementById("theme-button-button")
    const root = document.documentElement;

    let dark = "#282A36";
    let white = "#F8F8F2";
    let text_line_white = "gray";
    let text_line_dark = "#cbcbcb"; 
    if (themeIcon.textContent === "dark_mode") {
        themeIcon.textContent = "light_mode";
        root.style.setProperty('--bg-color', dark);
        root.style.setProperty('--icon-color', white);
        root.style.setProperty('--input-line-color', text_line_dark);
    } else {
        themeIcon.textContent = "dark_mode";
        root.style.setProperty('--bg-color', white);
        root.style.setProperty('--icon-color', dark);
        root.style.setProperty('--input-line-color', text_line_white);
    }
}
function verifylogin() {
    event.preventDefault();
    let home_url = "https://google.com";
        let username = document.getElementById("username").value;
        let psw = document.getElementById("psw").value;
        let uuid = generateUUID();
        let usernames = [];

        localStorage.setItem("uwu", "test");

        if (localStorage.getItem('UUIDs') === null) {
            localStorage.setItem('UUIDs', JSON.stringify(["uwu"]));
        }

        let uuidList = JSON.parse(localStorage.getItem('UUIDs'));

        for (var i = 0; i < localStorage.length; i++) {
            usernames.push(localStorage.key(i));
        }
        
        if (usernames.includes(username)) {
            console.log("in storage!");
            if (psw == localStorage.getItem(username)) {
                console.log("in!");
                let cookie = "sessionUUIDOHNO="+ uuid + ":" + username; 
                document.cookie = cookie + ";SameSite=Lax;path=/";
                uuidList.push(uuid);
                localStorage.setItem('UUIDs', JSON.stringify(uuidList));
                warn("Success!", "You will be redirected...", "INF");
            } else {
                console.log("out! (UWU) ");
                warn("Error!", "Invalid Password!", "ERR");
            }
            } else {
                console.log("out!");
                warn("Error!", "Username Not Found! (Sign up?)", "ERR");
            }
}

function warn(header, message, type) {
    const root = document.documentElement;

    let warnCont = document.getElementById("invalid");
    let warnIcon = document.getElementById("warn-icon");
    let warnHeader = document.getElementById("invalid-header");
    let warnText = document.getElementById("invalid-text-span");

    let red = "#ff5555";
    let green = "#44da6a";

    if (type === "ERR") {
        root.style.setProperty("--warn-type-color", red);
        warnIcon.textContent = "error";
        warnText.innerHTML = message;
        warnHeader.innerHTML = header;
        warnCont.style.visibility = "visible";
        setTimeout(() => {
            warnCont.style.visibility = "hidden";
        }, 2000)
    }

    if (type === "INF") {
        root.style.setProperty("--warn-type-color", green);
        warnIcon.textContent = "done";
        warnText.innerHTML = message;
        warnHeader.innerHTML = header;
        warnCont.style.visibility = "visible";
        setTimeout(() => {
            warnCont.style.visibility = "hidden";
        }, 2000);
    }
}

function generateUUID() {
    return 'xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx'.replace(/[xy]/g, function(c) {
        var r = (Math.random() * 16) | 0;
        var v = c === 'x' ? r : (r & 0x3 | 0x8);
        return v.toString(16);    
    });
    }
