var id = 1;

$(".txtb").on("keyup",function(e){
    //13  means enter button
    if(e.keyCode == 13 && $(".txtb").val() != "")
    {
      var task = $("<div class='task'></div>").text($(".txtb").val());

      var star = $("<i class='far fa-star' id='"+id+"'></i>").click(function(){
        $(this).removeClass('far fa-star');
        $(this).addClass('fas fa-star');
      });

      var del = $("<i class='fas fa-trash-alt'></i>").click(function(){
        var p = $(this).parent();
        p.fadeOut(function(){
          p.remove();
        });
      });

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


