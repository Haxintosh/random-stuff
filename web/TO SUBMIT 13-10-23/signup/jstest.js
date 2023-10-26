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

function verifysignup() {
    let home_url = "https://google.com";
    
        let username = document.getElementById("username").value;
        let psw = document.getElementById("psw").value;
        let pswConfirm = document.getElementById("psw-conf").value;
        var usernames = [];
        let uuid = generateUUID();


        if (localStorage.getItem('UUIDs') === null) {
            localStorage.setItem('UUIDs', JSON.stringify(["uwu"]));
        }

        let uuidList = JSON.parse(localStorage.getItem('UUIDs'));
        // localStorage.setItem('UUIDs', JSON.stringify(["uwu"])); // REMOVE
        
        console.log(username);
        console.log(psw);
        console.log(pswConfirm);

        if (username==="rickroll") {
            window.location.replace("https://www.youtube.com/watch?v=dQw4w9WgXcQ");
            return;
        }

        // welcome to if hell
        if (username==="") {
            warn("Error!", "Empty username!", "ERR");
            return;
        } 
        
        if (psw==="") {
            warn("Error!", "Empty password!", "ERR");
            return;          
        } 
        
        if (pswConfirm==="") {
            warn("Error!", "Empty confirm password!", "ERR");
            return;
        }

        if (psw.length < 8) {
            warn("Error!", "Password less than 8 characters!", "ERR");
            return;
        }

        localStorage.setItem('testuser', 'test');

        for (var i = 0; i < localStorage.length; i++) {
        usernames.push(localStorage.key(i));
        }

        console.log(usernames);


        if (usernames.includes(username)) {
            console.log("in storage!");
            // if (dict[username] == psw) {
            //     console.log("in!");
            //     warn("Success!", "You will be redirected...", "INF");
            //     window.location.replace(home_url);
            warn("Error!", "Username taken!", "ERR");
            return;
            } 
        
        if (psw===pswConfirm) {
                localStorage.setItem(username, psw);
                let cookie = "sessionUUIDOHNO="+uuid; 
                document.cookie = cookie + ";SameSite=Strict";
                uuidList.push(uuid);
                localStorage.setItem('UUIDs', JSON.stringify(uuidList));
                warn("Success!", "You will be redirected...", "INF");
                // window.location.replace("https://sillygoosy.ca");         
            } else {
                warn("Error!", "Confirm password does not equal to password!", "ERR");
                return;
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

    // straight from... uh oh looks like it got corrupted here
function generateUUID() {
    return 'xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx'.replace(/[xy]/g, function(c) {
        var r = (Math.random() * 16) | 0;
        var v = c === 'x' ? r : (r & 0x3 | 0x8);
        return v.toString(16);
    });
    }
