Welcome to ViSERA
===========================

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   index.md

ViSERA - Visualized & Standardized Environment for Radiomics Analysis
=======================================================================

ViSERA is a powerful workflow generator for standardized radiomics analysis and medical image visualization. It provides a free, open-source platform specialized for visualization, processing, segmentation, registration, fusion, and analysis of medical/biomedical images, including radiomics and machine learning capabilities.

Table of Contents
---------------

.. contents:: :local:

Overview
--------

ViSERA is a Python-based desktop software designed to improve usability, reusability, and reproducibility in medical imaging and healthcare research. As a major, entirely-revamped upgrade to the original SERA (MATLAB-based), ViSERA enables standardized and reproducible radiomic feature extraction in compliance with the Image Biomarker Standardization Initiative (IBSI 1.0).

The platform employs numerous popular image processing algorithms to create end-to-end standardized workflows, making it an ideal development platform for reproducible research by connecting different tools.

Key Features
-----------

* **Standardized Radiomics Analysis**: Compliant with IBSI 1.0 standards
* **Advanced Image Filtering**: Standardized against IBSI 2.0 with multiple filter options
* **End-to-End Workflows**: Connect various imaging and analysis tools
* **Collaborative Research Support**: Ensures consistency across different studies
* **User-Friendly Interface**: Designed for various expertise levels including:

  * Radiation oncologists
  * Radiologists
  * Medical physicists
  * Data scientists

* **Comprehensive Machine Learning Tools**: Built-in classification, regression, and clustering modules

Visual Node-Based Workflow System
-------------------------------

ViSERA uses a visual programming approach where modules are represented as nodes that can be connected to create complete data processing pipelines. This intuitive interface allows users with minimal programming experience to build sophisticated workflows.

Creating Workflows
~~~~~~~~~~~~~~~~

1. **Adding Modules**: Double-click on a module from the module palette to add it to the workspace
2. **Configuring Modules**: Double-click on a module node to open its configuration dialog
3. **Connecting Modules**: Click and drag from an output port to an input port to create connections
4. **Running Workflows**: Click the "Run" button on a node to execute it and all its prerequisite nodes
5. **Stopping Execution**: Click the "Stop" button to halt execution of a running workflow

Module Compatibility
~~~~~~~~~~~~~~~~~~

Each module explicitly defines which other modules can connect to its inputs and outputs, ensuring that only valid connections can be made:

* **Image Reader**: Outputs to Image Convertor, Filter, Fusion, and Registration modules
* **RT Struct Reader**: Outputs to Radiomic Feature Generator and Image Writer modules
* **Image Filter**: Takes image input, outputs to multiple imaging modules
* **Radiomic Feature Generator**: Takes image and mask inputs, outputs to data analysis modules
* **Preprocessing**: Takes feature data, connects to machine learning modules
* **Classification/Regression/Clustering**: Take preprocessed data as input, connect to visualization

Example Workflows
~~~~~~~~~~~~~~~

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

Workflow Controls
~~~~~~~~~~~~~~~

* **Layout Management**: Automatically arrange nodes with the "Align Modules" function
* **Module Search**: Quickly find modules using the search function (Tab key)
* **Copy/Paste**: Duplicate node configurations to create similar processing steps
* **Save/Load**: Save entire workflows and reload them for future use

Keyboard Shortcuts
~~~~~~~~~~~~~~~~

* **Tab**: Open module search
* **Ctrl+C / Cmd+C**: Copy selected nodes
* **Ctrl+V / Cmd+V**: Paste nodes
* **Delete**: Remove selected nodes
* **D**: Lock/Unlock nodes

Workflow Modules
--------------

ViSERA offers a comprehensive set of modules that can be connected to create end-to-end research workflows. These modules cover the entire radiomics pipeline from image input to statistical analysis.

Image Viewer
~~~~~~~~~~~

The Medical Image Viewer is a comprehensive module designed for advanced medical image visualization and analysis, providing tools for detailed examination, segmentation, and analysis of medical imaging data.

View Types
^^^^^^^^^

* **Axial View**: Horizontal cross-sections (top-down view)
* **Sagittal View**: Vertical cross-sections from side to side
* **Coronal View**: Vertical cross-sections from front to back
* **3D View**: Complete three-dimensional rendering with:

  * Volume View: Full 3D visualization of image data
  * Mask View: Visualization of segmentation results

File Support
^^^^^^^^^^^

* NIFTI Files: Support for Neuroimaging Informatics Technology Initiative format
* DICOM Files: Individual DICOM image support
* DICOM Directories: Support for complete DICOM studies/series
* Segmentation Files: Import/export of segmentation data

Toolbar Functions
^^^^^^^^^^^^^^^

**Image Navigation & Information**

