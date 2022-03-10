// const control = document.getElementById('head')

// function addTitle(){
//     control.innerText = "What the"
// }

let i = 1;

const tmp = document.getElementById("head");

function addTitle(){
  tmp.innerHTML += `\n제목${i++}`;
}