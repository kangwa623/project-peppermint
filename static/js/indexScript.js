/* file: indexScript.js */

var copy = document.querySelector(".logos-slide").cloneNode(true);
document.querySelector(".logos").appendChild(copy);


$('.js-scroll-trigger').click(function() {
    $('.navbar-collapse').collapse('hide');
});