* **Hand Tool**: Real-time coordinate display, intensity values, metadata access
* **Image List**: Layer navigation with options for information, removal, and colormap customization

**Image Manipulation Tools**

* **Segmentation**: Threshold-based and manual drawing tools
* **Crop Tool**: Define regions of interest
* **Ruler**: Precise distance measurements
* **Rotation**: Rotate images along any axis with animation capabilities
* **Contrast**: Window/level adjustment and brightness controls
* **Filter**: Apply threshold-based filters

**Visualization Controls**

* **Crosshairs**: Toggle visibility, synchronized across all views
* **Overlay**: Add image layers with transparency control
* **Screenshot**: Capture and save current view
* **Layout Control**: Reset to standard four-panel layout

Image Reader
~~~~~~~~~~~

A flexible module for importing various medical image formats into the ViSERA workflow.

Key Parameters
^^^^^^^^^^^^

* **Source Type**: Choose between folder or single file import
* **Path**: Location of the medical image file(s) to import

Supported Input Formats
^^^^^^^^^^^^^^^^^^^^^

* DICOM Files and Directories
* NIFTI Files (.nii, .nii.gz)
* Various other medical image formats

Workflow Integration
^^^^^^^^^^^^^^^^^^

* Outputs to Image Convertor
* Outputs to Image Filter
* Outputs to Image Fusion
* Outputs to Image Registration

RT Struct Reader
~~~~~~~~~~~~~~

Specialized module for importing radiotherapy structure sets, supporting the standardized DICOM-RT format used in radiation oncology.

Key Parameters
^^^^^^^^^^^^

* **RT Label Directory**: Path to the RT structure set file
* **RT Main Image Directory**: Path to the corresponding image data

Functionality
^^^^^^^^^^^

* Imports DICOM-RT structure sets along with their associated images
* Extracts contours and segmentation information
* Provides labeled structures for further analysis

Workflow Integration
^^^^^^^^^^^^^^^^^^

* Outputs to Radiomic Feature Generator
* Outputs to Image Writer
* Outputs to Image Viewer

Table Reader/Writer
~~~~~~~~~~~~~~~~~

Modules for importing and exporting tabular data in various formats.

Reader Parameters
^^^^^^^^^^^^^^^

* **File Path**: Location of the input data file
* **Format Detection**: Automatic detection of file format

Writer Parameters
^^^^^^^^^^^^^^^

* **Path**: Destination for saving the output data
* **File Format**: Choice of output format (.xlsx, .csv, .dcm, .nii.gz, .nrrd)
* **Single/Multi File**: Option to save as single file or multiple files

Supported Formats
^^^^^^^^^^^^^^^

* CSV files
* Excel spreadsheets
* Structured data exports from analysis modules

Image Registration
~~~~~~~~~~~~~~~~

Tools for spatial alignment of images from different modalities or time points.

Registration Types
^^^^^^^^^^^^^^^

* **Rigid Registration**: Maintains shape and size, only allows rotation and translation
* **Non-Rigid Registration**: Allows local deformations for better alignment
* **Simple Non-Rigid**: Simplified version of non-rigid registration for faster processing

Key Parameters
^^^^^^^^^^^^

**Rigid Registration**

* **Number of Histogram Bins**: Value for intensity histograms (default: 10)
* **Sampling Method**: Method for sampling points during registration
* **Sampling Percentage**: Percentage of voxels to sample (default: 0.01)
* **Learning Rate**: Step size for optimization (default: 0.01)
* **Number of Iterations**: Maximum iterations for optimization (default: 5)
* **Interpolation**: Method for interpolation (Linear, Nearest, etc.)

**Non-Rigid Registration**

* **Number of Iterations**: Iterations for deformable registration
* **Number of Resolutions**: Multi-resolution levels for optimization
* **Final Grid Spacing**: Density of deformation field
* **Transform Type**: B-Spline or other transformation types
* **Auto-Transform**: Automatic adjustment of transform parameters
* **Auto-Scale**: Automatic scaling during registration

Workflow Integration
^^^^^^^^^^^^^^^^^

* Takes fixed and moving images as inputs
* Outputs transformed image aligned to reference

Image Filter
~~~~~~~~~~~

Comprehensive set of image filtering options for enhancing features, reducing noise, and preparing images for feature extraction.

Filter Types
^^^^^^^^^^

* **Gabor Filter**: Texture and edge detection
* **Wavelet Filter**: Multi-scale analysis
* **Threshold Filter**: Simple intensity-based filtering
* **Gradient Filter**: Edge enhancement
* **Smoothing Filter**: Noise reduction

Key Parameters
^^^^^^^^^^^^

**Gabor Filter**

