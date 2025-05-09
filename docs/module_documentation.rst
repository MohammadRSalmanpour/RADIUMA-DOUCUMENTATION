Module Documentation
====================

.. contents:: :local:

Preprocessing
-------------

Overview
^^^^^^^^

The preprocessing module provides essential data preparation capabilities before applying machine learning algorithms. Proper preprocessing is crucial for achieving optimal model performance.

Supported Preprocessing Techniques
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

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
--------------

Overview
^^^^^^^^

The Classification module provides multiple algorithms for data analysis with customizable parameters through an intuitive user interface.

Supported Algorithms
^^^^^^^^^^^^^^^^^^^^

**1. Logistic Regression Classifier**

A linear model for classification that predicts class probabilities.

**Key Parameters:**

* **Penalty**: Regularization type (L1, L2, Elasticnet, None)
* **Regularization Strength (C)**: Inverse of regularization strength (default: 1.0)
* **Solver**: Algorithm for optimization (lbfgs, liblinear, newton-cg, sag, saga)
* **Multi-class Option**: How to handle multi-class data (auto, ovr, multinomial)
* **Max Iterations**: Maximum iterations for solver (default: 100)
* **Random State**: Seed for reproducibility (default: 43)
* **Class Weight**: Balance classes by weights (None or 'balanced')

**2. K-Nearest Neighbors Classifier**

Non-parametric method using closest training examples.

**Key Parameters:**

* **Number of Neighbors**: K value for nearest neighbors
* **Weights**: How to weight neighbors (Uniform, Distance)
* **Distance Metric**: Method for calculating distances (euclidean, manhattan, etc.)
* **Algorithm**: Search method (Auto, Ball_tree, Kd_tree, Brute)

**3. Decision Tree Classifier**

Creates a model predicting targets by learning decision rules.

**Key Parameters:**

* **Criterion**: Function to measure split quality (gini, entropy, log_loss)
* **Max Depth**: Maximum depth of the tree
* **Min Samples Split**: Minimum samples required to split node
* **Min Samples Leaf**: Minimum samples required at leaf node
* **Class Weight**: Class weights (None, 'balanced')
* **Random State**: Seed for reproducibility (default: 43)

**4. Support Vector Machines (SVM)**

Finds optimal hyperplane to separate classes.

**Key Parameters:**

* **Kernel**: Kernel type (linear, poly, rbf, sigmoid)
* **Regularization Parameter (C)**: Regularization strength (default: 1.0)
* **Gamma**: Kernel coefficient for 'rbf', 'poly' and 'sigmoid' (scale, auto)
* **Degree**: Degree for poly kernel
* **Decision Function Shape**: Shape of decision function (ovr, ovo)
* **Class Weight**: Class weights (None, 'balanced')

**5. AdaBoost Classifier**

Ensemble method using weak classifiers on modified data versions.

**Key Parameters:**

* **Base Estimator**: Base estimator type (DecisionTreeClassifier, SVC, etc.)
* **Number of Estimators**: Boosting iterations (default: 50)
* **Learning Rate**: Weight applied to each classifier (default: 1.0)
* **Algorithm**: Boosting algorithm (SAMME, SAMME.R)
* **Random State**: Seed for reproducibility

**6. Bagging Classifier**

Ensemble using base classifiers on random data subsets.

**Key Parameters:**

* **Base Estimator**: Base estimator type (DecisionTreeClassifier, SVC, etc.)
* **Number of Estimators**: Number of base estimators (default: 10)
* **Max Samples**: Samples per base estimator (default: 1.0)
* **Max Features**: Features per base estimator (default: 1.0)
* **Bootstrap**: Whether to sample with replacement (True/False)
* **Random State**: Seed for reproducibility

**7. Naive Bayes (GaussianNB)**

Applies Bayes' theorem with feature independence assumption.

Classification Workflow
^^^^^^^^^^^^^^^^^^^^^^^

1. Select and configure algorithms
2. Apply preprocessing steps
3. Train models
4. Evaluate using standard metrics
5. Compare algorithm performance

Classification Pipeline
^^^^^^^^^^^^^^^^^^^^^^^

The Classification module guides you through a complete machine learning workflow:

**1. Data Splitting**

* **Shuffle**: Enable shuffling to randomize the data before splitting
* **Split**: Choose between percentage split or K-fold cross-validation
* **Percentage**: Specify training data percentage (e.g., 80%)
* **K-fold**: Set the number of folds for cross-validation
* **Perform Final Test**: Option to reserve data for final testing

**2. Imputation**

