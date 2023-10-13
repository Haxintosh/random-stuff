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

function verify(){
        let dict = { // worst login ever
            "uwu" : "test",
            "honk" : "ein",
            "ping" : "pong"
        };
    
        let username = document.getElementById("userfield").value;
        let psw = document.getElementById("pswfield").value;
        if (username in dict) {
            if (dict[username] == psw) {
                alert("logged in")
            } else {
                warn()
            }
            } else {
                invalid()
            }
}

function warn() {
    let warnIcon = document.getElementById("warn-icon");
    let warnHeader = document.getElementById("invalid-header");
    let warnText = document.getElementById("invalid-text-span");

    let red = "#ff5555";
    let green = "#44da6a";

}