* **Gamma**: Controls filter shape
* **Lambda**: Wavelength of sinusoidal factor
* **Theta**: Orientation of filter
* **Step**: Increment value for filter application
* **Response**: Type of filter response
* **Rotation**: Enable/disable rotation invariance
* **Pooling Method**: Method for combining filter responses

**Wavelet Filter**

* **Dimension**: 2D or 3D processing
* **Boundary Condition**: Handling of image boundaries
* **Filter Configuration**: Specific filter settings
* **Filter Size**: Size of the wavelet kernel
* **Decomposition Level**: Number of wavelet transform levels
* **Wavelet Family**: Type of wavelet (Haar, Daubechies, etc.)
* **Wavelet Type**: Specific wavelet implementation

Workflow Integration
^^^^^^^^^^^^^^^^^

* Takes image input
* Applies selected filtering techniques
* Outputs filtered image for further processing

Image Fusion
~~~~~~~~~~~

Advanced capabilities for combining information from multiple imaging modalities.

Fusion Methods
^^^^^^^^^^^^

* **Weighted Fusion**: Linear combination of input images
* **Wavelet Fusion**: Multi-resolution decomposition and fusion
* **PCA Fusion**: Principal Component Analysis based fusion

Key Parameters
^^^^^^^^^^^^

**Weighted Fusion**

* **Weight 1**: Weight for first input image (0-1)
* **Weight 2**: Weight for second input image (0-1)
* **Interpolation**: Method for interpolating between images (Linear, Cubic, etc.)

**Wavelet Fusion**

* **Fusion Method**: Algorithm for combining wavelet coefficients (Max, Min, Mean)
* **Level**: Decomposition level for wavelet transform
* **Mode**: Signal extrapolation mode
* **Wavelet**: Wavelet family to use (Haar, etc.)

**PCA Fusion**

* **Number of Components**: Components to use in reconstruction
* **SVD Solver**: Algorithm for Singular Value Decomposition
* **Components**: Number of principal components

Workflow Integration
^^^^^^^^^^^^^^^^^

* Takes two input images
* Combines information according to selected method
* Outputs a single fused image

Radiomic Feature Generator
~~~~~~~~~~~~~~~~~~~~~~~~

Core module for extracting standardized quantitative features from medical images following IBSI guidelines.

Feature Types
^^^^^^^^^^^

* **First-order Statistics**: Intensity-based features
* **Shape-based Features**: Morphological characteristics
* **Texture Features**: Spatial patterns (GLCM, GLRLM, etc.)
* **Wavelet Features**: Multi-resolution analysis

Key Parameters
^^^^^^^^^^^^

* **Data Type**: Modality type (MR, CT, PET, etc.)
* **Discretization Type**: Method for binning intensity values
* **Bin Size**: Size of intensity bins for feature calculation
* **Image Interpolation**: Method for resampling images
* **ROI Interpolation**: Method for resampling masks
* **Isotropic Voxel Size**: Size for resampling to isotropic voxels
* **Intensity Rounding**: Option to round intensity values
* **Segmentation Range**: Option to limit intensity range
* **Outlier Filtering**: Methods for handling outliers
* **Quantization Method**: Approach for discretizing intensities
* **Maximum ROIs**: Number of regions to analyze per image

Workflow Integration
^^^^^^^^^^^^^^^^^

* Takes both image and mask inputs
* Extracts features according to standardized definitions
* Outputs tabular data with all calculated features

Examples
-------

This section provides step-by-step guides for common tasks in ViSERA to help users get started quickly.

Image Conversion
~~~~~~~~~~~~~

The Image Conversion functionality allows users to easily convert medical images between different file formats, making it simple to work with various imaging systems and software.

How It Works
^^^^^^^^^^

1. **Image Reader Module**: First, use the Image Reader to load your source images

   * Supports reading from individual files or entire folders
   * Compatible with NIFTI (.nii, .nii.gz), NRRD, and DICOM formats
   * Handles both single images and multi-file image series

2. **Writer Module**: Then, connect the Writer module to convert and save the images

   * Specify your desired output location
   * Choose the target format for conversion
   * Process individual files or batch convert entire directories

Workflow Integration
^^^^^^^^^^^^^^^^^

To convert images:

1. Add an Image Reader module to your workflow
2. Configure the Image Reader to load your source image(s)
3. Add a Writer module to your workflow 
4. Connect the output port of the Image Reader to the input port of the Writer
5. Configure the Writer with your desired output format and location
6. Run the workflow to perform the conversion

This simple two-step process allows for easy conversion of medical images between supported formats without specialized knowledge of file formats or conversion tools.

RT Struct Processing
~~~~~~~~~~~~~~~~~

RT Structure Sets are critical for radiation therapy planning and analysis. ViSERA provides a straightforward workflow for importing and processing these specialized files.

