username = document.getElementById("name")
cls = document.getElementById("class")
age = document.getElementById("age")
submit_btn = document.getElementById("submit")

get_name = document.getElementById("get_name")
get_cls = document.getElementById("get_class")
get_age = document.getElementById("get_age")
fetch_btn = document.getElementById("fetch")

submit_btn.addEventListener("click", async function(){
    let url = `http://127.0.0.1:5000/addStudent?username=${username.value}&class=${cls.value}&age=${age.value}`

    try {
        let response = await fetch(url)

        let data = await response.json()
        
        alert(data['message'])
    } 
    catch (error) {
        console.error(error)
        alert(error)
    }
})

fetch_btn.addEventListener("click", async function() {
    let url = `http://127.0.0.1:5000/getStudent/${get_name.value}`

    try {
        let response = await fetch(url)

        let data = await response.json()
        
        alert(data['message'])

        get_cls.placeholder = data['class']
        get_age.placeholder = data['age']
    } 
    catch (error) {
        console.error(error)
        alert(error)
    }
})