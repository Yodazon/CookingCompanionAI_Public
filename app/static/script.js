function openPage(page) {
    console.log(page)
    window.location.href = page;
}

function addInput(){
    //Getting the container where the input elements are located

    var container = document.getElementById("input-container");

    // Creating new input elements
    var input = document.createElement("input");
    input.type = "text";
    input.name = "input" + container.childElementCount;
    input.placeholder = "Ingredient #" + (container.childElementCount +1)
    input.className = "rounded-md "

    //Append new element 
    container.appendChild(input)


}