How It Works
^^^^^^^^^^

1. **RT Struct Reader Module**: Begin by loading your radiation therapy structure set

   * Requires both a main image and corresponding structure set labels
   * RT Label Directory: Path to the RT structure set file
   * RT Main Image Directory: Path to the corresponding image data
   * Automatically extracts contours and segmentation information

2. **Writer Module**: Connect to the Writer module to save processed RT structures

   * Choose your desired output location
   * Select appropriate format for saving segmentation data
   * Preserve the relationship between images and their associated structures

Workflow Integration
^^^^^^^^^^^^^^^^^

To process RT Struct files:

1. Add an RT Struct Reader module to your workflow
2. Configure the RT Struct Reader with paths to both your main image and structure set labels
3. Add a Writer module to your workflow
4. Connect the output port of the RT Struct Reader to the input port of the Writer
5. Configure the Writer with your desired output location and format
6. Run the workflow to complete the processing

This workflow enables efficient handling of radiation therapy planning data while maintaining the integrity of structure sets and their associated imaging.

Image Filtering
~~~~~~~~~~~~~

Image filtering is essential for enhancing specific features, reducing noise, and preparing images for analysis. ViSERA provides several standardized filters that comply with IBSI guidelines.

How It Works
^^^^^^^^^^

1. **Image Reader Module**: Start by loading the medical image you want to filter

   * Select your source image file or directory
   * The module supports NIFTI, NRRD, and DICOM formats

2. **Filter Module**: Apply one or more filters to the input image

   * **Mean Filter**: Smooths images by replacing each pixel with the average of its neighborhood
   * **LoG (Laplacian of Gaussian)**: Highlights edges and regions of rapid intensity change
   * **Laws Filter**: Extracts texture features using small convolution kernels
   * **Gabor Filter**: Identifies texture and directional features at various scales
   * **Wavelet Filter**: Performs multi-resolution analysis for feature extraction

3. **Writer Module**: Save the filtered image to your desired location

   * Select output location and format
   * Preserve metadata from the original image

Customizable Parameters
^^^^^^^^^^^^^^^^^^^^

Each filter provides adjustable parameters to fine-tune the results:

* **Mean Filter**: Kernel size, boundary handling
* **LoG Filter**: Sigma value, kernel size
* **Laws Filter**: Kernel type, window size
* **Gabor Filter**: Frequency, orientation, bandwidth
* **Wavelet Filter**: Wavelet family, decomposition level, boundary handling

Workflow Integration
^^^^^^^^^^^^^^^^^

To filter medical images:

1. Add an Image Reader module to your workflow
2. Configure the Image Reader to load your source image
3. Add a Filter module to your workflow
4. Connect the output port of the Image Reader to the input port of the Filter
5. Select the desired filter type and adjust parameters
6. Add a Writer module to your workflow
7. Connect the output port of the Filter to the input port of the Writer
8. Configure the Writer with your desired output location and format
9. Run the workflow to apply the filter and save the results

This workflow enables precise control over image enhancement techniques while maintaining compatibility with downstream analysis modules.

Image Fusion
~~~~~~~~~~

Image fusion combines information from multiple images into a single composite image, preserving the most important visual information from each source. This is particularly useful for integrating complementary data from different imaging modalities or acquisition times.

How It Works
^^^^^^^^^^

1. **Image Reader Module**: Load the images you want to fuse

   * You'll need two separate Image Reader modules, one for each input image
   * Both images should have compatible dimensions for proper fusion

2. **Image Fusion Module**: Combine the images using one of three fusion methods

   * **Weighted Fusion**: Linear combination of input images
     
     * Weight 1: Contribution of first image (0-1)
     * Weight 2: Contribution of second image (0-1)
     * Interpolation: Method for combining images (Linear, Cubic, etc.)
   
   * **Wavelet Fusion**: Multi-resolution decomposition and fusion
     
     * Fusion Method: Algorithm for combining wavelet coefficients (Max, Min, Mean)
     * Level: Decomposition level for wavelet transform
     * Mode: Signal extrapolation mode
     * Wavelet: Wavelet family to use (Haar, etc.)
   
   * **PCA Fusion**: Principal Component Analysis based fusion
     
     * Number of Components: Components to use in reconstruction
     * SVD Solver: Algorithm for Singular Value Decomposition
     * Components: Number of principal components

3. **Writer Module**: Save the fused image to your desired location

   * Select output location and format
   * Preserve metadata from the original images

Workflow Integration
^^^^^^^^^^^^^^^^^

To fuse medical images:

