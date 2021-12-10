
<div id="top"></div>

# &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;  COVID-19 VACCINE SIDE EFFECTS PREDICTOR


<!-- <div align="center"> -->

###  [Vaccine Side-Effects Predictor](https://vaccine-side-effect-predictor.herokuapp.com/)


![CovidShot](https://www.coe.int/documents/10518249/88399762/Covid-Vaccine/23edacee-ac47-953e-7c8d-012ec176c157?t=1611227091000)

<br>

<!-- TABLE OF CONTENTS -->

<details>
  <summary>Table of Contents</summary>
    <li><a href="#1 Background ">Background</a></li>
    <li><a href="#2 Inspiration and Motivation ">Inspiration and Motivation</a></li>
    <li><a href="#3 Our Process ">Our Process</a></li>
      <ul>
         <li><a href="#Tools">Tools</a></li>
      </ul>
    <li><a href="#4 Data-Clean-UP">Data Clean Up </a></li>
    <li><a href="#5 Machine-Learning-Model">Machine Learning Model</a></li>
    <li><a href="#6 Conclusion”>Conclusion</li>
    <li><a href="#7 Sources">Sources</a></li>
    <li><a href="#8 The-Team">Team</a></li>
  </ol>
</details>

# **What Could You Expect After Your Covid Vaccine?**  
  
## **Background** 

The Vaccine Adverse Event Reporting System [VAERS](https://vaers.hhs.gov/reportevent.html) was created by the FDA and CDC to recieve and compile reports about 
the adverse events that may be associated vaccinations world wide, including the COVID-19 vaccines. Physicians and vaccine providers are encouraged to report adverse events after a vaccination. We used Kaggle [COVID-19 Vaccine Adverse Event Reporting System](https://www.kaggle.com/ayushggarg/covid19-vaccine-adverse-reactions?select=2021VAERSSYMPTOMS.csv) to gather vaccine records. 
  
<p align="right">(<a href="#top">back to top</a>)</p>

## **Inspiration and Motivation**

Support individuals to understand what side effects they may experience from Covid Vaccination based on reported side effects from previous vaccine 
addministration.  Our site uses machine learning to decipherthe input from user shared data that includes vaccine manufacturer, age, prior known allergies, 
medical history and gender.  The machine learning model predicts the possible side effects in the categories of Mild, Moderate, or Severe using the KNN model to
determine possible side effects unique to each user. 

<p align="right">(<a href="#top">back to top</a>)</p>


## **Our Process**
Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliqu

### **Tools**
  
* Machine Learning Models/KNN
* Python
* Pandas
* Flask
* WordCloud
* Heroku
* Matplotlib/Plotly/D3/Bootstrap
* Jupyter Notebook
* Tableau
  
<!-- Tools -->
<details>
  <summary>Tools</summary>
    <li><a href="# Machine_Learning Models/KNN ">Machine_Learning Models/KNN </a></li>
    <li><a href="# Python ">Python</a></li>
    <li><a href="# Pandas ">Pandas</a></li>
    <li><a href="# Flask ">Flask</a></li>
    <li><a href="# Wordcloud ">Wordcloud</a></li>
    <li><a href="# Matplotlib/Plotly/DS3/Bootstrap ">Matplotlib/Plotly/DS3/Bootstrap</a></li>
    <li><a href="# Tableau ">Tableau</a></li>
    <li><a href="# Jupyter_Notebook ">Jupyter Notebook</a></li>
  </ol>
</details>
  

"Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat

"Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.  
"Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat

<p align="right">(<a href="#top">back to top</a>)</p>


![image (1)](https://user-images.githubusercontent.com/82190357/145183563-27e1b7f1-a28e-4401-9172-fcd23046e5f3.png)

## **Data Clean UP** 
  
  * ETL 
    * Remove Non-Covid Vaccine Data 
    * Symptom categorical groupings 
  
"Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat
<p align="right">(<a href="#top">back to top</a>)</p>

## **Machine Learning Model**
  
  * KNN to take in user input data and return symptoms categories and examples 
 
 "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat
 
<p align="right">(<a href="#top">back to top</a>)</p>

## **Conclusion** 

Challenges

As data scientists, we have limited medical expertise and many medical symptom terms had to be researched, resulting in the subjective assignment of category
groups and the classification of severity of symptoms as Mild, Moderate, Severe. 

Future Implications

* If we were given more time and resources our site is scalable. The data is readily available for all vaccinations so we could ptoentially expand to become a
  general vaccine information site to reassure patients about future risks to make informed decisions when considering upcoming vaccinations. 

* We would go directly to the source instead of Kaggle and extract data from the beginning of COVID vaccinations to now for more data.

* Recruit a medical professional to decipher mild, moderate, severe side effect classess and review quality of data.

* Further deep dive to examine the non-side effect patient data for trends that were reported to get an even better probability.
  
  

<p align="right">(<a href="#top">back to top</a>)</p>

![image](https://raw.githubusercontent.com/D11eleven/Vaccine_Side_Effects_Predictor/main/Resources/Tab1.png)

## **Sources**
 
[COVID-19 Vaccine Adverse Event Reporting System](https://www.kaggle.com/ayushggarg/covid19-vaccine-adverse-reactions?select=2021VAERSSYMPTOMS.csv) 
<br>

[VAERS](https://vaers.hhs.gov/)
  
[Medicine.net](https://www.medicinenet.com/medterms-medical-dictionary/article.htm)

<p align="right">(<a href="#top">back to top</a>)</p>
  
##  **The Team**
[Amy Bednarz](https://github.com/abednarz210) ---|--- [Darrell Horich](https://github.com/D11eleven) ---|--- [Taylor Lyons](https://github.com/taylorsyde) ---|--- [Samantha Perez](https://github.com/Sjenn257)

  
 > The mind, in addition to medicine, has the power to turn the immune system around. -Jonas Salk  
  
<p align="right">(<a href="#top">back to top</a>)</p>

