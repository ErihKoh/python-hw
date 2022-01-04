// Add expense Modal
let elem = document.querySelector(".modal");
let instance = M.Modal.init(elem);

let elem2 = document.querySelector("select");
let instance2 = M.FormSelect.init(elem2);

// Add expanse filter

let elem1 = document.querySelector("#expenseFilter");
let instance1 = M.Modal.init(elem1);

let today = new Date();

function formatDate(date) {
  var d = new Date(date),
    month = "" + (d.getMonth() + 1),
    day = "" + d.getDate(),
    year = d.getFullYear();

  if (month.length < 2) month = "0" + month;
  if (day.length < 2) day = "0" + day;

  return [year, month, day].join("-");
}

let nowDay = formatDate(today);
console.log(nowDay);

document.querySelector("#end").setAttribute("max", nowDay);
