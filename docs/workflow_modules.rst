Workflow Modules
===============

Radiuma offers a comprehensive set of modules that can be connected to create end-to-end research workflows. These modules cover the entire radiomics pipeline from image input to statistical analysis.

.. contents:: :local:

Image Viewer
------------

.. image:: images/5.image_viewer.png
   :alt: Image Viewer
   :width: 100%

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

.. image:: images/file_support.png
   :alt: Image Viewer
   :width: 100%

* NIFTI Files: Support for Neuroimaging Informatics Technology Initiative format
* DICOM Files: Individual DICOM image support
* DICOM Directories: Support for complete DICOM studies/series
* Segmentation Files: Import/export of segmentation data
* RT Structure Files: Import RT structure files

Toolbar Functions
^^^^^^^^^^^^^^^^^

.. image:: images/image_viewer_buttons.png
   :alt: Image Viewer Buttons
   :width: 100%

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
------------

.. image:: images/6.image_reader.png
   :alt: Image Reader
   :width: 100%

A flexible module for importing various medical image formats into the Radiuma workflow.

Key Parameters
^^^^^^^^^^^^^^

* **Source Type**: Choose between folder or single file import
* **Path**: Location of the medical image file(s) to import

Supported Input Formats
^^^^^^^^^^^^^^^^^^^^^^^

* DICOM Files and Directories
* NIFTI Files (.nii, .nii.gz and not directories)
* NRRD Files (.nrrd)
* Various other medical image formats

Workflow Integration
^^^^^^^^^^^^^^^^^^^^

* Outputs to Image Convertor
* Outputs to Image Filter
* Outputs to Image Fusion
* Outputs to Image Registration

RT Struct Reader
----------------

.. image:: images/7.rt_struct_reader.png
   :alt: RT Struct Reader
   :width: 100%

Specialized module for importing radiotherapy structure sets, supporting the standardized DICOM-RT format used in radiation oncology.

Key Parameters
^^^^^^^^^^^^^^

* **RT Label Directory**: Path to the RT structure set file
* **RT Main Image Directory**: Path to the corresponding image data

Functionality
^^^^^^^^^^^^^

* Imports DICOM-RT structure sets along with their associated images
* Extracts contours and segmentation information
* Provides labeled structures for further analysis

Workflow Integration
^^^^^^^^^^^^^^^^^^^^

* Outputs to Radiomic Feature Generator
* Outputs to Image Writer
* Outputs to Image Viewer

Table Reader
------------

.. image:: images/8.table_reader.png
   :alt: Table Reader
   :width: 100%

Modules for importing tabular data in various formats.

Reader Parameters
^^^^^^^^^^^^^^^^^

* **File Path**: Location of the input data file
* **Format Detection**: Automatic detection of file format

Supported Formats
^^^^^^^^^^^^^^^^^

* CSV files
* Excel spreadsheets
* Structured data exports from analysis modules

Image/Table Writer
------------------

.. image:: images/9.writer.png
   :alt: Writer
   :width: 100%

Modules for exporting tabular and image data in various formats.

Writer Parameters
^^^^^^^^^^^^^^^^^

* **File or Folder Path**: Location of the input data file or folder
* **Format**: Choice of output format (.xlsx, .csv, single/multiple .dcm, .nii.gz, .nrrd)

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
* DICOM files
* NIFTI files
* NRRD files

Image Registration
------------------

.. image:: images/10.image_registration.png
   :alt: Image Registration
   :width: 100%

Tools for spatial alignment of images from different modalities or time points.

Registration Types
^^^^^^^^^^^^^^^^^^

* **Rigid Registration**: Maintains shape and size, only allows rotation and translation
* **Non-Rigid Registration**: Allows local deformations for better alignment
* **Simple Non-Rigid**: Simplified version of non-rigid registration for faster processing

References
^^^^^^^^^^

