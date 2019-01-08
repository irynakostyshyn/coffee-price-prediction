# Сoffee price prediction

What is a Problem? Lack of data for economic prediction tasks.

Methodology :
Use time-series model
Classical time series forecasting methods may be focused on linear relationships, nevertheless, they are sophisticated and perform well on a wide range of problems, assuming that your data is suitably prepared and the method is well configured.
I will use the moving average (MA) method models. A moving average model is different from calculating the moving average of the time series.
The method is suitable for univariate time series without trend and seasonal components

In this task, I have a hidden Markov model of prediction, because I do not have data about an exact amount of coffee bean production, so I will make a  hypothesis that the weather can describe a coffee bean production.


### Data description

Manipulation with data and explanation I did [here](https://github.com/irynakostyshyn/coffee-price-prediction/blob/master/merge_datasets.ipynb)

For price prediction tasks always hard to find an adequate dataset. My task is to collect and preprocess data for such specific tasks.
If you have to work with prices you always need to have economic data such a GDP, GDP per capita, inflation index (CPI) etc.

* GDP - GDP (current US)
* GDP per capita - (current US)
* Agricultural land - (% of land area)
* Rural population
* ICO - mounthly
* Disaster
  - Geophysical(Volcanic activity, Mass movement(dry), Landslide, Earthquake); 
  - Climatological (Wildfire, Drought);
  - Biological (Epidemia, Insect infestation); 
  - Meteorogical (Extreme temperature, Storm, Fog)
  
  
### Data sources :
* [International Coffe Organization](www.ico.org)
* [Université Catholique de Louvain's disaster database](www.emdat.be)
* https://data.oecd.org/
* https://data.worldbank.org/


### Data preprocessing Results 
* [Economical indexes](https://github.com/irynakostyshyn/coffee-price-prediction/blob/master/data/data/clean_data.csv)
* [Data for time series](https://github.com/irynakostyshyn/coffee-price-prediction/blob/master/data/data/data_for_renges.csv)
