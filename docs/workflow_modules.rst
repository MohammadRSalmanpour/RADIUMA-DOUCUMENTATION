Workflow Modules
================

ViSERA offers a comprehensive set of modules that can be connected to create end-to-end research workflows. These modules cover the entire radiomics pipeline from image input to statistical analysis.

.. contents:: :local:

Image Viewer
------------

The Medical Image Viewer is a comprehensive module designed for advanced medical image visualization and analysis, providing tools for detailed examination, segmentation, and analysis of medical imaging data.

View Types
^^^^^^^^^^

* **Axial View**: Horizontal cross-sections (top-down view)
* **Sagittal View**: Vertical cross-sections from side to side
* **Coronal View**: Vertical cross-sections from front to back
* **3D View**: Complete three-dimensional rendering with:

  * Volume View: Full 3D visualization of image data
  * Mask View: Visualization of segmentation results

File Support
^^^^^^^^^^^^

* NIFTI Files: Support for Neuroimaging Informatics Technology Initiative format
* DICOM Files: Individual DICOM image support
* DICOM Directories: Support for complete DICOM studies/series
* Segmentation Files: Import/export of segmentation data

Toolbar Functions
^^^^^^^^^^^^^^^^^

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

Advanced Features
^^^^^^^^^^^^^^^^

**Segmentation Workflow**

1. Open the image file in ViSERA
2. Select the "Segmentation" tool from the toolbar
3. Choose the segmentation method (Manual or Threshold)
4. Define the area to segment and press OK or press "Enter"
5. Add label types or create a new label
6. Fine-tune the segmentation using tools like the "Eraser"
7. Save the segmentation as a new image file

**Label Management**

* Edit and customize label colors through the "Labels" option
* Apply multiple segments using the "Apply" button in the segmentation tools
* Manage multiple segmentations simultaneously for complex structures

**Image Transformation**

1. Use the "Transforms" button in the toolbar
2. Select transformation options (flipping, rotating, etc.)
3. Reset transformations with the "Clear Transformation" button
4. Access additional transformation options through the "Cursor" button

**Image Information**

* View detailed image metadata by clicking "more info"
* Access acquisition parameters, dimensions, and other technical details

**Contrast Adjustment**

* Modify image contrast using the "Contrast" tool in the toolbar
* Fine-tune visualization for optimal feature visibility
* Apply presets or create custom window/level settings

**Display Layout**

* Switch between different view layouts (axial, sagittal, coronal, 3D)
* Customize layout configuration for specific analysis needs
* Toggle between single-view and multi-view layouts

Image Reader
------------

A flexible module for importing various medical image formats into the ViSERA workflow.

Key Parameters
^^^^^^^^^^^^^^

* **Source Type**: Choose between folder or single file import
* **Path**: Location of the medical image file(s) to import

Supported Input Formats
^^^^^^^^^^^^^^^^^^^^^^^

* DICOM Files and Directories
* NIFTI Files (.nii, .nii.gz)
* Various other medical image formats

Workflow Integration
^^^^^^^^^^^^^^^^^^^^

* Outputs to Image Convertor
* Outputs to Image Filter
* Outputs to Image Fusion
* Outputs to Image Registration

RT Struct Reader
----------------

Specialized module for importing radiotherapy structure sets, supporting the standardized DICOM-RT format used in radiation oncology.

Key Parameters
^^^^^^^^^^^^^^

* **RT Label Directory**: Path to the RT structure set file
* **RT Main Image Directory**: Path to the corresponding image data

Functionality
^^^^^^^^^^^^^^

* Imports DICOM-RT structure sets along with their associated images
* Extracts contours and segmentation information
* Provides labeled structures for further analysis

Workflow Integration
^^^^^^^^^^^^^^^^^^^^

* Outputs to Radiomic Feature Generator
* Outputs to Image Writer
* Outputs to Image Viewer

Table Reader/Writer
-------------------

Modules for importing and exporting tabular data in various formats.