* **Rigid Registration**: Besl, P.J. and McKay, N.D. (1992). "A Method for Registration of 3-D Shapes." IEEE Transactions on Pattern Analysis and Machine Intelligence, 14(2), 239-256.
* **Non-Rigid Registration**: Rueckert, D., Sonoda, L.I., Hayes, C., Hill, D.L.G., Leach, M.O., and Hawkes, D.J. (1999). "Nonrigid Registration Using Free-Form Deformations: Application to Breast MR Images." IEEE Transactions on Medical Imaging, 18(8), 712-721.
* **Simple Non-Rigid**: Thirion, J.P. (1998). "Image Matching as a Diffusion Process: An Analogy with Maxwell's Demons." Medical Image Analysis, 2(3), 243-260.

Key Parameters
^^^^^^^^^^^^^^

**Rigid Registration**

* **Number of Histogram Bins**: Value for intensity histograms (default: 10)
* **Sampling Method**: Method for sampling points during registration (None, Random, Regular)
* **Sampling Percentage**: Percentage of voxels to sample (default: 0.01)
* **Learning Rate**: Step size for optimization (default: 0.01)
* **Number of Iterations**: Maximum iterations for optimization (default: 5)
* **Interpolation**: Method for interpolation (Linear, NearestNeighbor, BSpline, etc.)

**Non-Rigid Registration**

* **Number of Iterations**: Iterations for deformable registration (default: 5)
* **Number of Resolutions**: Multi-resolution levels for optimization (default: 1)
* **Final Grid Spacing**: Density of deformation field (default: 1)
* **Transform Type**: Transform method (BSplineTransform is default)
* **Auto-Transform**: Automatic adjustment of transform parameters (True/False)
* **Auto-Scale**: Automatic scaling during registration (True/False)

**Simple Non-Rigid Registration**

* **Enable Simple Registration**: Toggle simplified non-rigid registration

Workflow Integration
^^^^^^^^^^^^^^^^^^^^

* Takes fixed and moving images as inputs
* Outputs transformed image aligned to reference

Image Filter
------------

.. image:: images/11.image_filter.png
   :alt: Image Filter
   :width: 100%

Comprehensive set of image filtering options for enhancing features, reducing noise, and preparing images for feature extraction.

Filter Types
^^^^^^^^^^^^

* **Mean Filter**: Smooths images by reducing noise while preserving edges
* **LoG (Laplacian of Gaussian) Filter**: Highlights edges and regions of rapid intensity change
* **Laws Filter**: Extracts texture features using small convolution kernels
* **Gabor Filter**: Texture and edge detection at various orientations and scales
* **Wavelet Filter**: Multi-scale analysis for feature extraction

Key Parameters
^^^^^^^^^^^^^^

**Common Parameters**
* **Filter Type**: Selection of filter algorithm (Mean, LoG, Laws, Gabor, Wavelet)
* **Slice/Volume Processing**: 2D or 3D filtering
* **Boundary Condition**: Handling of image boundaries (Nearest, Zero, etc.)

**Mean Filter**
* **Filter Size**: Size of the kernel for mean calculation (default: 1)

**LoG Filter**
* **Sigma**: Scale parameter for Gaussian (default: 1)
* **Sigma Truncate**: Truncation factor for Gaussian kernel (default: 1)
* **Calculate Average**: Whether to calculate average in filter (default: False)
* **Riesz Steered**: Apply Riesz transform (default: False)
* **Riesz Parameters**: Parameters for Riesz transform (default: "1,0,2")

**Laws Filter**
* **Kernel**: Specific Laws kernel to apply (default: "L5S5E5")
* **Calculate Energy**: Calculate energy statistics (default: False)
* **Delta**: Step size parameter (default: 1)
* **Rotation Invariance**: Enable rotation invariance (default: False)
* **Pooling Method**: Method for combining filter responses (default: "Max")

