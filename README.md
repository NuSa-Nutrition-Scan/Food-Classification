<h1>Food Classification</h1>
<p>
This repository contains code to detect a food and find out the nutrients contained in it. This project aims to help users find out what types of food and nutrients are contained in these foods so that users can adjust their daily nutritional needs.

Through the research we have done, we found one approach to find a solution to the problem. We use the Transfer Learning approach with the help of Libraries from TensorFlow.
</p>

<h2>Overview</h2>
<p><img align="left" src="https://github.com/NuSa-Nutrition-Scan/Food-Detection/assets/81479217/61e4be79-ade6-4cd4-90a5-69ecc4c4965c" alt="overview" /></p>
<p>Program flow is as follows :</p>
<ul>
  <li>We upload the image of the food we want to detect.</li>
  <li>Then click the submit button.</li>
  <li>The food image will be processed and then output in the form of the name of the food contained in the image.</li>
  <li>The output from the gradio API in Hugging Face will be a JSON File that contains the food name and percentage of predicted confidence.</li>
</ul>

<h2>How to Replicate Process</h2>
<ol>
  <li>First clone this repository using comment "git clone git@github.com:NuSa-Nutrition-Scan/Food-Classification.git"</li>
  <li>install requirements needed</li>
  <li>If you want to do training data, you can access it at Computer Vision.ipynb</li>
  <li>If you want to do a deployment to run the script, you can use Demo-deploy-with-gradio.py</li>
</ol>

<h2>Directory Structure</h2>
<ol>
  <li>my_model_1</li>
  Folder of Food Classification saved models that contain model architecture and weights of parameters.
  
  <li>Computer Vision.ipynb</li>
  Jupyter Notebook for building and training Food Classification Models that include pre-processing untill deployment with help of gradio library
  
  <li>Demo-deploy-with-gradio</li>
  With the Python script that we use for building the model in Hugging Face, we deploy our Food Classification model with the help of the Gradio library, which can
  produce a GUI for the use of machine learning models.
  
  <li>requirements.txt</li>
  List of python package that we use to training and deploying our food classification model
</ol>


<h2>Branches in This Repository</h2>
<ol>
  <li>In this feature, we use three branches where everyone tries to get the most effective model accuracy.</li>
</ol>



