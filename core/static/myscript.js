// alert("Hi!");

document.addEventListener("DOMContentLoaded", function() {    
    const btn = document.querySelector("button");
    btn.addEventListener("click", changeColor);
});

function changeColor() {
    const element = document.querySelector("div");
    element.style.color = "red";
}

// function redColor() {
//     const txt = document.querySelector("div");
//     txt.style.color = "red";
// };
