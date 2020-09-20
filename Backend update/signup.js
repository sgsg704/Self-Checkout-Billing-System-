document.getElementById("verifyform").addEventListener("submit", saveitem);
var fs = require("fs");
function saveitem(e) {
  const jsonstring = fs.readFileSync("./customer.json", "utf-8");

  var signnemail = document.getElementById("signupemail").Value;
  var signname = document.getElementById("signupemail").Value;
  var signnpassword = document.getElementById("signupemail").Value;
  var person = {
    email: signnemail,
    name: signname,
    password: signnpassword,
  };
  var persons = JSON.parse(jsonstring);
  persons.push(person);
  fs.writeFile("./customer.json", JSON.stringify(person), (err) => {
    if (err) {
      console.log(err);
    } else {
      console.log("File written successfully");
    }
  });
  document.getElementById("verifyform").reset();
  e.preventDefault;
}