* **Continuous Missing Value**: Strategy for handling missing numerical values
* **Categorical Missing Value**: Strategy for handling missing categorical values

**3. Scaling**

* **Standard Scaling**: Normalize data to mean of 0 and standard deviation of 1

**4. Feature Selection**

* **PCA**: Reduce features using Principal Component Analysis
* **K Best (ANOVA)**: Select top K features based on statistical tests

**5. Hyperparameter Tuning**

* **Grid Search**: Exhaustively search parameter combinations

Regression
---------

Overview
^^^^^^^^

The Regression module provides multiple algorithms for predicting continuous target variables.

Supported Algorithms
^^^^^^^^^^^^^^^^^^^^

**1. Linear Regression**

Standard approach estimating linear relationships between variables.

**Key Parameters:**

* **Fit Intercept**: Whether to calculate the intercept (default: True)
* **Positive**: Force coefficients to be positive (default: False)

**2. Ridge Regression**

Linear model with L2 regularization to reduce overfitting.

**Key Parameters:**

* **Alpha**: Regularization strength (default: 1.0)
* **Solver**: Method for computation (auto, svd, cholesky, lsqr, sparse_cg, etc.)
* **Fit Intercept**: Whether to calculate the intercept (default: True)
* **Max Iterations**: Maximum iterations for solver (default: 500)
* **Tolerance**: Precision of the solution (default: 0.0001)
* **Random State**: Seed for reproducibility (default: 43)

**3. Lasso Regression**

Linear model with L1 regularization promoting sparse coefficients.

**Key Parameters:**

* **Alpha**: Regularization strength (default: 1.0)
* **Fit Intercept**: Whether to calculate the intercept (default: True)
* **Max Iterations**: Maximum iterations for solver (default: 1000)
* **Tolerance**: Precision of the solution (default: 0.0001)
* **Selection**: Feature selection method (cyclic, random)
* **Random State**: Seed for reproducibility (default: 43)

**4. Logistic Regression for Regression**

Adapts logistic regression for regression tasks.

**Key Parameters:**

* **Penalty**: Regularization type (L1, L2, Elasticnet, None)
* **Regularization Strength (C)**: Inverse of regularization strength (default: 1.0)
* **Solver**: Algorithm for optimization (lbfgs, liblinear, newton-cg, sag, saga)
* **Max Iterations**: Maximum iterations for solver (default: 100)
* **L1 Ratio**: Mixing parameter for elasticnet penalty (default: 1.0)
* **Random State**: Seed for reproducibility (default: 43)

**5. AdaBoost Regression**

Ensemble method using weak regressors.

**Key Parameters:**

* **Base Estimator**: Type of weak regressor (DecisionTreeRegressor, etc.)
* **Number of Estimators**: Number of boosting stages (default: 50)
* **Learning Rate**: Weight applied to each regressor (default: 1.0)
* **Loss**: Loss function (linear, square, exponential)
* **Random State**: Seed for reproducibility (default: 43)

**6. Bagging Regression**

Ensemble method aggregating predictions from multiple models.

**Key Parameters:**

* **Base Estimator**: Base regressor type (DecisionTreeRegressor, SVR, etc.)
* **Number of Estimators**: Number of base estimators (default: 10)
* **Max Samples**: Samples per base estimator (default: 1.0)
* **Max Features**: Features per base estimator (default: 1.0)
* **Bootstrap**: Whether to sample with replacement (True/False)
* **Random State**: Seed for reproducibility (default: 43)

Evaluation Metrics
^^^^^^^^^^^^^^^^^^

* **Mean Absolute Error (MAE)**: Average of absolute differences between predictions and actual values
* **Root Mean Squared Error (RMSE)**: Square root of average squared differences
* **R-squared Score**: Proportion of variance explained by the model
* **Median Absolute Error**: Median of absolute differences between predictions and actual values

Regression Pipeline
^^^^^^^^^^^^^^^^^^^

The Regression module guides you through a complete workflow:

**1. Data Preprocessing**

* **Train/Test Split**: Divide data into training and testing sets
* **Feature Scaling**: Standardize or normalize feature ranges
* **Missing Value Handling**: Impute missing values with means, medians, or constants

**2. Model Selection**

* **Model Comparison**: Compare performance of different regression algorithms
* **Hyperparameter Tuning**: Find optimal parameter values
* **Cross-Validation**: Evaluate model performance on multiple data splits

**3. Model Evaluation**

* **Performance Metrics**: Calculate accuracy metrics on test data
* **Residual Analysis**: Analyze prediction errors and identify patterns
* **Feature Importance**: Evaluate contribution of each feature

