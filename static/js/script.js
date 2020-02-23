const topButton = document.getElementById("topBtn");

window.onscroll = function() {scrollFunction()};

function scrollFunction() {
  if(document.body.scrollTop > 40 || document.documentElement.scrollTop > 40) {
    topButton.style.display = "block";
  } else {
    topButton.style.display = "none";
  }
}

// When the user clicks on the button, scroll to the top of the document
function topFunction() {
  document.body.scrollTop = 0; // For Safari
  document.documentElement.scrollTop = 0; // For Chrome, Firefox, IE and Opera
}

$(document).ready(function () {
  $("ol.carousel-indicators > li").first().addClass("active");
  $('.carousel-item')[0].className = "carousel-item active";
  $('body').scrollspy({ target: '#myNav' });
 });
