// const getBtn = document.getElementById('get');
// const submitBtn = document.getElementById('submit');

// const getData = () => {
//     axios.get('http://localhost:5000')
//     .then(response => {
//         console.log(response)
//     })
//     .then(function (data) {
//         document.getElementById('wawaw').innerHTML = `Total is ${data}`
//     })
// };

// getBtn.addEventListener('click', getData);
function submitForm() {
    var http = new XMLHttpRequest();
    http.open("POST", "http://localhost:5000", true);
    http.setRequestHeader("Content-type","application/x-www-form-urlencoded");
    var params = "search=" + document.getElementById('wawaw'); // probably use document.getElementById(...).value
    http.send(params);
    http.onload = function() {
        alert(http.responseText);
    }
}