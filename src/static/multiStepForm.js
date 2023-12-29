/*
Credits: https://w3sniff.com/code?id=102&title=Multi-Step-Form-with-Tailwind-CSS
*/

console.log("hello");
var currentTab = 0; // Current tab is set to be the first tab (0)
showTab(currentTab); // Display the current tab

function showTab(n) {
  // This function will display the specified tab of the form...
  var x = document.getElementsByClassName("step");
  x[n].style.display = "block";
  //... and fix the Previous/Next buttons:
  if (n == 0) {
    document.getElementById("prevBtn").style.display = "none";
  } else {
    document.getElementById("prevBtn").style.display = "inline";
  }
  if (n == x.length - 1) {
    document.getElementById("nextBtn").innerHTML = "Submit";
  } else {
    document.getElementById("nextBtn").innerHTML = "Next";
  }
  //... and run a function that will display the correct step indicator:
  fixStepIndicator(n);
}

function nextPrev(n) {
  console.log(n);
  // This function will figure out which tab to display
  var x = document.getElementsByClassName("step");
  // Exit the function if any field in the current tab is invalid:
  if (n == 1 && !validateForm()) return false;
  // Hide the current tab:
  x[currentTab].style.display = "none";
  // Increase or decrease the current tab by 1:
  currentTab = currentTab + n;
  // if you have reached the end of the form...
  console.log(currentTab);
  if (currentTab >= x.length) {
    // ... the form gets submitted:
    document.getElementById("multiStepForm").submit();
    return false;
  }
  // Otherwise, display the correct tab:
  showTab(currentTab);
}

function validateForm() {
  // This function deals with validation of the form fields
  var x,
    y,
    i,
    valid = true;
  x = document.getElementsByClassName("step");
  y = x[currentTab].getElementsByTagName("input");
  // A loop that checks every input field in the current tab:
  for (i = 0; i < y.length; i++) {
    // If a field is empty...
    if (y[i].value == "") {
      // add an "invalid" class to the field:
      y[i].className += " invalid";
      // and set the current valid status to false
      valid = false;
    }
  }
  // If the valid status is true, mark the step as finished and valid:
  if (valid) {
    document.getElementsByClassName("stepIndicator")[currentTab].className +=
      " finish";
  }
  return valid; // return the valid status
}

function fixStepIndicator(n) {
  // This function removes the "active" class of all steps...
  console.log("fix step indicator");
  console.log(n);
  var i;
  var x = document.getElementsByClassName("stepIndicator");
  var y = document.getElementsByClassName("stepIndicatorBorder");
  for (i = 0; i < x.length; i++) {
    x[i].className = x[i].className.replace(
      " text-primary-600 dark:text-primary-500",
      ""
    );
    y[i].className = y[i].className.replace(
      " border-primary-600 dark:border-primary-500",
      ""
    );
  }
  //... and adds the "active" till the current step:
  for (i = 0; i <= n; i++) {
    x[n].className += "  text-primary-600 dark:text-primary-500";
    y[n].className += " border-primary-600 dark:border-primary-500";
  }
}
