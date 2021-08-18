var i = 0;
var txt = 'Love Writing ❤️';
var speed = 200; 

function typeWriter() {
if (i < txt.length) {
    document.getElementById("animation").innerHTML += txt.charAt(i);
    i++;
    setTimeout(typeWriter, speed);
}
}
typeWriter()

var slideIndex = 0;
showSlides();
function showSlides() {
  var i;
  var slides = document.getElementsByClassName("display_none");
  for(i = 0; i < slides.length; i++) {
    slides[i].style.display = "none";
  }
  slideIndex++;
  if(slideIndex > slides.length) {
    slideIndex = 1
  }
  slides[slideIndex - 1].style.display = "block";
  setTimeout(showSlides, 30000);
}