Reader Parameters
^^^^^^^^^^^^^^^^^

* **File Path**: Location of the input data file
* **Format Detection**: Automatic detection of file format

Writer Parameters
^^^^^^^^^^^^^^^^^

* **Path**: Destination for saving the output data
* **File Format**: Choice of output format (.xlsx, .csv, .dcm, .nii.gz, .nrrd)
* **Single/Multi File**: Option to save as single file or multiple files

Supported Formats
^^^^^^^^^^^^^^^^^

* CSV files
* Excel spreadsheets
* Structured data exports from analysis modules

Advanced Table Operations
^^^^^^^^^^^^^^^^^^^^^^^^^

The Table Reader module allows users to import, combine, and manipulate tabular data for further analysis. It supports merging tables either by rows (concatenation) or by columns, making it a versatile tool for integrating datasets.

**Operation Types**

* **Row Concatenation**: Combine tables by adding rows from one table below another
* **Column Merge**: Combine tables by adding columns from one table alongside another

**Row Concatenation Parameters**

* **Ignore Index**: Check this box to reset the row index in the combined table
* **How**: Choose the merge method (inner, outer, left, right)

**Column Merge Parameters**

* **Ignore Index**: Check this box to reset the row index in the combined table
* **Indicator**: Add a column indicating the source of each row
* **How**: Choose the merge method (inner, outer, left, right)

Writer Module Capabilities
^^^^^^^^^^^^^^^^^^^^^^^^^^

The Writer module allows you to export processed data, images, or analysis results into various file formats. This ensures that your work can be saved and shared in a format that suits your needs, whether for further analysis, reporting, or collaboration.

**Supported Export Formats**

* **.nii.gz**: Nifti format for medical imaging
* **.nrrd**: Nrrd format for medical imaging
* **.dcm (single dicom)**: Single DICOM file
* **.dcm (multi dicom)**: Multiple DICOM files in a folder
* **.xlsx**: Excel format for tabular data
* **.csv**: Comma-separated values format for tabular data

Image Registration
------------------

Tools for spatial alignment of images from different modalities or time points.

Registration Types
^^^^^^^^^^^^^^^^^^

* **Rigid Registration**: Maintains shape and size, only allows rotation and translation
* **Non-Rigid Registration**: Allows local deformations for better alignment
* **Simple Non-Rigid**: Simplified version of non-rigid registration for faster processing

Key Parameters
^^^^^^^^^^^^^^

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
^^^^^^^^^^^^^^^^^^^^

* Takes fixed and moving images as inputs
* Outputs transformed image aligned to reference

Image Filter
------------

Comprehensive set of image filtering options for enhancing features, reducing noise, and preparing images for feature extraction.

Filter Types
^^^^^^^^^^^^

* **Gabor Filter**: Texture and edge detection
* **Wavelet Filter**: Multi-scale analysis
* **Threshold Filter**: Simple intensity-based filtering
* **Gradient Filter**: Edge enhancement
* **Smoothing Filter**: Noise reduction

Key Parameters
^^^^^^^^^^^^^^

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
^^^^^^^^^^^^^^^^^^^^^

* Takes image input
* Applies selected filtering techniques
* Outputs filtered image for further processing

Image Fusion
------------

Advanced capabilities for combining information from multiple imaging modalities.

Fusion Methods
^^^^^^^^^^^^^^

* **Weighted Fusion**: Linear combination of input images
* **Wavelet Fusion**: Multi-resolution decomposition and fusion
* **PCA Fusion**: Principal Component Analysis based fusion

Key Parameters
^^^^^^^^^^^^^^

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
^^^^^^^^^^^^^^^^^^^^^

* Takes two input images
* Combines information according to selected method
* Outputs a single fused image

Benefits of Image Fusion
^^^^^^^^^^^^^^^^^^^^^^^^

Since different image modalities such as MRI, ultrasound, CT, SPECT, PET, and others include specific information (perspectives) of the same object, image fusion techniques enable users to:

