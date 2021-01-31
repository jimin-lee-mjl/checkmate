// edit_list_title -> PUT
$("#list_title")
    // When you click on item, record into data("initialText") content of this item.
    .focus(function() {
        $(this).data("initialText", $(this).html());
        console.log($(this).html());
    })
    // When you leave an item...
    .blur(function() {
        // ...if content is different...
        if ($(this).data("initialText") !== $(this).html()) {
            // ... do something.
            console.log('New data when content change.');
            console.log($(this).html());
            
            var list_title = $(this).html();
            console.log(list_title);
            // fetch(url,{
            //     method: "PUT",
            //     body: JSON.stringify({
            //       title: list_title
            //     }),
            //     headers:{
            //       'Content-Type':'application/json'
            //     }            
            //   })
            //   .then(
            //     function(type){
            //       return type.json();
            //     }
            //   )
            //   .then(
            //     function(result){
            //       console.log(result);
            //     }
            //   );
        }
    });


// check 선언
// click -> update task status -> PUT
var check = $("<i class='fas fa-check'></i>").click(function(){
  var p = $(this).parent();
  p.fadeOut(function(){
    if (p.parent().hasClass("notcomp")){
      $(".comp").append(p);
      p.fadeIn();
    } else if (p.parent().hasClass("comp")){
      $(".notcomp").append(p);
      p.fadeIn();
    }
  });

  //update task status
  // fetch(url,{
  //     method: "PUT",
  //     body: JSON.stringify({
  //       status: "complete"
  //     }),
  //     headers:{
  //       'Content-Type':'application/json'
  //     }            
  //   })
  //   .then(
  //     function(type){
  //       return type.json();
  //     }
  //   )
  //   .then(
  //     function(result){
  //       console.log(result);
  //     }
  //   );    
});

// del 선언 
// click -> delete task -> DELETE
var del = $("<i class='fas fa-trash-alt'></i>").click(function(){
  var p = $(this).parent();
  p.fadeOut(function(){
    p.remove();
  });

  //delete db
  // var del_content = $(this).parent().val();
  // fetch(url,{
  //     method: "DELETE",
  //     body: JSON.stringify({
  //       content: del_content
  //     }),
  //     headers:{
  //       'Content-Type':'application/json'
  //     }            
  //   })
  //   .then(
  //     function(type){
  //       return type.json();
  //     }
  //   )
  //   .then(
  //     function(result){
  //       console.log(result);
  //     }
  //   );          
});

// enter 키 -> task 추가 -> POST
$(".txtb").on("keyup",function(e){
  //13  means enter button
  if(e.keyCode == 13 && $(".txtb").val() != "")
  {
    var new_task = $(".txtb").val();
    
    // fetch(url,{
    //   method: "POST",
    //   body: JSON.stringify({
    //     content: new_task
    //   }),
    //   headers:{
    //     'Content-Type':'application/json'
    //   }            
    // })
    // .then(
    //   function(type){
    //     return type.json();
    //   }
    // )
    // .then(
    //   function(result){
    //     console.log(result);
    //   }
    // );

    var task_box = $("<div class='task'></div>");
    var task = $("<div class ='task_content' contentEditable='true'></div>").text($(".txtb").val());
    var due = $("<div class ='task_due' contentEditable='true'></div>").text("due date:");
    // del, check append
    
    task_box.append(task, due);
    task_box.append(del, check);

      // append to notcomplete task
    $(".notcomp").append(task_box);
      //to clear the input
    $(".txtb").val("");
  }
});






