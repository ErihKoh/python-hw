// Add expense Modal
let elem = document.querySelector(".modal");
let instance = M.Modal.init(elem);

let elem2 = document.querySelector("select");
let instance2 = M.FormSelect.init(elem2);

// Add expanse filter

let elem1 = document.querySelector("#expenseFilter");
let instance1 = M.Modal.init(elem1);

// date

function formatDate(date) {
  let d = new Date(date),
    month = "" + (d.getMonth() + 1),
    day = "" + d.getDate(),
    year = d.getFullYear();

  if (month.length < 2) month = "0" + month;
  if (day.length < 2) day = "0" + day;

  return [year, month, day].join("-");
}

let today = new Date();
let nowDay = formatDate(today);
let startDate = document.querySelector("#start");
let endDate = document.querySelector("#end");
let expenseDate = document.querySelector("#dateExpense");

expenseDate.setAttribute("max", nowDay);
endDate.setAttribute("max", nowDay);
startDate.setAttribute("max", nowDay);
endDay.setAttribute("value", nowDay);
