var requestOptions = {
    method: 'GET',
    redirect: 'follow'
  };
  
  fetch("http://127.0.0.1:5000/", requestOptions)
    .then(response => response.text())
    .then(result => console.log(JSON.parse(result)))
    .catch(error => console.log('error', error));


document.querySelector("#form1").addEventListener("submit",function(e){
  e.preventDefault();
  info_body = {
    user_name: document.querySelector("#name").value,
    user_password: document.querySelector("#password").value
  }
  fetch("http://127.0.0.1:5000/login", {
    method: "POST",
    headers: {'Content-Type': 'application/json'},
    body: JSON.stringify(info_body),
  })
    .then(response => response.text())
    .then(result => console.log(result))
    .catch(error => console.log('error', error));
    return
})
952863