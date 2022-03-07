<h2>Poseidon A.I.</h2>
<p>Data Engineering project using Machine Learning to create A.I. predicting death and its probability from Covid-19.</p>

<h3>Description</h3>
<p>The A.I. is for Polish residents (build on data from Polish Ministry of Health). It predicts both outcome and probability of death caused by Covid-19 infection. It can predict the result for a certain day of the year - this means the result will be valid only if the subject will get infected that certain day. In simple terms it shows when the infection is most dangerous for the certain person.</p>

<h3>Technical description</h3>
<p>Model is built with Python using Pandas Dataframes and Scikit-Learn libraries. Process is divided to 4 steps (corresponding to 4 files):</p>
<ul>
  <li>datasets.py - normalizing the data (cleaning, formating, preparing for merging) and saving to new csv files</li>
  <li>combined_dataset.py - merging both datasets by trying to match an infection for every death case and adding new one if not found</li>
  <li>AI_model.py - building A.I. model from merged data with Logistic Regression and saving to a file</li>
  <li>AI_program - result delivery program that uses saved model and subject data</li>
</ul>

<h3>Installation</h3>
<p>The only thing needed is Python interpreter / environment. There are sample datasets in /data folder that are compatible with Ministry of Health and project format. When you have the model to get a result you must fill variables in the code with your data.*</p>
<p>* TERYT is the terytorial / geo code used by Polish public administration.</p>

<br>
<p>All rights reserved. It is portfolio application only.</p>
