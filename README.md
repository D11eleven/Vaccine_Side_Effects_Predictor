
<div id="top"></div>

# PROJECT-4&nbsp; &nbsp;    VACCINE SIDE EFFECTS PREDICTOR


<!-- <div align="center"> -->

### [Vaccine Side Effects Predictor](https://dashboard.heroku.com/apps/utsaproject-4)


![CovidShot](https://www.coe.int/documents/10518249/88399762/Covid-Vaccine/23edacee-ac47-953e-7c8d-012ec176c157?t=1611227091000)


<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li><a href="#1Background ">About The Project</a></li>
    <li><a href="#2Inspiration ">Inspiration</a></li>
    <li><a href="#3Process">Process</a></li>
      <ul>
         <li><a href="#Tools">Tools</a></li>
      </ul>
    <li><a href="#6Tools">Tools</a></li>
    <li><a href="#7Data-Sources">Data Sources</a></li>
    <li><a href="#8The Team">Team</a></li>
  </ol>
</details>

## 1Background 

The Vaccine Adverse Event Reporting System (VAERS) was created by the FDA and CDC to receive reports about adverse events that may be associated with 
vaccinations world wide, including the COVID-19 vaccines. Physicians and vaccine providers are encouraged to report adverse events after a vaccination.

## 2Inspiration 

How can we support individuals to understand what side effects they may experience from a Covid Vaccination based on vaccine manufacturer, their age, prior 
allergies, medical history and gender.  Create a model to predict the possible side effects in the categories of_ Mild, Moderate, or Severe._ 

* Dataset from Kaggle [COVID-19 Vaccine Adverse Event Reporting System](https://www.kaggle.com/ayushggarg/covid19-vaccine-adverse-reactions?select=2021VAERSSYMPTOMS.csv) 
* 
<p align="right">(<a href="#top">back to top</a>)</p>


## 3Our Process

### Tools
- Machine Learning Models/KNN/LinearRegression/xxx
- Python/Pandas/Flask
- Jupyter Notebook
- Matplotlib/Plotly/D3/[Bootstrap](https://getbootstrap.com)
- Tableau

Our original data sources contained nearly 2 million records before ETL. Our team used Pandas and Python to extract and clean data relevant to Texas. These remaining records were then imported into a local Postgres database and deployed to a Postgres Heroku cloud server. 

A Python Flask App was written to facilitate the retrieval of data in the postgres database coming from user requests via the dashboard. It was then deployed using Heroku to create a fully functional Web App.  

The final web application uses Heroku and Flask to retrieve data and Plotly, Leaflet, and Chart.js to render.

<p align="right">(<a href="#top">back to top</a>)</p>

## 4Data Clean UP 

*
<p align="right">(<a href="#top">back to top</a>)</p>

## 5Machine Learning Model
 
 * KNN
 * 
<p align="right">(<a href="#top">back to top</a>)</p>

## 6Future  

Sources: 
<p align="right">(<a href="#top">back to top</a>)</p>








## 7Data Sources
 
[COVID-19 Vaccine Adverse Event Reporting System](https://www.kaggle.com/ayushggarg/covid19-vaccine-adverse-reactions?select=2021VAERSSYMPTOMS.csv) 
<br>

[VAERS](https://vaers.hhs.gov/)

<p align="right">(<a href="#top">back to top</a>)</p>
  
## 8The Team
[Amy Bednarz](https://github.com/abednarz210) ---|--- [Darrell Horich](https://github.com/D11eleven) ---|--- [Taylor Lyons](https://github.com/taylorsyde) ---|--- [Samantha Perez](https://github.com/Sjenn257)
  
<p align="right">(<a href="#top">back to top</a>)</p>

