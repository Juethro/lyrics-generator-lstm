// const getBtn = document.getElementById('get')
const sendBtn = document.getElementById('submit')

// getBtn.addEventListener('click', function(){
//     fetch('http://localhost:5000', {
//     method:'GET'
// })
//     .then(res => res.json())
//     .then(data => console.log(data))
// });

sendBtn.addEventListener('click', function(){
    let inp_1 = document.getElementById('in-1').value;
    let inp_2 = document.getElementById('in-2').value;
    let inp_3 = document.getElementById('in-3').value;
    let inp_4 = document.getElementById('in-4').value;

    fetch('http://localhost:5000', {
    method:'POST',
    mode: 'no-cors',
    headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json'
    },
    body: JSON.stringify({
        'inp_1': inp_1,
        'inp_2': inp_2,
        'inp_3': inp_3,
        'inp_4': inp_4
    })
})
    .then(res => res.json())
    .then(json => {
        var ut = JSON.stringify(json);
        var out = JSON.parse(ut);
        document.getElementById('out-1').innerHTML = out['inp_1'];
        document.getElementById('out-2').innerHTML = out['inp_2'];
        document.getElementById('out-3').innerHTML = out['inp_3'];
        document.getElementById('out-4').innerHTML = out['inp_4'];
    })
});
