document.addEventListener("DOMContentLoaded", function () {
  let sidenav = document.querySelectorAll(".sidenav");
  M.Sidenav.init(sidenav);
});

let datePicker = document.querySelectorAll(".datepicker");
M.Datepicker.init(datePicker, {
  format: "dd mmmm, yyyy",
  i18n: { done: "Select" },
});

let selects = document.querySelectorAll('select');
M.FormSelect.init(selects);

let collapsibles = document.querySelectorAll('.collapsible');
M.Collapsible.init(collapsibles);