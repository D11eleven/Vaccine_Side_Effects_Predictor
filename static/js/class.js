$(document).ready(function() {
    console.log("Page Loaded");

    $("#filter").click(function() {
        makePredictions();
    });
});

function makePredictions() {
    var age_group = $("#age_group").val();
    var sex = $("#sex").val();
    var other_meds = $("#other_meds").val();
    var history = $("#history").val();
    var prior_vax = $("#prior_vax").val();
    var allergies = $("#allergies").val();
    var vax_name = $("#vax_name").val();
    var vax_dose = $("#vax_dose").val();
 
    // create the payload
    var payload = {
        "age_group": age_group,
        "sex": sex,
        "other_meds": other_meds,
        "history": history,
        "prior_vax": prior_vax,
        "allergies": allergies,
        "vax_name": vax_name,
        "vax_dose": vax_dose
    }

    // Perform a POST request to the query URL
    $.ajax({
        type: "POST",
        url: "/makePredictions",
        contentType: 'application/json;charset=UTF-8',
        data: JSON.stringify({ "data": payload }),
        success: function(returnedData) {
            // print it
            console.log(returnedData);

            var pred = JSON.parse(returnedData[0])
            var words = JSON.parse(returnedData[1])

            console.log(pred)
            console.log(words)

            $.each(words, function(index, item) { 
                console.log("Symptom: " + item["key"]);
                console.log("Class: " + item["category"]);
            })
        
        },
        error: function(XMLHttpRequest, textStatus, errorThrown) {
            alert("Status: " + textStatus);
            alert("Error: " + errorThrown);
        }

    });

}