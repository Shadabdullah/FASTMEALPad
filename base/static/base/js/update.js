


document.addEventListener('DOMContentLoaded', function () {
    const updBtn = document.querySelectorAll('.update-btn')
    const updateF = document.getElementById('updateForm')
    
    updBtn.forEach(function (updateBtn) {
        updateBtn.addEventListener('click', function () {
        updateF.classList.toggle("hidden")

            console.log("PRess")
        })
    })
})
 function removeModal(){
    const updateF = document.getElementById('updateForm');
    updateF.classList.add('hidden')
    console.log("pressed")

}
const submitBtn = document.getElementById('submitBtn')
if(submitBtn !== null){
    submitBtn.addEventListener('click', removeModal)
}
