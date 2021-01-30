var id = 1;
var isClicked = true;

$(".txtb").on("keyup",function(e){
    //13  means enter button
    if(e.keyCode == 13 && $(".txtb").val() != "")
    {
      // task
      var task = $("<div class='task'></div>").text($(".txtb").val());

      //star
      var star = $(`<span id='star_${id}'><i class='far fa-star'></i></span>`).click(function(){
        var p = $(this).parent();

        if(isClicked) {
          $(this).children(".fa-star").removeClass("far fa-star").addClass("fas fa-star");
          p.css('background', '#371F54');
          isClicked = false;
          
        } else {
          $(this).children(".fa-star").removeClass("fas fa-star").addClass("far fa-star");
          p.css('background', '#81589f9d');
          isClicked = true;
        }
      });

      //delete
      var del = $("<i class='fas fa-trash-alt'></i>").click(function(){
        var p = $(this).parent();
        p.fadeOut(function(){
          p.remove();
        });
      });

      //check
      var check = $("<i class='fas fa-check'></i>").click(function(){
        var p = $(this).parent();
        p.fadeOut(function(){
          $(".comp").append(p);
          p.fadeIn();
        });
        $(this).remove();
      });

      task.append(del,check,star);

      $(".notcomp").append(task);
      //to clear the input
      $(".txtb").val("");
      
      id++;
    }
});


  // var todayContainer = document.querySelector(".today");
  // var d = new Date();
  // var weekday = new Array(7);
  // weekday[0] = "Sunday 🖖";
  // weekday[1] = "Monday 💪😀";
  // weekday[2] = "Tuesday 😜";
  // weekday[3] = "Wednesday 😌☕️";
  // weekday[4] = "Thursday 🤗";
  // weekday[5] = "Friday 🍻";
  // weekday[6] = "Saturday 😴";
  
  // var n = weekday[d.getDay()];
  
  // var randomWordArray = Array(
  //   "Oh my, it's ",
  //   "Whoop, it's ",
  //   "Happy ",
  //   "Seems it's ",
  //   "Awesome, it's ",
  //   "Have a nice ",
  //   "Happy fabulous ",
  //   "Enjoy your "
  // );
  // var randomWord =
  //   randomWordArray[Math.floor(Math.random() * randomWordArray.length)];
  // todayContainer.innerHTML = randomWord + n;