1. Add two Image Reader modules to your workflow
2. Configure each Image Reader to load one of your source images
3. Add an Image Fusion module to your workflow
4. Connect the output ports of both Image Readers to the input ports of the Image Fusion module
5. Select the desired fusion method and adjust its parameters
6. Add a Writer module to your workflow
7. Connect the output port of the Image Fusion module to the input port of the Writer
8. Configure the Writer with your desired output location and format
9. Run the workflow to perform the fusion and save the results

This workflow allows you to combine complementary information from different imaging sources into a single comprehensive visualization for improved analysis and interpretation.

Image Registration for AutoPET
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Image registration is a crucial step in medical image analysis, especially for multimodal imaging like PET/CT. This example demonstrates how to register PET and CT images from AutoPET datasets.

How It Works
^^^^^^^^^^

1. **Image Reader Module (Fixed Image)**: Load the CT image as the fixed (reference) image

   * Configure the reader to point to your CT data source
   * CT scans typically provide detailed anatomical information

2. **Image Reader Module (Moving Image)**: Load the PET image as the moving image to be aligned

   * Configure the reader to point to your PET data source
   * PET scans provide functional or metabolic information

3. **Image Registration Module**: Align the PET (moving) image to the CT (fixed) image

   * **Rigid Registration**: Maintains shape and size, only allows rotation and translation
     
     * Number of Histogram Bins: Controls the granularity of intensity matching
     * Sampling Method: Determines how points are sampled during registration
     * Learning Rate: Controls the optimization step size
     * Number of Iterations: Sets the maximum number of optimization steps
     * Interpolation: Method used for interpolating between voxels
   
   * **Non-Rigid Registration**: Allows local deformations for better alignment of soft tissues
     
     * Transform Type: Typically BSplineTransform for PET/CT registration
     * Number of Iterations: Controls the optimization process
     * Final Grid Spacing: Determines the density of the deformation field

4. **Writer Module**: Save the registered PET image

   * Select output location and format
   * The registered image will be aligned to the anatomical reference of the CT image

Workflow Integration
^^^^^^^^^^^^^^^^^

To register AutoPET images:

1. Add an Image Reader module for the fixed (CT) image
2. Configure the first Image Reader to load your CT image
3. Add a second Image Reader module for the moving (PET) image
4. Configure the second Image Reader to load your PET image
5. Add an Image Registration module to your workflow
6. Connect the output port of the CT Image Reader to the "fix image" input port of the Image Registration module
7. Connect the output port of the PET Image Reader to the "moving image" input port of the Image Registration module
8. Select the appropriate registration type and parameters based on your data
9. Add a Writer module to your workflow
10. Connect the output port of the Image Registration module to the input port of the Writer
11. Configure the Writer with your desired output location and format
12. Run the workflow to perform the registration and save the results

This registration workflow enables accurate spatial alignment of functional PET data with anatomical CT data, which is essential for proper localization and quantification of metabolic activity in cancer studies.

PET/CT Registration and Fusion
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This advanced workflow combines both registration and fusion techniques to create comprehensive visualizations from multimodal AutoPET data. The workflow aligns PET images to CT images and then fuses them to combine functional and anatomical information.

How It Works
^^^^^^^^^^

1. **Image Reader Module (CT)**: Load the CT image which serves dual purposes:

   * Acts as the fixed (reference) image for registration
   * Provides anatomical information for the fusion process (Image 2)

2. **Image Reader Module (PET)**: Load the PET image as the moving image to be aligned

   * The PET data contains functional/metabolic information
   * Will be spatially registered to match the CT reference frame

3. **Image Registration Module**: Align the PET image to the CT reference

   * Uses either rigid or non-rigid registration depending on requirements
   * Produces a spatially aligned PET image that matches the CT coordinate system

4. **Image Fusion Module**: Combine the registered PET with the original CT

   * **Input 1**: Registered PET image (from registration module)
   * **Input 2**: Original CT image (directly from CT Image Reader)
   * Creates a single composite image highlighting both structure and function

5. **Writer Module**: Save the fused image for further analysis

   * Preserves both anatomical context and metabolic information
   * Can be saved in various formats for use in clinical or research contexts

Workflow Integration
^^^^^^^^^^^^^^^^^

To implement this PET/CT registration and fusion pipeline:

1. Add two Image Reader modules to your workflow:
   
   * One for the CT image
   * One for the PET image

2. Configure both Image Readers to load the appropriate data

3. Add an Image Registration module and connect:
   
   * CT Image Reader output → "fix image" input
   * PET Image Reader output → "moving image" input

4. Configure registration parameters appropriate for PET/CT alignment:
   
   * For most applications, rigid registration with appropriate histogram bins
   * For soft tissue focus, consider non-rigid registration

5. Add an Image Fusion module and connect:
   
   * Registration module output → "Image 1" input 
   * CT Image Reader output → "Image 2" input

