// alert("Hi!");

document.addEventListener("DOMContentLoaded", changeColor);

function changeColor() {
    const element = document.querySelector("div");
    element.style.color = "#00a329";
}

function redColor() {
    const txt = document.querySelector("div");
    txt.style.color = "red";
};
