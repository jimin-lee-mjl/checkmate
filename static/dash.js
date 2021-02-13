var todayContainer = document.querySelector(".today");
var d = new Date();
var weekday = new Array(7);
weekday[0] = "Sunday 🖖";
weekday[1] = "Monday 💪😀";
weekday[2] = "Tuesday 😜";
weekday[3] = "Wednesday 😌☕️";
weekday[4] = "Thursday 🤗";
weekday[5] = "Friday 🍻";
weekday[6] = "Saturday 😴";

var n = weekday[d.getDay()];

var randomWordArray = Array(
  "Oh my, it's ",
  "Whoop, it's ",
  "Happy ",
  "Seems it's ",
  "Awesome, it's ",
  "Have a nice ",
  "Happy fabulous ",
  "Enjoy your "
);
var randomWord =
  randomWordArray[Math.floor(Math.random() * randomWordArray.length)];
todayContainer.innerHTML = randomWord + n;

// prgress
const progress = document.querySelector(".progress-done");

progress.style.width = progress.getAttribute("data-done") + "%";
progress.style.opacity = 1;
