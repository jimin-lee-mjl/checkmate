var id = 1;
var isClicked = true;

$(".txtb").on("keyup",function(e){
    //13  means enter button
    if(e.keyCode == 13 && $(".txtb").val() != "")
    {
      var task = $("<div class='task'></div>").text($(".txtb").val());

      var cal = "<span style='display:none;'><input style='margin-left: 10px;' type='text' id='from_"+id+"'><span> ~ </span><input type='text' id='to_"+id+"'></span>";

      var calendar = $(`<span id='cal_${id}'><i class='far fa-calendar-alt'></i></span>`).click(function(){
        
        var arr = $(this).attr("id").split("_");
        var p = $("#from_"+arr[1]).parent();
        p.toggle();

        var style = p.attr("style");
        
        if(style.toString().includes('none')) {
          $("#from_"+arr[1]).val("");
          $("#to_"+arr[1]).val("");
        }

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

      task.append(del,check,star,cal,calendar);
      
      $(".notcomp").append(task);
      //to clear the input
      $(".txtb").val("");

      fn_init(id);

      id++;
    }
});

function fn_init(id) {
  var rangeDate = 31; // set limit day
  var setSdate, setEdate;
  $("#from_"+id).datepicker({
      dateFormat: 'yy-mm-dd',
      minDate: 0,
      onSelect: function(selectDate){
          var stxt = selectDate.split("-");
              stxt[1] = stxt[1] - 1;
          var sdate = new Date(stxt[0], stxt[1], stxt[2]);
          var edate = new Date(stxt[0], stxt[1], stxt[2]);
              edate.setDate(sdate.getDate() + rangeDate);
          $('#to_'+id).datepicker('option', {
              minDate: selectDate,
              beforeShow : function () {
                  $("#to_"+id).datepicker( "option", "maxDate", edate );
                  setSdate = selectDate;
                  //console.log(setSdate)
          }});
          //to 설정
      }
      //from 선택되었을 때
  });
  $("#to_"+id).datepicker({
      dateFormat: 'yy-mm-dd',
      onSelect : function(selectDate){
          setEdate = selectDate;
          //console.log(setEdate)
      }
  });
}