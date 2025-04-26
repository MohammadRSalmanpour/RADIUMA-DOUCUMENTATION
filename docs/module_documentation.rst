Module Documentation
===================

.. contents:: :local:

Preprocessing
------------

Overview
^^^^^^^^

The preprocessing module provides essential data preparation capabilities before applying machine learning algorithms. Proper preprocessing is crucial for achieving optimal model performance.

Supported Preprocessing Techniques
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Data Encoding**

* **Label Encoder**: Transforms categorical labels to numerical values
* **One-Hot Encoder**: Converts categorical features to binary vectors
* **Target Encoder**: Replaces categories with target mean values

**Data Cleaning**

* **Missing Value Imputation**: Multiple strategies for handling null values
* **Outlier Detection**: Methods to identify and handle outliers
* **Feature Scaling**: Normalize/standardize data for consistent ranges

**Feature Engineering**

* **Polynomial Features**: Creates interaction features
* **Feature Selection**: Methods to identify most relevant variables
* **Dimensionality Reduction**: PCA, t-SNE, and other techniques

Key Preprocessing Algorithms
^^^^^^^^^^^^^^^^^^^^^^^^^^^

* **Principal Component Analysis (PCA)**: Linear dimensionality reduction using SVD
* **Kernel PCA**: Non-linear dimensionality reduction 
* **Factor Analysis**: Linear dimensionality reduction using factor analysis
* **Fast ICA**: Independent Component Analysis

Workflow Integration
^^^^^^^^^^^^^^^^^^

1. Data Loading
2. Encoding
3. Data Splitting
4. Imputation
5. Scaling
6. Feature Selection
7. Model Training

Best Practices
^^^^^^^^^^^^

1. Always encode categorical variables
2. Handle missing values appropriately
3. Scale features for better performance
4. Select relevant features to reduce dimensionality
5. Keep random states consistent for reproducibility
6. Use cross-validation for reliable evaluation
7. Reserve test data until final evaluation

Classification
------------

Overview
^^^^^^^^

The Classification module provides multiple algorithms for data analysis with customizable parameters through an intuitive user interface.

Supported Algorithms
^^^^^^^^^^^^^^^^^^

**1. Logistic Regression Classifier**

A linear model for classification that predicts class probabilities.

**Key Parameters:**

* Penalty (L1, L2, Elasticnet, None)
* Regularization Strength (C)
* Solver (Lbfgs, Liblinear, etc.)
* Multi-class Option

**2. K-Nearest Neighbors Classifier**

Non-parametric method using closest training examples.

**Key Parameters:**

* Number of Neighbors
* Weights (Uniform, Distance)
* Distance Metric
* Algorithm (Auto, Ball_tree, Kd_tree, Brute)

**3. Decision Tree Classifier**

Creates a model predicting targets by learning decision rules.

**Key Parameters:**

* Criterion (gini, entropy, log_loss)
* Max Depth
* Min Samples Split/Leaf
* Class Weight

**4. Support Vector Machines (SVM)**

Finds optimal hyperplane to separate classes.

**Key Parameters:**

* Kernel (linear, poly, rbf, sigmoid)
* Regularization Parameter (C)
* Gamma
* Degree (for poly kernel)

**5. AdaBoost Classifier**

Ensemble method using weak classifiers on modified data versions.

**Key Parameters:**

* Base Estimator
* Number of Estimators
* Learning Rate
* Algorithm (SAMME, SAMME.R)

**6. Bagging Classifier**

Ensemble using base classifiers on random data subsets.

**Key Parameters:**

* Base Estimator
* Number of Estimators
* Bootstrap option
* Sample and Feature ratios

**7. Naive Bayes (GaussianNB)**

Applies Bayes' theorem with feature independence assumption.

Classification Workflow
^^^^^^^^^^^^^^^^^^^^^

1. Select and configure algorithms
2. Apply preprocessing steps
3. Train models
4. Evaluate using standard metrics
5. Compare algorithm performance

Regression
---------

Overview
^^^^^^^^

The Regression module provides multiple algorithms for predicting continuous target variables.

Supported Algorithms
^^^^^^^^^^^^^^^^^^

**1. Linear Regression**

Standard approach estimating linear relationships between variables.

**Key Parameters:**

* Fit Intercept
* Positive Constraints

**2. Ridge Regression**

Linear model with L2 regularization to reduce overfitting.

**Key Parameters:**

* Alpha (regularization strength)
* Solver
* Fit Intercept
* Max Iterations

**3. Lasso Regression**

Linear model with L1 regularization promoting sparse coefficients.

**Key Parameters:**

* Alpha
* Selection method (cyclic, random)
* Max Iterations
* Tolerance

**4. Logistic Regression for Regression**

Adapts logistic regression for regression tasks.

**Key Parameters:**

* Penalty
* Regularization Strength
* Solver
* L1 Ratio (for elasticnet)

**5. AdaBoost Regression**

Ensemble method using weak regressors.

**Key Parameters:**

* Base Estimator
* Loss function
* Learning Rate
* Number of Estimators

**6. Bagging Regression**

Ensemble method aggregating predictions from multiple models.

**Key Parameters:**

* Base Estimator
* Number of Estimators
* Bootstrap option
* Sample and Feature ratios

Evaluation Metrics
^^^^^^^^^^^^^^^^

* Mean Absolute Error (MAE)
* Root Mean Squared Error (RMSE)
* R-squared Score
* Median Absolute Error

Clustering
---------

Overview
^^^^^^^^

The Clustering module provides algorithms for grouping similar data points without labeled training data.

Supported Algorithms
^^^^^^^^^^^^^^^^^^

**1. K-Means Clustering**

Partitions observations into k clusters with nearest mean.

**Key Parameters:**

* Number of Clusters
* Initialization Method
* Number of Initializations
* Max Iterations

**2. Agglomerative Clustering**

Hierarchical approach building nested clusters.

**Key Parameters:**

* Number of Clusters
* Linkage criterion
* Distance Metric
* Compute Distances option

**3. K-Mode Clustering**

Specialized for categorical data.

**Key Parameters:**

* Number of Clusters
* Initialization Method
* Number of Initializations
* Max Iterations

**4. Gaussian Mixture Model**

Probabilistic model assuming data from Gaussian distributions mixture.

**Key Parameters:**

* Number of Components
* Covariance Type
* Initialization Parameters
* Tolerance 