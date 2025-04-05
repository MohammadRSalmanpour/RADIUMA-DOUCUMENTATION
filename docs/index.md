# ViSERA - Visualized & Standardized Environment for Radiomics Analysis

ViSERA is a powerful workflow generator for standardized radiomics analysis and medical image visualization. It provides a free, open-source platform specialized for visualization, processing, segmentation, registration, fusion, and analysis of medical/biomedical images, including radiomics and machine learning capabilities.

## Table of Contents
- [Overview](#overview)
- [Key Features](#key-features)
- [Visual Node-Based Workflow System](#visual-node-based-workflow-system)
- [Workflow Modules](#workflow-modules)
  - [Image Viewer](#image-viewer)
  - [Image Reader](#image-reader)
  - [RT Struct Reader](#rt-struct-reader)
  - [Table Reader/Writer](#table-readerwriter)
  - [Image Registration](#image-registration)
  - [Image Filter](#image-filter)
  - [Image Fusion](#image-fusion)
  - [Radiomic Feature Generator](#radiomic-feature-generator)
- [Installation](#installation)
  - [Prerequisites](#prerequisites)
  - [Download](#download)
  - [Setup](#setup)
  - [Running ViSERA](#running-visera)
- [Module Documentation](#module-documentation)
  - [Preprocessing](#preprocessing)
  - [Classification](#classification)
  - [Regression](#regression)
  - [Clustering](#clustering)

## Overview

ViSERA is a Python-based desktop software designed to improve usability, reusability, and reproducibility in medical imaging and healthcare research. As a major, entirely-revamped upgrade to the original SERA (MATLAB-based), ViSERA enables standardized and reproducible radiomic feature extraction in compliance with the Image Biomarker Standardization Initiative (IBSI 1.0).

The platform employs numerous popular image processing algorithms to create end-to-end standardized workflows, making it an ideal development platform for reproducible research by connecting different tools.

## Key Features

- **Standardized Radiomics Analysis**: Compliant with IBSI 1.0 standards
- **Advanced Image Filtering**: Standardized against IBSI 2.0 with multiple filter options
- **End-to-End Workflows**: Connect various imaging and analysis tools
- **Collaborative Research Support**: Ensures consistency across different studies
- **User-Friendly Interface**: Designed for various expertise levels including:
  - Radiation oncologists
  - Radiologists
  - Medical physicists
  - Data scientists
- **Comprehensive Machine Learning Tools**: Built-in classification, regression, and clustering modules

## Visual Node-Based Workflow System

ViSERA uses a visual programming approach where modules are represented as nodes that can be connected to create complete data processing pipelines. This intuitive interface allows users with minimal programming experience to build sophisticated workflows.

### Creating Workflows

1. **Adding Modules**: Double-click on a module from the module palette to add it to the workspace
2. **Configuring Modules**: Double-click on a module node to open its configuration dialog
3. **Connecting Modules**: Click and drag from an output port to an input port to create connections
4. **Running Workflows**: Click the "Run" button on a node to execute it and all its prerequisite nodes
5. **Stopping Execution**: Click the "Stop" button to halt execution of a running workflow

### Module Compatibility

Each module explicitly defines which other modules can connect to its inputs and outputs, ensuring that only valid connections can be made:

- **Image Reader**: Outputs to Image Convertor, Filter, Fusion, and Registration modules
- **RT Struct Reader**: Outputs to Radiomic Feature Generator and Image Writer modules
- **Image Filter**: Takes image input, outputs to multiple imaging modules
- **Radiomic Feature Generator**: Takes image and mask inputs, outputs to data analysis modules
- **Preprocessing**: Takes feature data, connects to machine learning modules
- **Classification/Regression/Clustering**: Take preprocessed data as input, connect to visualization

### Example Workflows

**Basic Radiomics Analysis Pipeline:**
1. Image Reader → Load medical images
2. RT Struct Reader → Load region of interest segmentations
3. Radiomic Feature Generator → Extract quantitative features
4. Preprocessing → Prepare features for analysis
5. Classification → Analyze features for diagnostic/prognostic models

**Image Processing Pipeline:**
1. Image Reader → Load reference image
2. Image Reader → Load secondary image
3. Image Registration → Align images spatially
4. Image Fusion → Combine aligned images
5. Image Filter → Enhance features of interest
6. Image Writer → Save processed results

### Workflow Controls

- **Layout Management**: Automatically arrange nodes with the "Align Modules" function
- **Module Search**: Quickly find modules using the search function (Tab key)
- **Copy/Paste**: Duplicate node configurations to create similar processing steps
- **Save/Load**: Save entire workflows and reload them for future use

### Keyboard Shortcuts

- **Tab**: Open module search
- **Ctrl+C / Cmd+C**: Copy selected nodes
- **Ctrl+V / Cmd+V**: Paste nodes
- **Delete**: Remove selected nodes
- **D**: Lock/Unlock nodes

## Workflow Modules

ViSERA offers a comprehensive set of modules that can be connected to create end-to-end research workflows. These modules cover the entire radiomics pipeline from image input to statistical analysis.

### Image Viewer

The Medical Image Viewer is a comprehensive module designed for advanced medical image visualization and analysis, providing tools for detailed examination, segmentation, and analysis of medical imaging data.

#### View Types
- **Axial View**: Horizontal cross-sections (top-down view)
- **Sagittal View**: Vertical cross-sections from side to side
- **Coronal View**: Vertical cross-sections from front to back
- **3D View**: Complete three-dimensional rendering with:
  - Volume View: Full 3D visualization of image data
  - Mask View: Visualization of segmentation results

#### File Support
- NIFTI Files: Support for Neuroimaging Informatics Technology Initiative format
- DICOM Files: Individual DICOM image support
- DICOM Directories: Support for complete DICOM studies/series
- Segmentation Files: Import/export of segmentation data

#### Toolbar Functions

**Image Navigation & Information**
- **Hand Tool**: Real-time coordinate display, intensity values, metadata access
- **Image List**: Layer navigation with options for information, removal, and colormap customization

**Image Manipulation Tools**
- **Segmentation**: Threshold-based and manual drawing tools
- **Crop Tool**: Define regions of interest
- **Ruler**: Precise distance measurements
- **Rotation**: Rotate images along any axis with animation capabilities
- **Contrast**: Window/level adjustment and brightness controls
- **Filter**: Apply threshold-based filters

**Visualization Controls**
- **Crosshairs**: Toggle visibility, synchronized across all views
- **Overlay**: Add image layers with transparency control
- **Screenshot**: Capture and save current view
- **Layout Control**: Reset to standard four-panel layout

### Image Reader

A flexible module for importing various medical image formats into the ViSERA workflow.

#### Key Parameters
- **Source Type**: Choose between folder or single file import
- **Path**: Location of the medical image file(s) to import

#### Supported Input Formats
- DICOM Files and Directories
- NIFTI Files (.nii, .nii.gz)
- Various other medical image formats

#### Workflow Integration
- Outputs to Image Convertor
- Outputs to Image Filter
- Outputs to Image Fusion
- Outputs to Image Registration

### RT Struct Reader

Specialized module for importing radiotherapy structure sets, supporting the standardized DICOM-RT format used in radiation oncology.

#### Key Parameters
- **RT Label Directory**: Path to the RT structure set file
- **RT Main Image Directory**: Path to the corresponding image data

#### Functionality
- Imports DICOM-RT structure sets along with their associated images
- Extracts contours and segmentation information
- Provides labeled structures for further analysis

#### Workflow Integration
- Outputs to Radiomic Feature Generator
- Outputs to Image Writer
- Outputs to Image Viewer

### Table Reader/Writer

Modules for importing and exporting tabular data in various formats.

#### Reader Parameters
- **File Path**: Location of the input data file
- **Format Detection**: Automatic detection of file format

#### Writer Parameters
- **Path**: Destination for saving the output data
- **File Format**: Choice of output format (.xlsx, .csv, .dcm, .nii.gz, .nrrd)
- **Single/Multi File**: Option to save as single file or multiple files

#### Supported Formats
- CSV files
- Excel spreadsheets
- Structured data exports from analysis modules

### Image Registration

Tools for spatial alignment of images from different modalities or time points.

#### Registration Types
- **Rigid Registration**: Maintains shape and size, only allows rotation and translation
- **Non-Rigid Registration**: Allows local deformations for better alignment
- **Simple Non-Rigid**: Simplified version of non-rigid registration for faster processing

#### Key Parameters

**Rigid Registration**
- **Number of Histogram Bins**: Value for intensity histograms (default: 10)
- **Sampling Method**: Method for sampling points during registration
- **Sampling Percentage**: Percentage of voxels to sample (default: 0.01)
- **Learning Rate**: Step size for optimization (default: 0.01)
- **Number of Iterations**: Maximum iterations for optimization (default: 5)
- **Interpolation**: Method for interpolation (Linear, Nearest, etc.)

**Non-Rigid Registration**
- **Number of Iterations**: Iterations for deformable registration
- **Number of Resolutions**: Multi-resolution levels for optimization
- **Final Grid Spacing**: Density of deformation field
- **Transform Type**: B-Spline or other transformation types
- **Auto-Transform**: Automatic adjustment of transform parameters
- **Auto-Scale**: Automatic scaling during registration

#### Workflow Integration
- Takes fixed and moving images as inputs
- Outputs transformed image aligned to reference

### Image Filter

Comprehensive set of image filtering options for enhancing features, reducing noise, and preparing images for feature extraction.

#### Filter Types
- **Gabor Filter**: Texture and edge detection
- **Wavelet Filter**: Multi-scale analysis
- **Threshold Filter**: Simple intensity-based filtering
- **Gradient Filter**: Edge enhancement
- **Smoothing Filter**: Noise reduction

#### Key Parameters

**Gabor Filter**
- **Gamma**: Controls filter shape
- **Lambda**: Wavelength of sinusoidal factor
- **Theta**: Orientation of filter
- **Step**: Increment value for filter application
- **Response**: Type of filter response
- **Rotation**: Enable/disable rotation invariance
- **Pooling Method**: Method for combining filter responses

**Wavelet Filter**
- **Dimension**: 2D or 3D processing
- **Boundary Condition**: Handling of image boundaries
- **Filter Configuration**: Specific filter settings
- **Filter Size**: Size of the wavelet kernel
- **Decomposition Level**: Number of wavelet transform levels
- **Wavelet Family**: Type of wavelet (Haar, Daubechies, etc.)
- **Wavelet Type**: Specific wavelet implementation

#### Workflow Integration
- Takes image input
- Applies selected filtering techniques
- Outputs filtered image for further processing

### Image Fusion

Advanced capabilities for combining information from multiple imaging modalities.

#### Fusion Methods
- **Weighted Fusion**: Linear combination of input images
- **Wavelet Fusion**: Multi-resolution decomposition and fusion
- **PCA Fusion**: Principal Component Analysis based fusion

#### Key Parameters

**Weighted Fusion**
- **Weight 1**: Weight for first input image (0-1)
- **Weight 2**: Weight for second input image (0-1)
- **Interpolation**: Method for interpolating between images (Linear, Cubic, etc.)

**Wavelet Fusion**
- **Fusion Method**: Algorithm for combining wavelet coefficients (Max, Min, Mean)
- **Level**: Decomposition level for wavelet transform
- **Mode**: Signal extrapolation mode
- **Wavelet**: Wavelet family to use (Haar, etc.)

**PCA Fusion**
- **Number of Components**: Components to use in reconstruction
- **SVD Solver**: Algorithm for Singular Value Decomposition
- **Components**: Number of principal components

#### Workflow Integration
- Takes two input images
- Combines information according to selected method
- Outputs a single fused image

### Radiomic Feature Generator

Core module for extracting standardized quantitative features from medical images following IBSI guidelines.

#### Feature Types
- **First-order Statistics**: Intensity-based features
- **Shape-based Features**: Morphological characteristics
- **Texture Features**: Spatial patterns (GLCM, GLRLM, etc.)
- **Wavelet Features**: Multi-resolution analysis

#### Key Parameters
- **Data Type**: Modality type (MR, CT, PET, etc.)
- **Discretization Type**: Method for binning intensity values
- **Bin Size**: Size of intensity bins for feature calculation
- **Image Interpolation**: Method for resampling images
- **ROI Interpolation**: Method for resampling masks
- **Isotropic Voxel Size**: Size for resampling to isotropic voxels
- **Intensity Rounding**: Option to round intensity values
- **Segmentation Range**: Option to limit intensity range
- **Outlier Filtering**: Methods for handling outliers
- **Quantization Method**: Approach for discretizing intensities
- **Maximum ROIs**: Number of regions to analyze per image

#### Workflow Integration
- Takes both image and mask inputs
- Extracts features according to standardized definitions
- Outputs tabular data with all calculated features

## Installation

### Prerequisites
- Python 3.11 or below

### Download
```shell
git clone -b new-year-visera --recurse-submodules git@github.com:MohammadRSalmanpour/ViSERA.git 
```

Download NodeGraphPySide6 from [this repository](https://github.com/somso2e/NodeGraphPySide6/tree/70043c151c67e74dde7b34c2969b19b02782940a) and replace it with dependencies/NodeGraphPySide6.

### Setup
```shell
pip install -r requirements.txt 
pip install ./dependencies/NodeGraphPySide6/
```

### Running ViSERA
```shell
python ./ViSERA
```

## Module Documentation

### Preprocessing

#### Overview
The preprocessing module provides essential data preparation capabilities before applying machine learning algorithms. Proper preprocessing is crucial for achieving optimal model performance.

#### Available Methods

##### 1. Data Encoding
Converts categorical data into numerical format for machine learning algorithms.

| Method | Description | Use Case | Implementation |
|--------|-------------|----------|----------------|
| **Label Encoding** | Converts each categorical value to a unique integer | Ordinal data where order matters | `sklearn.preprocessing.LabelEncoder` |
| **One-Hot Encoding** | Creates binary columns for each category | Nominal data with no inherent order | `sklearn.preprocessing.OneHotEncoder` |
| **Ordinal Encoding** | Converts values to ordinal integers based on specified ordering | Data with known category ordering | `sklearn.preprocessing.OrdinalEncoder` |

##### 2. Data Splitting
Divides the dataset into training, validation, and test sets.

| Method | Description | Key Parameters |
|--------|-------------|----------------|
| **Percentage Split** | Splits data by percentage | Train Split (50-95%), Shuffle, Random Seed |
| **K-fold Cross-Validation** | Splits data into K folds | K (2-10), Random Seed |

##### 3. Data Imputation
Handles missing values in the dataset.

| Method | Description | Key Parameters |
|--------|-------------|----------------|
| **Simple Imputer** | Basic strategy for imputing missing values | Strategy (mean, median, mode, constant) |
| **KNN Imputer** | Uses K-Nearest Neighbors | N Neighbors, Weights, Distance Metric |
| **Iterative Imputer** | Models each feature as a function of other features | Initial Strategy, Estimator, Max Iterations |

##### 4. Data Scaling
Standardizes feature ranges to improve model performance.

| Method | Description | Key Parameters |
|--------|-------------|----------------|
| **Robust Scaler** | Scales features using statistics robust to outliers | Quantile Range |
| **Min-Max Scaler** | Scales features to a specified range | Min, Max values |
| **Standard Scaler** | Standardizes by removing mean and scaling to unit variance | None |
| **Normalizer** | Scales samples to unit norm | Norm type (l1, l2, max) |
| **MaxAbs Scaler** | Scales to range [-1, 1] by max absolute value | None |

##### 5. Feature Selection/Extraction
Reduces dimensionality by selecting important features or creating composite features.

| Method | Description | Key Parameters |
|--------|-------------|----------------|
| **SelectKBest** | Selects top k features based on scoring function | Score Function, Number of Features |
| **SelectPercentile** | Selects features by percentile of scores | Score Function, Percentile |
| **Variance Threshold** | Removes low-variance features | Threshold |
| **PCA** | Linear dimensionality reduction using SVD | Components, SVD Solver, Whiten |
| **Kernel PCA** | Non-linear dimensionality reduction | Components, Kernel type, Parameters |
| **Factor Analysis** | Linear dimensionality reduction using factor analysis | Components, Rotation |
| **Fast ICA** | Independent Component Analysis | Components, Algorithm, Fun |

#### Workflow Integration
1. Data Loading
2. Encoding
3. Data Splitting
4. Imputation
5. Scaling
6. Feature Selection
7. Model Training

#### Best Practices
1. Always encode categorical variables
2. Handle missing values appropriately
3. Scale features for better performance
4. Select relevant features to reduce dimensionality
5. Keep random states consistent for reproducibility
6. Use cross-validation for reliable evaluation
7. Reserve test data until final evaluation

### Classification

#### Overview
The Classification module provides multiple algorithms for data analysis with customizable parameters through an intuitive user interface.

#### Supported Algorithms

##### 1. Logistic Regression Classifier
A linear model for classification that predicts class probabilities.

**Key Parameters:**
- Penalty (L1, L2, Elasticnet, None)
- Regularization Strength (C)
- Solver (Lbfgs, Liblinear, etc.)
- Multi-class Option

##### 2. K-Nearest Neighbors Classifier
Non-parametric method using closest training examples.

**Key Parameters:**
- Number of Neighbors
- Weights (Uniform, Distance)
- Distance Metric
- Algorithm (Auto, Ball_tree, Kd_tree, Brute)

##### 3. Decision Tree Classifier
Creates a model predicting targets by learning decision rules.

**Key Parameters:**
- Criterion (gini, entropy, log_loss)
- Max Depth
- Min Samples Split/Leaf
- Class Weight

##### 4. Support Vector Machines (SVM)
Finds optimal hyperplane to separate classes.

**Key Parameters:**
- Kernel (linear, poly, rbf, sigmoid)
- Regularization Parameter (C)
- Gamma
- Degree (for poly kernel)

##### 5. AdaBoost Classifier
Ensemble method using weak classifiers on modified data versions.

**Key Parameters:**
- Base Estimator
- Number of Estimators
- Learning Rate
- Algorithm (SAMME, SAMME.R)

##### 6. Bagging Classifier
Ensemble using base classifiers on random data subsets.

**Key Parameters:**
- Base Estimator
- Number of Estimators
- Bootstrap option
- Sample and Feature ratios

##### 7. Naive Bayes (GaussianNB)
Applies Bayes' theorem with feature independence assumption.

#### Classification Workflow
1. Select and configure algorithms
2. Apply preprocessing steps
3. Train models
4. Evaluate using standard metrics
5. Compare algorithm performance

### Regression

#### Overview
The Regression module provides multiple algorithms for predicting continuous target variables.

#### Supported Algorithms

##### 1. Linear Regression
Standard approach estimating linear relationships between variables.

**Key Parameters:**
- Fit Intercept
- Positive Constraints

##### 2. Ridge Regression
Linear model with L2 regularization to reduce overfitting.

**Key Parameters:**
- Alpha (regularization strength)
- Solver
- Fit Intercept
- Max Iterations

##### 3. Lasso Regression
Linear model with L1 regularization promoting sparse coefficients.

**Key Parameters:**
- Alpha
- Selection method (cyclic, random)
- Max Iterations
- Tolerance

##### 4. Logistic Regression for Regression
Adapts logistic regression for regression tasks.

**Key Parameters:**
- Penalty
- Regularization Strength
- Solver
- L1 Ratio (for elasticnet)

##### 5. AdaBoost Regression
Ensemble method using weak regressors.

**Key Parameters:**
- Base Estimator
- Loss function
- Learning Rate
- Number of Estimators

##### 6. Bagging Regression
Ensemble method aggregating predictions from multiple models.

**Key Parameters:**
- Base Estimator
- Number of Estimators
- Bootstrap option
- Sample and Feature ratios

#### Evaluation Metrics
- Mean Absolute Error (MAE)
- Root Mean Squared Error (RMSE)
- R-squared Score
- Median Absolute Error

### Clustering

#### Overview
The Clustering module provides algorithms for grouping similar data points without labeled training data.

#### Supported Algorithms

##### 1. K-Means Clustering
Partitions observations into k clusters with nearest mean.

**Key Parameters:**
- Number of Clusters
- Initialization Method
- Number of Initializations
- Max Iterations

##### 2. Agglomerative Clustering
Hierarchical approach building nested clusters.

**Key Parameters:**
- Number of Clusters
- Linkage criterion
- Distance Metric
- Compute Distances option

##### 3. K-Mode Clustering
Specialized for categorical data.

**Key Parameters:**
- Number of Clusters
- Initialization Method
- Number of Initializations
- Max Iterations

##### 4. Gaussian Mixture Model
Probabilistic model assuming data from Gaussian distributions mixture.

**Key Parameters:**
- Number of Components
- Covariance Type
- Initialization Parameters
- Tolerance

##### 5. K-Medoids Clustering
More robust to noise and outliers than K-Means.

**Key Parameters:**
- Number of Clusters
- Distance Metric
- Method (alternate, pam)
- Initialization Method

#### Evaluation Metrics
- Completeness Score
- Homogeneity Score
- V-measure Score
- Adjusted Rand Index
- Silhouette analysis

#### Optimization Techniques
- Elbow method for optimal cluster number
- Silhouette analysis for cluster validation



