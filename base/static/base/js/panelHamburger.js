const prof = document.getElementById("user-menu-button")
const menu = document.getElementById("userMenu")

 function profileHandler(){
    menu.classList.toggle("hidden")
 }
if(prof){

  prof.addEventListener("click" , profileHandler)
}

// code for mobile view
const toggleButton = document.getElementById("toggle-button");
const hamburgerIcon = document.getElementById("hamburger");
const closeIcon = document.getElementById("close");
const menuArea = document.getElementById("mobile-menu")
if(toggleButton){


  toggleButton?.addEventListener("click", function () {
    // Toggle the "hidden" class on the SVG icons
    hamburgerIcon.classList.toggle("hidden");
    menuArea.classList.toggle("hidden")
    closeIcon.classList.toggle("hidden");
  });
}