6. Configure fusion parameters:
   
   * For clinical viewing, weighted fusion with customized color maps
   * For feature analysis, consider PCA or wavelet fusion

7. Add a Writer module and connect:
   
   * Fusion module output → Writer input

8. Configure the Writer with your desired output location and format

9. Run the workflow to register, fuse, and save the results

This integrated workflow creates comprehensive visualizations that preserve the metabolic sensitivity of PET while maintaining the anatomical detail of CT, which is particularly valuable for tumor localization, treatment planning, and response assessment in oncology applications.

PET/CT Registration and Filtering
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This workflow combines registration and filtering techniques to enhance specific features in multimodal AutoPET data. The workflow first aligns PET images to CT images and then applies filters to enhance particular features of interest in the registered images.

How It Works
^^^^^^^^^^

1. **Image Reader Module (CT)**: Load the CT image as the fixed (reference) image

   * Provides the anatomical reference frame
   * CT scans offer detailed structural information

2. **Image Reader Module (PET)**: Load the PET image as the moving image

   * Contains functional/metabolic information
   * Will be spatially aligned to match the CT reference frame

3. **Image Registration Module**: Align the PET image to the CT reference

   * Uses either rigid or non-rigid registration depending on requirements
   * Ensures the metabolic activity is precisely localized to anatomical structures

4. **Image Filter Module**: Apply selected filters to the registered PET image

   * Enhances specific features of interest
   * Reduces noise or highlights particular characteristics
   * Available filters include Gabor, Wavelet, Threshold, Gradient, and Smoothing

5. **Writer Module**: Save the filtered registered image

   * Preserves the spatial alignment with anatomical structures
   * Enhanced features are ready for further analysis

Workflow Integration
^^^^^^^^^^^^^^^^^

To implement this PET/CT registration and filtering pipeline:

1. Add two Image Reader modules to your workflow:
   
   * One for the CT image
   * One for the PET image

2. Configure both Image Readers to load the appropriate data

3. Add an Image Registration module and connect:
   
   * CT Image Reader output → "fix image" input
   * PET Image Reader output → "moving image" input

4. Configure registration parameters appropriate for PET/CT alignment:
   
   * For most applications, rigid registration is sufficient
   * For areas with tissue deformation, consider non-rigid registration

5. Add an Image Filter module and connect:
   
   * Registration module output → Filter input

6. Configure filter parameters based on your analysis goals:
   
   * For texture analysis: Gabor or Wavelet filters
   * For edge detection: Gradient filters
   * For noise reduction: Smoothing filters
   * For segmentation preparation: Threshold filters

7. Add a Writer module and connect:
   
   * Filter module output → Writer input

8. Configure the Writer with your desired output location and format

9. Run the workflow to register, filter, and save the results

This workflow is particularly useful for enhancing specific features in registered PET images while maintaining accurate spatial alignment with anatomical structures. It's valuable for improved lesion detection, feature extraction preparation, and preprocessing for advanced analysis like radiomics or AI-based detection.

PET Filtering and Radiomics Analysis
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This workflow demonstrates how to enhance PET images using filters before extracting radiomic features from regions of interest. By preprocessing images with appropriate filters, you can improve feature quality and highlight specific characteristics relevant to your analysis.

How It Works
^^^^^^^^^^

1. **Image Reader Module (PET)**: Load the PET image for analysis

   * Contains functional/metabolic information
   * Source data for feature extraction

2. **Image Reader Module (Segmentation)**: Load the segmentation mask

   * Defines regions of interest (ROIs) such as tumors or specific tissues
   * Can be derived from manual segmentation or automated methods

3. **Image Filter Module**: Apply selected filters to the PET image

   * Enhances specific features or reduces noise
   * Improves the quality of subsequently extracted radiomic features
   * Different filters can highlight different image characteristics

4. **Radiomic Feature Generator**: Extract quantitative features from the filtered image

   * Takes the filtered PET image as the image input
   * Takes the segmentation mask to define ROIs
   * Calculates a wide range of standardized radiomic features from the filtered image within the defined regions

5. **Writer Module**: Save the extracted radiomic features

   * Typically exports as tabular data (CSV, Excel)
   * Preserves all calculated features with appropriate labeling

Workflow Integration
^^^^^^^^^^^^^^^^^

To implement this PET filtering and radiomics pipeline:

1. Add an Image Reader module for the PET image
   
   * Configure to load your PET dataset

2. Add an Image Reader module for the segmentation mask
   
   * Configure to load your segmentation masks that define the regions of interest

3. Add an Image Filter module and connect:
   
   * PET Image Reader output → Filter input

