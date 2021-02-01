//get clicked category_id, category_name
function getParameterByName(name) {
  name = name.replace(/[\[]/, "\\[").replace(/[\]]/, "\\]");
  var regex = new RegExp("[\\?&]" + name + "=([^&#]*)"),
          results = regex.exec(location.search);
  return results == null ? "" : decodeURIComponent(results[1].replace(/\+/g, " "));
}

var category_id = getParameterByName('category_id');
var category_name = getParameterByName('category_name');
console.log(category_id);
console.log(category_name);

//url 지정
// var server_url = '';
// var category_id = '';
// var url = server_url + '/todo/' + category_id;

//get todolist -> GET
get_category_name();
get_todo();

function get_category_name() {
  console.log(category_name);
  document.querySelector('header').innerHTML = `
          <h1 class="screen-header__title" id="category_title" contentEditable="true">${category_name}</h1>
        `;
}

// function get_todolist() {
//   var url = server_url + '/todo/'
//   fetch(url,{category_id: clicked_category_id})
//     .then(
//       function(type){
//         return type.json();
//       }
//     )
//     .then(
//       function(result){
//         console.log(result);
//         console.log(result.result[0].name);
//         console.log(result.result[0].id);

//         category_id = result.result[0].id;
//         console.log(category_id);

//         // get title
//         document.querySelector('header').innerHTML = `
//           <h1 class="screen-header__title" id="category_title" contentEditable="true">${result.result[0].name}</h1>
//         `;
//         get_todo();
//       }
//     );
// }

//get todo -> GET
function get_todo() {
  var url = '/todo/'+ category_id;
  console.log(category_id);
  fetch(url, {category_id: category_id})
    .then(
      function(type){
        return type.json();
      }
    )
    .then(
      function(result){

        console.log(result.result);
        var result = result.result
        console.log(result);
        
        // get content

        for(var i=0; i<result.length; i++){
          var content = result[i].content;
          var status = result[i].status;

          if (status === false) {
            var task = $("<div class='task' contentEditable='true'></div>").text(content);
            task.append(del, check);
            console.log(task[0]);
            $(".notcomp").append(task);
          } 
          else {
            var task = $("<div class='task' contentEditable='true'></div>").text(content);
            task.append(del, check);
            console.log(task);
            $(".comp").append(task);
          }
        }
      }
    );
} 

// edit_category_title -> PUT
$("#category_title")
    // When you click on item, record into data("initialText") content of this item.
    .focus(function() {
        $(this).data("initialText", $(this).html());
        console.log($("#category_title").html());
    })
    // When you leave an item...
    .blur(function() {
        // ...if content is different...
        if ($(this).data("initialText") !== $(this).html()) {
            // ... do something.
            console.log('New data when content change.');
            console.log($(this).html());
            
            var category_title = $(this).html();
            console.log(category_title);
            // var url = server_url + '/todo/' 
            // fetch(url,{
            //     method: "PUT",
            //     body: JSON.stringify({
            //       name: category_title
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
  var url = server_url + '/todo/'+ category_id;
  console.log(url);
  fetch(url,{
      method: "PUT",
      body: JSON.stringify({
        status: "1"
      }),
      headers:{
        'Content-Type':'application/json'
      }            
    })
    .then(
      function(type){
        return type.json();
      }
    )
    .then(
      function(result){
        console.log(result);
      }
    );    
});

// del 선언 
// click -> delete task -> DELETE
var del = $("<i class='fas fa-trash-alt'></i>").click(function(){
  var p = $(this).parent();
  p.fadeOut(function(){
    p.remove();
  });

  //delete db
  var del_content = $(this).parent().val();
  fetch(url,{
      method: "DELETE",
      body: JSON.stringify({
        content: del_content
      }),
      headers:{
        'Content-Type':'application/json'
      }            
    })
    .then(
      function(type){
        return type.json();
      }
    )
    .then(
      function(result){
        console.log(result);
      }
    );          
});

// enter 키 -> task 추가 -> POST
$(".txtb").on("keyup",function(e){
  //13  means enter button
  if(e.keyCode == 13 && $(".txtb").val() != "")
  {
    var new_task_content = $(".txtb").val();
    
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

    var task = $("<div class ='task_content' contentEditable='true'></div>").text(new_task_content);
    
    // del, check append
    task.append(del, check);

      // append to notcomplete task
    $(".notcomp").append(task);
      //to clear the input
    $(".txtb").val("");
  }
});

