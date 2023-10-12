function themechange() {
    var themeIcon = document.getElementById("theme-icon");
    let themeButton = document.getElementById("theme-button-button")
    const root = document.documentElement;

    let dark = "#2f3741"
    let white = "white";
;    // Check the current text content of the theme-icon
    if (themeIcon.textContent === "dark_mode") {
        // Change to "light_mode" when it's "dark_mode"
        themeIcon.textContent = "light_mode";
        root.style.setProperty('--bg-color', dark);
        root.style.setProperty('--icon-color', white);
    } else {
        // Change back to "dark_mode" when it's "light_mode"
        themeIcon.textContent = "dark_mode";
        root.style.setProperty('--bg-color', white);
        root.style.setProperty('--icon-color', dark)
    }
}
