function themechange() {
    let themeIcon = document.getElementById("theme-icon");
    let themeButton = document.getElementById("theme-button-button")
    const root = document.documentElement;

    let dark = "#282A36";
    let white = "#F8F8F2";
    let text_line_white = "gray";
    let text_line_dark = "#cbcbcb"

;    // Check the current text content of the theme-icon
    if (themeIcon.textContent === "dark_mode") {
        // Change to "light_mode" when it's "dark_mode"
        themeIcon.textContent = "light_mode";
        root.style.setProperty('--bg-color', dark);
        root.style.setProperty('--icon-color', white);
        root.style.setProperty('--input-line-color', text_line_dark);
    } else {
        // Change back to "dark_mode" when it's "light_mode"
        themeIcon.textContent = "dark_mode";
        root.style.setProperty('--bg-color', white);
        root.style.setProperty('--icon-color', dark);
        root.style.setProperty('--input-line-color', text_line_white);
    }
}

function verifylogin() {
    let home_url = "https://google.com";
        let dict = { // worst login ever
            "uwu" : "test",
            "honk" : "ein",
            "ping" : "pong"
        };
    
        let username = document.getElementById("username").value;
        let psw = document.getElementById("psw").value;
        console.log(username);
        console.log(psw);
        if (username in dict) {
            console.log("in dict!")
            if (dict[username] == psw) {
                console.log("in!");
                warn("Success!", "You will be redirected...", "INF");
                window.location.replace(home_url);
                
            } else {
                console.log("out! (UWU) ");
                warn("Error!", "Invalid Password!", "ERR");
            }
            } else {
                console.log("out!");
                warn("Error!", "Invalid Username (Sign up?)", "ERR");
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
