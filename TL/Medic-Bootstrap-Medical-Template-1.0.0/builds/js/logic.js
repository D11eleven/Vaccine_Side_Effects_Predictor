anychart.onDocumentReady(function() {
    var data = [{'x': 'Weakness', 'value': 2600, 'category': 'MILD'},
    {'x': 'Joint Pain/Discomfort', 'value': 2400, 'category': 'MILD'},
    {'x': 'Injection Site Irritation/Discomfort',
     'value': 2400,
     'category': 'MILD'},
    {'x': 'Chills', 'value': 1700, 'category': 'MILD'},
    {'x': 'Fever', 'value': 1700, 'category': 'MILD'},
    {'x': 'Back pain', 'value': 900, 'category': 'MILD'},
    {'x': 'Respiratory distress', 'value': 800, 'category': 'MODERATE'},
    {'x': 'Itching', 'value': 700, 'category': 'MILD'},
    {'x': 'Migraine/Headache', 'value': 600, 'category': 'MILD'},
    {'x': 'Fatigue', 'value': 500, 'category': 'MILD'},
    {'x': 'Blood Pressure Change', 'value': 500, 'category': 'MILD'},
    {'x': 'Muscle Aches/Pain/Tightness', 'value': 500, 'category': 'MILD'},
    {'x': 'Nausea/Vomiting', 'value': 400, 'category': 'MILD'},
    {'x': 'Abdominal Pain/Discomfort', 'value': 400, 'category': 'MILD'},
    {'x': 'Chest Discomfort', 'value': 400, 'category': 'MILD'},
    {'x': 'Anxiety', 'value': 400, 'category': 'MILD'},
    {'x': 'Muscle Spasms', 'value': 300, 'category': 'MILD'},
    {'x': 'Vertigo', 'value': 200, 'category': 'MILD'},
    {'x': 'Skin sensitivity', 'value': 200, 'category': 'MILD'},
    {'x': 'Alterred Vision', 'value': 200, 'category': 'MODERATE'},
    {'x': 'Skin Rash', 'value': 200, 'category': 'MILD'},
    {'x': 'Sensitivity', 'value': 200, 'category': 'MILD'},
    {'x': 'Diarrhea', 'value': 200, 'category': 'MILD'},
    {'x': 'Cough', 'value': 200, 'category': 'MILD'},
    {'x': 'Oral discomfort', 'value': 100, 'category': 'MILD'},
    {'x': 'Under Arm Pain', 'value': 100, 'category': 'MILD'},
    {'x': 'Runny Nose', 'value': 100, 'category': 'MILD'},
    {'x': 'Pulmonary', 'value': 100, 'category': 'SEVERE'},
    {'x': 'Facial Paralysis', 'value': 100, 'category': 'MODERATE'},
    {'x': 'Appetite Decreased', 'value': 100, 'category': 'MILD'},
    {'x': 'Feeling Abnormal', 'value': 100, 'category': 'MILD'},
    {'x': 'Coordination dysfunction', 'value': 100, 'category': 'MILD'},
    {'x': 'Difficulty swallowing', 'value': 100, 'category': 'MILD'},
    {'x': 'Inflammation/Swelling', 'value': 100, 'category': 'MILD'},
    {'x': 'Heart Attack', 'value': 100, 'category': 'SEVERE'},
    {'x': 'Flushing', 'value': 100, 'category': 'MILD'},
    {'x': 'Eye Discharge', 'value': 100, 'category': 'MILD'},
    {'x': 'High blood pressure', 'value': 100, 'category': 'MODERATE'}]

   // create a tag (word) cloud chart
    var chart = anychart.tagCloud(data);
  
     // set a chart title
    //chart.title('Top 20 Symptoms')
    // set an array of angles at which the words will be laid out
    chart.angles([0, 90])
    // enable a color range
    chart.colorRange(true);
    // set the color range length
    chart.colorRange().length('80%');

    chart.textSpacing(.5)

    chart.tooltip().format("{%yPercentOfTotal}%");
  
    // display the word cloud chart
    chart.container("cloud");
    chart.draw();

    chart.listen("pointClick", function(e){
      var url = "https://www.merriam-webster.com/dictionary/" + e.point.get("x");
      window.open(url, "_blank");
    });

  });
