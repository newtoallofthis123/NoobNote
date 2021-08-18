var i = 0;
var txt = '⬇️ Download NoobNote';
var speed = 200; 

function typeWriter(e) {
if (i < txt.length) {
    document.getElementById("animation").innerHTML += txt.charAt(i);
    i++;
    setTimeout(typeWriter, speed);
}
}
typeWriter()
