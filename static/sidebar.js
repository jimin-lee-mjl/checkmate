/*===== EXPANDER MENU  =====*/ 
const showMenu = (toggleId, navbarId, bodyId)=>{
  const toggle = document.getElementById(toggleId),
  navbar = document.getElementById(navbarId),
  bodypadding = document.getElementById(bodyId)

  if(toggle && navbar){
    toggle.addEventListener('click', ()=>{
      navbar.classList.toggle('expander')

      bodypadding.classList.toggle('body-pd')
    })
  }
}
showMenu('nav-toggle','navbar','body-pd')

/*===== LINK ACTIVE  =====*/ 
// const linkColor = document.querySelectorAll('.nav__link')
// function colorLink(){
//   linkColor.forEach(l=> l.classList.remove('active'))
//   this.classList.add('active')
// }
// linkColor.forEach(l=> l.addEventListener('click', colorLink))


/*===== COLLAPSE MENU  =====*/ 
const linkCollapse = document.getElementsByClassName('collapse__link')
var i

for(i=0;i<linkCollapse.length;i++){
  linkCollapse[i].addEventListener('click', function(){
    const collapseMenu = this.nextElementSibling
    collapseMenu.classList.toggle('showCollapse')

    const rotate = collapseMenu.previousElementSibling
    rotate.classList.toggle('rotate')
  })
}


/*===== create_new_group_list =====*/ 
var create_group_list_btn = document.getElementById('create_group_list_btn'); 

function create_group_list() {
var new_group_list = document.createElement("a");
var br = document.createElement("br");

new_group_list.innerHTML = "New_List";

new_group_list.setAttribute("href","#");
new_group_list.setAttribute("class","collapse__sublink");
new_group_list.setAttribute("onclick","location.href='/tasks-group'");

var parent_group_list = document.getElementById("sub_group_list");
parent_group_list.appendChild(new_group_list);
parent_group_list.appendChild(br);
};

create_group_list_btn.addEventListener("click", create_group_list);  


/*===== create_new_personal_list =====*/ 
var create_personal_list_btn = document.getElementById('create_personal_list_btn'); 

function create_personal_list() {
var new_personal_list = document.createElement("a");
var br = document.createElement("br");

new_personal_list.innerHTML = "New_List";

new_personal_list.setAttribute("href","#");
new_personal_list.setAttribute("class","collapse__sublink");
new_personal_list.setAttribute("onclick","location.href='/tasks'");

var parent_personal_list = document.getElementById("sub_personal_list");
parent_personal_list.appendChild(new_personal_list);
parent_personal_list.appendChild(br);
};

create_personal_list_btn.addEventListener("click", create_personal_list);  

/*===== active color =====*/ 
const linkColor = document.querySelectorAll('.nav__link')
const listColor = document.querySelectorAll('.collapse__sublink')
listColor.forEach(l=> l.classList.remove('list_active'));

//for task-group
if ( window.location.pathname == '/tasks-group' ) {
  var current_location = document.getElementById("group_todo");
  linkColor.forEach(l=> l.classList.remove('active'));
  current_location.classList.add('active');

  if (window.location.pathname == '/tasks-group/elice') {
    var current_list = document.getElementById("group_list_1");
    current_list.classList.add('list_active');
  } 
  else if (window.location.pathname == '/tasks-group/study') {
    var current_list = document.getElementById("group_list_2");
    current_list.classList.add('list_active');
  }
} 

// for personal-group
else if ( window.location.pathname == '/tasks' ){
  var current_location = document.getElementById("personal_todo");
  linkColor.forEach(l=> l.classList.remove('active'));
  current_location.classList.add('active');
  
  var current_list = document.getElementById("personal_list_1");
  current_list.classList.add('list_active');
}

//for calendar
else if ( window.location.pathname == '/calendar/personal' ){
  var current_location = document.getElementById("nav_calendar");
  linkColor.forEach(l=> l.classList.remove('active'));
  current_location.classList.add('active');
}

get_category();

//url 지정
var server_url = '';
var url = server_url + '/todo/';

//get_category
function get_category() {
    var url = server_url + '/todo/'
    fetch(url)
        .then(
        function(type){
            return type.json();
        })
        .then(
        function(result){
            var result = result.result;
            for(var i=0; i<result.length; i++){
                var name = result[i].name;
                console.log(name);    
                
                // get titles
                var category = $("<a href='#' class='collapse__sublink' id='category' onclick='location.href=\"/tasks\"'></a>").text(name);
                var br = $("<br>");
                $("#sub_personal_list").append(category, br);
            }
        });
} 
