Welcome to Radiuma Documentation
=================================

Radiuma - Visualized & Standardized Environment for Radiomics Analysis is a powerful workflow generator for standardized radiomics analysis and medical image visualization. It provides a free, open-source platform specialized for visualization, processing, segmentation, registration, fusion, and analysis of medical/biomedical images, including radiomics and machine learning capabilities.

.. toctree::
   :maxdepth: 3
   :caption: Contents:

   overview
   key_features
   visual_node_system
   workflow_modules
   examples
   module_documentation

Overview
--------

Radiuma is a Python-based desktop software designed to improve usability, reusability, and reproducibility in medical image analysis. Our lightweight interface combines the simplicity of visual programming with the power of Python frameworks.

The platform employs numerous popular image processing algorithms to create end-to-end standardized workflows, making it an ideal development platform for reproducible research by connecting different tools.

Key Features
------------

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
* **Multi-Tab Workflow Support**: Run multiple independent workflows simultaneously
* **Workflow Control System**: Granular control over workflow execution with both node-level and global stopping capabilities

Visual Node-Based Workflow System
---------------------------------

Radiuma uses a visual programming approach where modules are represented as nodes that can be connected to create complete data processing pipelines. This intuitive interface allows users with minimal programming experience to build sophisticated workflows.

Creating Workflows
~~~~~~~~~~~~~~~~~~

1. **Adding Modules**: Double-click on a module from the module palette to add it to the workspace
2. **Configuring Modules**: Double-click on a module node to open its configuration dialog
3. **Connecting Modules**: Click and drag from an output port to an input port to create connections
4. **Running Workflows**: Click the "Run" button on a node to execute it and all its prerequisite nodes
5. **Stopping Execution**: Click the "Stop" button on a running node or use the global "Stop Workflow" button in the log bar to halt execution

Multi-Tab Workflow Support
~~~~~~~~~~~~~~~~~~~~~~~~~~

Radiuma allows you to work with multiple workflows simultaneously through its tab-based interface:

1. **Creating New Tabs**: Click the "+" button on the tab bar or use the context menu to add a new workflow tab
2. **Renaming Tabs**: Right-click on a tab and select "Rename" to give your workflow a descriptive name
3. **Tab Management**: Each tab maintains its own independent workflow state and execution
4. **Importing Workflows**: When you import a saved workflow, it opens in a new tab automatically
5. **Drag and Drop**: You can drag .radioma files directly onto the application to open them in new tabs

Module Compatibility
~~~~~~~~~~~~~~~~~~~~

Each module explicitly defines which other modules can connect to its inputs and outputs, ensuring that only valid connections can be made:

* **Image Reader**: Outputs to Image Convertor, Filter, Fusion, and Registration modules
* **RT Struct Reader**: Outputs to Radiomic Feature Generator and Image Writer modules
* **Image Filter**: Takes image input, outputs to multiple imaging modules
* **Radiomic Feature Generator**: Takes image and mask inputs, outputs to data analysis modules
* **Preprocessing**: Takes feature data, connects to machine learning modules
* **Classification/Regression/Clustering**: Take preprocessed data as input, connect to visualization

Example Workflows
~~~~~~~~~~~~~~~~~

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
~~~~~~~~~~~~~~~~~

* **Layout Management**: Automatically arrange nodes with the "Align Modules" function
* **Module Search**: Quickly find modules using the search function (Tab key)
* **Copy/Paste**: Duplicate node configurations to create similar processing steps
* **Save/Load**: Save entire workflows and reload them for future use
* **Workflow Stopping**: Two ways to stop a running workflow:
   * **Node-level Stop**: Click the stop button on an individual running node
   * **Global Stop**: Use the "Stop Workflow" button in the log bar to terminate all running tasks

Keyboard Shortcuts
~~~~~~~~~~~~~~~~~~

* **Tab**: Open module search
* **Ctrl+C / Cmd+C**: Copy selected nodes
* **Ctrl+V / Cmd+V**: Paste nodes
* **Delete**: Remove selected nodes
* **D**: Lock/Unlock nodes

Workflow Modules
----------------

Radiuma offers a comprehensive set of modules that can be connected to create end-to-end research workflows. These modules cover the entire radiomics pipeline from image input to statistical analysis.

Image Viewer
~~~~~~~~~~~~

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

Image Reader
~~~~~~~~~~~~

A flexible module for importing various medical image formats into the Radiuma workflow.

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
~~~~~~~~~~~~~~~~

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

Table Reader/Writer
~~~~~~~~~~~~~~~~~~~

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

Image Registration
~~~~~~~~~~~~~~~~~

Tools for spatial alignment of images from different modalities or time points.

Registration Types
^^^^^^^^^^^^^^^^^

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
~~~~~~~~~~~~

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
