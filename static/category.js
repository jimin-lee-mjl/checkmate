// delete request
function deleteCategory(url, category_id) {
  const option = {
    method: "DELETE",
    body: JSON.stringify({
      category_id: category_id,
    }),
    headers: {
      "Content-Type": "application/json",
    },
  };

  fetch(url, option)
    .then(function (type) {
      return type.json();
    })
      .then(function (result) {
        if (result.status === "success") {
          window.location.replace("/dashboard");
        } else {
          alert("Sorry, can not delete this category.");
        }
      });
}

// function deleteTodos(url, category_id) {
//   fetch(url+category_id)
//     .then(function(type) {
//       return type.json();
//     })
//       .then(function(result) {
//         const todos = result.result;
//         for (let i=0; i<todos.length; i++) {
//           const option = {
//             method: "DELETE",
//             body: JSON.stringify({
//               todo_id: todos[i].id,
//             }),
//             headers: {
//               "Content-Type": "application/json",
//             },
//           };

//           fetch(url+category_id, option);
//         }
//       })
//         .then(function(result) {
//           console.log(result);
//           deleteCategory(url, category_id);
//         })
// }

function handleDelCategoryBtn() {
  const category_id = window.location.search.split('?category_id=')[1].split('&')[0];
  const delCategoryBtn = document.querySelector("#category_delete_btn");
  const URL = "/todo/";
  
  if (delCategoryBtn) {
    delCategoryBtn.addEventListener("click", function() {
      deleteCategory(URL, category_id);
    })
  }
}

function init() {
  handleDelCategoryBtn();
}

init();