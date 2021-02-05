// delete request
export default function deleteCategory(id) {
    const URL = "/todo/";
    const delCategoryBtn = document.querySelector("#category_delete_btn");
    const option = {
      method: "DELETE",
      body: JSON.stringify({
        category_id: id,
      }),
      headers: {
        "Content-Type": "application/json",
      },
    };
  
    if (delCategoryBtn) {
      delCategoryBtn.addEventListener('click', function() {
        console.log('hi');
        fetch(URL, option)
        .then(function (type) {
          return type.json();
        })
        .then(function (result) {
          console.log(result);
          if (result.status === "success") {
            window.location.replace("/dashboard");
          } else {
            alert("Sorry, can not delete this category.");
          }
        });
      });
    }
  }