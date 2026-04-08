button = document.getElementById("buttonEntrar");

button.addEventListener("click", ()=> {
    body = document.getElementById("body");

    item = document.createElement("img");

    item.style.width = "1000px";

    item.src = "./irra.jpg";

    body.innerHTML = "";
    body.appendChild(item);
});