$(document).ready(function() {
  $(".show-hide-btn").click(function() {
    var id = $(this).data("id");
    $("#half-" + id).toggle();//hide/show..
    $("#full-" + id).toggle();
  })
})

//NAVBAR
$(document).ready(function() {
        // Transition effect for navbar
        $(window).scroll(function() {
          // checks if window is scrolled more than 500px, adds/removes solid class
          if($(this).scrollTop() > 500) {
              $('.navbar').addClass('solid');
          } else {
              $('.navbar').removeClass('solid');
          }
        });
});