4. Configure filter parameters based on your analysis goals:
   
   * For texture enhancement: Gabor or Wavelet filters
   * For noise reduction: Smoothing filters
   * For edge enhancement: Gradient filters
   * For intensity normalization: Threshold filters

5. Add a Radiomic Feature Generator module and connect:
   
   * Filter module output → "Image" input of the Radiomic Feature Generator
   * Segmentation Image Reader output → "Mask" input of the Radiomic Feature Generator

6. Configure the Radiomic Feature Generator:
   
   * Select appropriate feature categories (first-order, shape, texture)
   * Set discretization parameters
   * Configure any preprocessing options

7. Add a Writer module and connect:
   
   * Radiomic Feature Generator output → Writer input

8. Configure the Writer to save results in your preferred format (typically CSV or Excel)

9. Run the workflow to filter the image, extract features, and save the results

This workflow is valuable for enhancing specific image characteristics before radiomics analysis, which can improve the discriminatory power of extracted features. It's particularly useful in oncology research, where filtered PET images may reveal subtle tumor characteristics not readily apparent in unprocessed images.

Radiomic Feature Extraction
~~~~~~~~~~~~~~~~~~~~~~~~~

Radiomics involves extracting quantitative features from medical images that can be used for clinical decision support. ViSERA provides standardized radiomics analysis that complies with the Image Biomarker Standardization Initiative (IBSI).

How It Works
^^^^^^^^^^

1. **Image Reader Module (Input Image)**: Load the primary medical image for feature extraction

   * Select the source image containing regions of interest
   * Commonly uses CT, MRI, PET, or other imaging modalities

2. **Image Reader Module (Mask Image)**: Load the corresponding segmentation mask

   * The mask delineates the regions of interest (ROIs) for feature extraction
   * Can be created using segmentation tools or imported from RT Structure sets

3. **Radiomic Feature Generator**: Extract quantitative features from the defined regions

   * **Handcrafted Radiomic Features**:
     
     * First-order Statistics: Intensity-based features (mean, median, entropy, etc.)
     * Shape-based Features: Morphological characteristics (volume, surface area, etc.)
     * Texture Features: Spatial patterns (GLCM, GLRLM, GLSZM, etc.)
     * Wavelet Features: Multi-resolution analysis of image patterns
   
   * **Deep Learning Features** (using pre-trained models):
     
     * Transfer learning from established neural network architectures
     * Feature extraction from different network layers
     * Adaptable to various imaging modalities

4. **Writer Module**: Save the extracted features to your chosen format

   * Typically exports as tabular data (CSV, Excel)
   * Preserves all calculated features with appropriate labeling
   * Can be configured for compatibility with statistical analysis tools

Key Parameters
^^^^^^^^^^^^

* **Data Type**: Imaging modality type (CT, MR, PET)
* **Discretization Type**: Method for binning intensity values
* **Bin Size/Count**: Controls the granularity of texture analysis
* **Image Interpolation**: Method for resampling images if needed
* **ROI Interpolation**: How segmentation masks are resampled
* **Isotropic Voxel Size**: For standardizing voxel dimensions
* **Feature Selection**: Options to choose specific feature sets
* **Deep Learning Model**: Selection of pre-trained network (if using deep learning)

Workflow Integration
^^^^^^^^^^^^^^^^^

To extract radiomic features:

1. Add an Image Reader module for your primary image
2. Configure the first Image Reader to load your source medical image
3. Add a second Image Reader module for your mask/segmentation
4. Configure the second Image Reader to load your segmentation mask
5. Add a Radiomic Feature Generator module to your workflow
6. Connect the output ports of both Image Readers to the corresponding input ports of the Radiomic Feature Generator
7. Select the desired feature categories and adjust extraction parameters
8. Add a Writer module to your workflow
9. Connect the output port of the Radiomic Feature Generator to the input port of the Writer
10. Configure the Writer to save results in your preferred format
11. Run the workflow to extract and save the radiomic features

This workflow enables standardized quantitative analysis of medical images, supporting research in personalized medicine, disease characterization, and treatment response prediction.

Installation
-----------

Prerequisites
~~~~~~~~~~~

* Python 3.11 or below

Download
~~~~~~~

.. code-block:: shell

   git clone -b new-year-visera --recurse-submodules git@github.com:MohammadRSalmanpour/ViSERA.git 

Download NodeGraphPySide6 from `this repository <https://github.com/somso2e/NodeGraphPySide6/tree/70043c151c67e74dde7b34c2969b19b02782940a>`_ and replace it with dependencies/NodeGraphPySide6.

Setup
~~~~

.. code-block:: shell

   pip install -r requirements.txt 
   pip install ./dependencies/NodeGraphPySide6/

Running ViSERA
~~~~~~~~~~~~