* Combine two or more images to enhance information content
* Improve performance of object recognition systems by integrating many sources
* Help in sharpening images
* Improve geometric corrections
* Enhance features not visible in either of the images
* Replace defective data
* Complement data sets for better decision making
* Reduce ambiguity and enhance reliability of defect detection

Radiomic Feature Generator
--------------------------

Core module for extracting standardized quantitative features from medical images following IBSI guidelines.

Feature Types
^^^^^^^^^^^^^^

* **First-order Statistics**: Intensity-based features
* **Shape-based Features**: Morphological characteristics
* **Texture Features**: Spatial patterns (GLCM, GLRLM, etc.)
* **Wavelet Features**: Multi-resolution analysis

Key Parameters
^^^^^^^^^^^^^^

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
^^^^^^^^^^^^^^^^^^^^^

* Takes both image and mask inputs
* Extracts features according to standardized definitions
* Outputs tabular data with all calculated features 

Comprehensive Feature Set
^^^^^^^^^^^^^^^^^^^^^^^^^

The Radiomic Feature Generator module (also known as PySERA) calculates 487 IBSI 1-standardized features, including:

* 79 first-order features (morphology, statistical, histogram, and intensity-histogram features)
* 272 higher-order 2D features
* 136 3D features

It can also calculate 10 moment invariant features not included in IBSI 1, bringing the total to 497 imaging features.

Feature Categories
^^^^^^^^^^^^^^^^^^

* **Morphology**: 29 features
* **Local Intensity**: 2 features
* **Intensity-based Statistics**: 18 features
* **Intensity Histogram**: 23 features
* **Intensity-Volume Histogram**: 7 features
* **Gray Level Co-occurrence Matrix (GLCM)**: 25 features per method (2D Averaged, 2D Slice-Merged, 2.5D Direction Merged, 2.5D All Merged, 3D Averaged, 3D Merged)
* **Gray Level Run Length Matrix (GLRLM)**: 16 features per method (2D Averaged, 2D Slice-Merged, 2.5D Direction Merged, 2.5D All Merged, 3D Averaged, 3D Merged)
* **Gray Level Size Zone Matrix (GLSZM)**: 16 features per method (2D, 2.5D, 3D)
* **Gray Level Distance Zone Matrix (GLDZM)**: 16 features per method (2D, 2.5D, 3D)
* **Neighborhood Grey Tone Difference Matrix (NGTDM)**: 5 features per method (2D, 2.5D, 3D)
* **Neighboring Grey Level Dependence Matrix (NGLDM)**: 17 features per method (2D, 2.5D, 3D)
* **Moment Invariants**: 10 features

Extended Parameters
^^^^^^^^^^^^^^^^^^^

* **Image modality type**: PET, CT, or MR
* **Discretization type**: FBN (fixed bin numbers) or FBS (fixed bin size/width)
* **Bin size/width**: Number of bins or width of each bin
* **Resampling flag**: Whether to perform scaling (1 to enable, 0 to use original voxel dimension)
* **Isotropic 2D voxels flag**: Whether to resample to isotropic 2D voxels or 3D voxels
* **Round voxel intensity value flag**: Whether to round intensity values to nearest integer
* **Range resegmentation flag**: Whether to perform range re-segmentation
* **Intensity outlier resegmentation flag**: Whether to filter outlier intensities
* **Image quantization flag**: Whether to use quantized image for first-order features
* **Resegmentation interval range**: Intensity range for resegmentation
* **ROI partial volume threshold**: Threshold for ROI after resampling
* **Quantization type**: Uniform or Lloyd
* **IVH Type**: Setting for Intensity Volume Histogram unit type
* **IVH discretization type**: Discrete or Continuous
* **Type of output data**: Which set of features to return

Standards Compliance
^^^^^^^^^^^^^^^^^^^^

The Radiomic Feature Generator is meticulously consistent with SERA and compliant with IBSI 1.0 standards while also being standardized against IBSI 2.0, ensuring reliability and reproducibility across research. 