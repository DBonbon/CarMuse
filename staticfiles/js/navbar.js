$(function(){
  $(".dropdown-item").click(function(){
    var icon_text = $(this).html(icon_text);
    $(".dropdown-toggle").html(icon_text);
  })
})


$(function(){
      $("[data.trigger]").on("click",function(){
        var targeet_id = $(this).attr('data-trigger');
        $(target_id).toggleClass("show");
        $('body').toggleClass("offcanvas-active");
      })

      //close button
      $("btn.close").click(function(e){
      $(".navbar-collapse").removeClass("show");
      $("body").removeClass("offcanvas-active");
    })
})


