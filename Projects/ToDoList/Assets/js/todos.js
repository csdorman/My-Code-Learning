//Check off specific todos by clicking
//This way ONLY works with pre-populated events.
//The "li" listener only listens on elements present on initial page load.

// $("li").click(function(){
//   $(this).toggleClass("completed");
// });

//So we need to listen on an element that is present on initial load.
//This is what it has to be for dynamically-created events to work
$("ul").on("click", "li", function(){
    $(this).toggleClass("completed");
  });

//Click on X to delete todo
$("ul").on("click", "span", function(event){
    $(this).parent().fadeOut(500, function(){
        $(this).remove();
    });
    event.stopPropagation();
});

//Adding a new todo
$("input[type='text']").keypress(function(event){
    //Check that enter key is the one pressed
    if(event.which === 13){
        //Grab text from input field, save as variable
       var todoText = $(this).val();
       $(this).val("");
        //Append variable to end of ul 
       $("ul").append("<li><span><i class='fas fa-minus-circle'></i></span> " + todoText + "</li>");
    }
})

$(".fa-edit").click(function(){
    $("input[type='text']").fadeToggle()
})