**Gabor Filter**
* **Gamma**: Controls filter shape (default: 1)
* **Lambda**: Wavelength of sinusoidal factor (default: 0.1)
* **Theta Initial**: Starting orientation of filter (default: 0.1)
* **Step**: Increment value for filter application (default: 0.001)
* **Response**: Type of filter response (default: "Abs")
* **Rotation Invariance**: Enable rotation invariance (default: False)
* **Pooling Method**: Method for combining filter responses (default: "Max")
* **Sigma**: Sigma value for Gabor kernel (default: 1)
* **Sigma Truncate**: Truncation factor for Gaussian kernel (default: 1)

**Wavelet Filter**
* **Filter Configuration**: Specific wavelet decomposition level to use (default: "LL")
* **Filter Size**: Size of the filter kernel (default: 1)
* **Rotation Invariance**: Enable rotation invariance (default: False)
* **Pooling Method**: Method for combining filter responses (default: "Max")
* **Decomposition Level**: Number of wavelet transform levels (default: 1)
* **Wavelet Family**: Type of wavelet (default: "Db")
* **Wavelet Type**: Specific wavelet implementation (default: "Db1")
* **Riesz Steered**: Apply Riesz transform (default: False)
* **Riesz Parameters**: Parameters for Riesz transform (default: "1,0,2")

Workflow Integration
^^^^^^^^^^^^^^^^^^^^

* Takes image input
* Applies selected filtering techniques
* Outputs filtered image for further processing

Image Fusion
------------

.. image:: images/12.image_fusion.png
   :alt: Image Fusion
   :width: 100%

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
^^^^^^^^^^^^^^^^^^^^

* Takes two input images
* Combines information according to selected method
* Outputs a single fused image

Radiomic Feature Generator
------------------------

.. image:: images/13.radiomic.png
   :alt: Radiomic Feature Generator
   :width: 100%

Core module for extracting standardized quantitative features from medical images following IBSI guidelines.

Feature Types
^^^^^^^^^^^^^

* **First-order Statistics**: Intensity-based features
* **Shape-based Features**: Morphological characteristics
* **Texture Features**: Spatial patterns (GLCM, GLRLM, etc.)
* **Wavelet Features**: Multi-resolution analysis

Key Parameters
^^^^^^^^^^^^^^

* **Data Type**: Modality type (MR, CT, PET, OTHER)
* **Discretization Type**: Method for binning intensity values (FBS, FBN)
* **Bin Size**: Size of intensity bins for feature calculation
* **Resampling Flag**: Whether to perform scaling (0: disabled, 1: enabled)
* **Image Interpolation**: Method for resampling images (Nearest, Linear, Cubic)
* **ROI Interpolation**: Method for resampling masks (Nearest, Linear, Cubic)
* **3D Isotropic Voxel Size**: Size for resampling to isotropic voxels
* **2D Isotropic Voxel Size**: Size for 2D isotropic voxels
* **Isotropic 2D Voxels Flag**: Whether to resample to 2D isotropic voxels
* **Intensity Rounding**: Option to round intensity values (0: disabled, 1: enabled)
* **Segmentation Range**: Option to limit intensity range (0: disabled, 1: enabled)
* **Resegmentation Interval**: Min and max values for intensity range
* **Outlier Filtering**: Methods for handling outliers (0: disabled, 1: enabled)
* **Quantization Method**: Approach for discretizing intensities (Uniform, Lloyd)
* **Intensity Volume Histogram Type**: Setting for IVH unit type
* **IVH Discretization Type**: Discrete or Continuous (1, 2, 3)
* **IVH Bin Size**: Bin size for IVH discretization
* **Maximum ROIs**: Number of regions to analyze per image (Maximum or specific number)
* **ROIs per Image**: Number of ROIs to process when not set to Maximum
* **Combine ROIs**: Whether to combine ROIs for analysis (0: disabled, 1: enabled)
* **Features to Output**: Which feature set to calculate (options from 487 total features)

Workflow Integration
^^^^^^^^^^^^^^^^^^^^

* Takes both image and mask inputs
* Extracts features according to standardized definitions
* Outputs tabular data with all calculated features 