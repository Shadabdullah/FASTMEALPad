document.addEventListener('DOMContentLoaded', function () {

    var logBtn = document.getElementById("log-btn");
    var modal = document.getElementById('myModal');
    var closeBtn = document.getElementsByClassName('close-btn')
    var cancelBtn = document.getElementById('cancel-btn')
   
    logBtn.onclick = function () {
      event.preventDefault(); // Prevents the default anchor link behavior
      modal.style.display = 'block';
     
    }
    closeBtn.onclick = function () {
      modal.style.display = 'none';
    };
    cancelBtn.onclick = () => {
      event.preventDefault();
      modal.style.display = 'none';
    }
  
    window.onclick = function (event) {
      if (event.target === modal) {
        modal.style.display = 'none';
      }
    };
  
  
  })
  