var id = 1;
var isClicked = true;

$(".txtb").on("keyup",function(e){
    //13  means enter button
    if(e.keyCode == 13 && $(".txtb").val() != "")
    {
      // task
      var task = $("<div class='task'></div>").text($(".txtb").val());
      
      //calendar
      var cal = "<input style='margin-left: 10px;' placeholder='FROM' type='text' id='from'><span> ~ </span><input type='text' placeholder='TO' id='to'>";

      var date = $("<i class='far fa-calendar-check'></i>").click(function(){

      });

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

      task.append(del,check,star,date,cal);

      $(".notcomp").append(task);
      //to clear the input
      $(".txtb").val("");
      
      id++;
      fn_init();
    }
});


function fn_init() {
  var rangeDate = 31; // set limit day
  var setSdate, setEdate;
  $("#from").datepicker({
      dateFormat: 'yy-mm-dd',
      minDate: 0,
      onSelect: function(selectDate){
          var stxt = selectDate.split("-");
              stxt[1] = stxt[1] - 1;
          var sdate = new Date(stxt[0], stxt[1], stxt[2]);
          var edate = new Date(stxt[0], stxt[1], stxt[2]);
              edate.setDate(sdate.getDate() + rangeDate);
          $('#to').datepicker('option', {
              minDate: selectDate,
              beforeShow : function () {
                  $("#to").datepicker( "option", "maxDate", edate );
                  setSdate = selectDate;
                  console.log(setSdate)
          }});
          //to 설정
      }
      //from 선택되었을 때
  });
  $("#to").datepicker({
      dateFormat: 'yy-mm-dd',
      onSelect : function(selectDate){
          setEdate = selectDate;
          console.log(setEdate)
      }
  });
}