# Breast Cancer Detection & Visualizatin

This Python script utilizes the scikit-learn library to perform breast cancer classification using the K-Nearest Neighbors algorithm. Additionally, it generates a heatmap to visualize the correlation between different features of the dataset.


**Overview:**
The script performs the following tasks:

-Loads the breast cancer dataset using load_breast_cancer from scikit-learn.
-Splits the dataset into training and testing sets using train_test_split.
-Trains a K-Nearest Neighbors classifier (KNeighborsClassifier) on the training data.
-Prints the accuracy score of the classifier on the testing data.
-Predicts the class label of a randomly generated sample using the trained classifier.
-Constructs a Pandas DataFrame to combine the dataset features and target labels.
-Visualizes the correlation between features using a heatmap with seaborn and matplotlib libraries.


**Requirements:**
-Python 3
-scikit-learn
-pandas
-numpy
-matplotlib
-seaborn


This is a simple code that performs binary classification on a pre-existing dataset from the sci-kit library and mainly works on the KNN algorithm
