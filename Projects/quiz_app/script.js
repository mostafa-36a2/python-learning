function httpGetAsync(theUrl, callback) {
    var xmlHttp = new XMLHttpRequest();
    xmlHttp.onreadystatechange = function () {
        if (xmlHttp.readyState == 4 && xmlHttp.status == 200)
            callback(xmlHttp.responseText);
    }
    xmlHttp.open("GET", theUrl, true); // true for asynchronous 
    xmlHttp.send(null);
}

function correct_answer_click(e) {
    console.log(e);
    alert("Correct Answer");
    e.target.classList.add("correct_answer");
    choice_index = e.target.getAttribute("choice-index");
    question_index = e.target.getAttribute("question-index");

    window.localStorage.setItem(`correct-${question_index}`, "1");
}

function wrong_answer_click(e) {
    alert("Wrong Answer");
    e.target.classList.add("wrong_answer");
    choice_index = e.target.getAttribute("choice-index");
    question_index = e.target.getAttribute("question-index");

    window.localStorage.setItem(`wrong-${question_index}-${choice_index}`, "1");
}

window.addEventListener("load", function () {

    httpGetAsync("http://127.0.0.1:5000", function (r) {
        json_obj = JSON.parse(r);

        for (var question_index = 0; question_index < json_obj.length; question_index += 1) {
            qa_div = document.createElement("div");
            qa_div.setAttribute("id", `qa-${question_index}`)

            // Create question
            p = document.createElement("p");
            p.appendChild(
                document.createTextNode(
                    json_obj[question_index].question
                )
            )
            p.setAttribute("id", `question-${question_index}`)
            qa_div.appendChild(p);

            //Create choices
            choices = json_obj[question_index].choices;
            for (var choice_index = 0; choice_index < choices.length; choice_index += 1) {
                button = document.createElement("button");
                button.appendChild(
                    document.createTextNode(
                        choices[choice_index].name
                    )
                )
                button.setAttribute("question-index", question_index);
                button.setAttribute("choice-index", choice_index);
                button.classList.add("choice");



                if (choices[choice_index].state == true) {
                    //button.classList.add("correct_answer");
                    button.addEventListener("click", correct_answer_click);
                    x = window.localStorage.getItem(`correct-${question_index}`) || "0"
                    if (x == "1") {
                        button.classList.add("correct_answer");
                    }
                }
                else {

                    button.addEventListener("click", wrong_answer_click)
                    x = window.localStorage.getItem(`wrong-${question_index}-${choice_index}`) || "0"
                    if (x == "1") {
                        button.classList.add("wrong_answer");
                    }
                }
                qa_div.appendChild(button);
            }

            document.getElementById("questions").appendChild(qa_div);
        }

        return 0;

    });
});

document.getElementById("reset").addEventListener("click", function () {
    localStorage.clear();
    alert("Local storage cleared");
    correct_answer.classList.remove("correct_answer");
    wrong_choices[0].classList.remove("wrong_answer");
    wrong_choices[1].classList.remove("wrong_answer");
    wrong_choices[2].classList.remove("wrong_answer");
})