.. code-block:: shell

   python ./ViSERA

Module Documentation
------------------

Preprocessing
~~~~~~~~~~~

Overview
^^^^^^^

The preprocessing module provides essential data preparation capabilities before applying machine learning algorithms. Proper preprocessing is crucial for achieving optimal model performance.

Available Methods
^^^^^^^^^^^^^^

**1. Data Encoding**

Converts categorical data into numerical format for machine learning algorithms.

.. list-table::
   :header-rows: 1
   :widths: 20 30 25 25

   * - Method
     - Description
     - Use Case
     - Implementation
   * - **Label Encoding**
     - Converts each categorical value to a unique integer
     - Ordinal data where order matters
     - ``sklearn.preprocessing.LabelEncoder``
   * - **One-Hot Encoding**
     - Creates binary columns for each category
     - Nominal data with no inherent order
     - ``sklearn.preprocessing.OneHotEncoder``
   * - **Ordinal Encoding**
     - Converts values to ordinal integers based on specified ordering
     - Data with known category ordering
     - ``sklearn.preprocessing.OrdinalEncoder``

**2. Data Splitting**

Divides the dataset into training, validation, and test sets.

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Method
     - Key Parameters
   * - **Percentage Split**
     - Train Split (50-95%), Shuffle, Random Seed
   * - **K-fold Cross-Validation**
     - K (2-10), Random Seed

**3. Data Imputation**

Handles missing values in the dataset.

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Method
     - Key Parameters
   * - **Simple Imputer**
     - Strategy (mean, median, mode, constant)
   * - **KNN Imputer**
     - N Neighbors, Weights, Distance Metric
   * - **Iterative Imputer**
     - Initial Strategy, Estimator, Max Iterations

**4. Data Scaling**

Standardizes feature ranges to improve model performance.

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Method
     - Key Parameters
   * - **Robust Scaler**
     - Quantile Range
   * - **Min-Max Scaler**
     - Min, Max values
   * - **Standard Scaler**
     - None
   * - **Normalizer**
     - Norm type (l1, l2, max)
   * - **MaxAbs Scaler**
     - None

**5. Feature Selection/Extraction**

Reduces dimensionality by selecting important features or creating composite features.

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Method
     - Key Parameters
   * - **SelectKBest**
     - Score Function, Number of Features
   * - **SelectPercentile**
     - Score Function, Percentile
   * - **Variance Threshold**
     - Threshold
   * - **PCA**
     - Components, SVD Solver, Whiten
   * - **Kernel PCA**
     - Components, Kernel type, Parameters
   * - **Factor Analysis**
     - Components, Rotation
   * - **Fast ICA**
     - Components, Algorithm, Fun

Workflow Integration
^^^^^^^^^^^^^^^^^

1. Data Loading
2. Encoding
3. Data Splitting
4. Imputation
5. Scaling
6. Feature Selection
7. Model Training

Best Practices
^^^^^^^^^^^

1. Always encode categorical variables
2. Handle missing values appropriately
3. Scale features for better performance
4. Select relevant features to reduce dimensionality
5. Keep random states consistent for reproducibility
6. Use cross-validation for reliable evaluation
7. Reserve test data until final evaluation

Classification
~~~~~~~~~~~

Overview
^^^^^^^

The Classification module provides multiple algorithms for data analysis with customizable parameters through an intuitive user interface.

Supported Algorithms
^^^^^^^^^^^^^^^^^

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
^^^^^^^^^^^^^^^^^^^^

1. Select and configure algorithms
2. Apply preprocessing steps
3. Train models
4. Evaluate using standard metrics
5. Compare algorithm performance

Regression
~~~~~~~~

Overview
^^^^^^^

The Regression module provides multiple algorithms for predicting continuous target variables.

Supported Algorithms
^^^^^^^^^^^^^^^^^

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
^^^^^^^^^^^^^^^

* Mean Absolute Error (MAE)
* Root Mean Squared Error (RMSE)
* R-squared Score
* Median Absolute Error

Clustering
~~~~~~~~

Overview
^^^^^^^

The Clustering module provides algorithms for grouping similar data points without labeled training data.

Supported Algorithms
^^^^^^^^^^^^^^^^^

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

**5. K-Medoids Clustering**

More robust to noise and outliers than K-Means.

**Key Parameters:**

* Number of Clusters
* Distance Metric
* Method (alternate, pam)
* Initialization Method

Evaluation Metrics
^^^^^^^^^^^^^^^

* Completeness Score
* Homogeneity Score
* V-measure Score
* Adjusted Rand Index
* Silhouette analysis

Optimization Techniques
^^^^^^^^^^^^^^^^^^^

* Elbow method for optimal cluster number
* Silhouette analysis for cluster validation
