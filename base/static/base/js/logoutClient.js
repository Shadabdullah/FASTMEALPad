document.addEventListener('DOMContentLoaded', function () {

    var logBtn = document.getElementById("logoutButtonFooter");
    var logHeader = document.getElementById('headerLogout')
    var modal = document.getElementById('myModal');
 
    var cancelBtn = document.getElementById('cancel-btn')
   
    logBtn.onclick = function () {
      event.preventDefault(); // Prevents the default anchor link behavior
      modal.classList.remove('hidden') 
     
    }
     logHeader.onclick = function () {
      event.preventDefault(); // Prevents the default anchor link behavior
      modal.classList.remove('hidden') 
     
    }
   
    cancelBtn.onclick = () => {
      event.preventDefault();
      modal.classList.add('hidden')
    }
  
    window.onclick = function (event) {
      if (event.target === modal) {
        modal.style.display = 'none';
      }
    };
  
  
  })
  