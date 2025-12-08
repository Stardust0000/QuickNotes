function mode() 
{
    const ele = document.body;
    if( ele.classList.contains("dark-theme")) {
        ele.classList.remove("dark-theme");
        ele.classList.add("light-theme");
    } else {
        ele.classList.remove("light-theme");
        ele.classList.add("dark-theme");
    }

    // save theme in local storage
    const theme = ele.classList.contains("dark-theme")? "dark":"light";
    localStorage.setItem("theme",theme);

    document.body.style.opacity = 0;
    setTimeout(()=> {
        document.body.style.opacity = 1;
    }, 200);

}
    const savedTheme = localStorage.getItem("theme");
    if(savedTheme === "dark") {
        document.body.classList.add("dark-theme")
    } else {
        document.body.classList.add("light-theme")
    }