Clustering
----------

Overview
^^^^^^^^

The Clustering module provides algorithms for grouping similar data points without labeled training data.

Supported Algorithms
^^^^^^^^^^^^^^^^^^^^

**1. K-Means Clustering**

Partitions observations into k clusters with nearest mean.

**Key Parameters:**

* **Number of Clusters**: Number of clusters to form (default: 8)
* **Initialization Method**: Method for initialization (k-means++, random)
* **Number of Initializations**: Number of times to run with different initializations (default: 10)
* **Max Iterations**: Maximum iterations for a single run (default: 300)
* **Random State**: Seed for reproducible results (default: 42)

**2. Agglomerative Clustering**

Hierarchical approach building nested clusters.

**Key Parameters:**

* **Number of Clusters**: Number of clusters to find (default: 2)
* **Linkage**: Method for calculating distances between clusters (ward, complete, average, single)
* **Distance Metric**: Metric for calculating distances (euclidean, manhattan, etc.)
* **Compute Distances**: Whether to compute distances for visualization (default: False)

**3. K-Mode Clustering**

Specialized for categorical data.

**Key Parameters:**

* **Number of Clusters**: Number of clusters to form (default: 8)
* **Initialization Method**: Method for initial centroids (cao, random, Huang)
* **Number of Initializations**: Number of times to run with different initializations (default: 10)
* **Max Iterations**: Maximum iterations for a single run (default: 100)
* **Random State**: Seed for reproducible results (default: 42)

**4. Gaussian Mixture Model**

Probabilistic model assuming data from Gaussian distributions mixture.

**Key Parameters:**

* **Number of Components**: Number of mixture components (default: 1)
* **Covariance Type**: Type of covariance parameters (full, tied, diag, spherical)
* **Number of Initializations**: Number of times to run with different initializations (default: 1)
* **Max Iterations**: Maximum number of EM iterations (default: 100)
* **Initialization Parameters**: Method for initialization (kmeans, random)
* **Tolerance**: Convergence threshold (default: 0.01)
* **Random State**: Seed for reproducible results (default: 42)

**5. Spectral Clustering**

Uses eigenvalues of similarity matrix to reduce dimensions before clustering.

**Key Parameters:**

* **Number of Clusters**: Number of clusters to form (default: 8)
* **Eigen Solver**: Method for computing eigenvectors (arpack, lobpcg, amg)
* **Number of Components**: Number of eigenvectors to use
* **Number of Initializations**: Number of times k-means will be run (default: 10)
* **Gamma**: Kernel coefficient for rbf kernel
* **Number of Neighbors**: Number of neighbors for nearest neighbors graph
* **Assign Labels**: Method for assigning labels (kmeans, discretize)

**6. Mean Shift**

Non-parametric technique that finds dense areas of data points.

**Key Parameters:**

* **Max Iterations**: Maximum number of iterations (default: 300)

**7. Affinity Propagation**

Finds clusters by passing messages between data points.

**Key Parameters:**

* **Damping**: Damping factor to avoid numerical oscillations (default: 0.5)
* **Convergence Iterations**: Number of iterations with no change before convergence (default: 15)
* **Max Iterations**: Maximum number of iterations (default: 200)
* **Affinity**: Metric used to compute affinity between points (euclidean, precomputed)

Clustering Evaluation Metrics
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* **Silhouette Score**: Measure of how similar objects are to their own cluster compared to other clusters
* **Davies-Bouldin Index**: Average similarity of each cluster with its most similar cluster
* **Calinski-Harabasz Index**: Ratio of between-cluster dispersion to within-cluster dispersion
* **Inertia**: Sum of squared distances of samples to their closest cluster center

Clustering Pipeline
^^^^^^^^^^^^^^^^^^^

The Clustering module guides you through a complete workflow:

**1. Data Preprocessing**

* **Feature Scaling**: Standardize features to equal scale
* **Dimensionality Reduction**: Apply PCA or t-SNE before clustering
* **Categorical Encoding**: Convert categorical variables for distance-based algorithms

**2. Model Selection**

* **Algorithm Selection**: Choose appropriate clustering method based on data type
* **Parameter Tuning**: Optimize key parameters like number of clusters
* **Initialization Method**: Choose how to initialize cluster centers

**3. Cluster Evaluation**

* **Visualization**: Plot clusters in 2D/3D space
* **Validation**: Assess cluster quality using internal and stability metrics
* **Interpretation**: Analyze cluster characteristics and distributions 