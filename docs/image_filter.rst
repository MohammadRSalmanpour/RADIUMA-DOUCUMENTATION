Image Filter
------------

.. image:: images/11.image_filter.png
   :alt: Image Filter
   :width: 100%
   
Comprehensive set of image filtering options for enhancing features, reducing noise, and preparing images for feature extraction.  
Supports 2D or 3D filtering modes with customizable boundary conditions (e.g., Nearest, Zero, etc.).

Mean Filter
^^^^^^^^^^^^
.. image:: images/11.image_filter_mean.png
   :alt: Image Filter
   :width: 100%

Smooths images by reducing noise while preserving edges
**Key Parameters**
* **Filter Size**: Size of the kernel for mean calculation (default: 1)


LoG (Laplacian of Gaussian) Filter
^^^^^^^^^^^^
.. image:: images/11.image_filter_log.png
   :alt: Image Filter LoG
   :width: 100%

Highlights edges and regions of rapid intensity change

**Key Parameters**
* **Sigma**: Scale parameter for Gaussian (default: 1)
* **Sigma Truncate**: Truncation factor for Gaussian kernel (default: 1)
* **Calculate Average**: Whether to calculate average in filter (default: False)
* **Riesz Steered**: Apply Riesz transform (default: False)
* **Riesz Parameters**: Parameters for Riesz transform (default: "1,0,2")

Laws Filter
^^^^^^^^^^^^
.. image:: images/11.image_filter_laws.png
   :alt: Image Filter Laws
   :width: 100%

Extracts texture features using small convolution kernels

**Key Parameters**
* **Kernel**: Specific Laws kernel to apply (default: "L5S5E5")
* **Calculate Energy**: Calculate energy statistics (default: False)
* **Delta**: Step size parameter (default: 1)
* **Rotation Invariance**: Enable rotation invariance (default: False)
* **Pooling Method**: Method for combining filter responses (default: "Max")


Gabor Filter
^^^^^^^^^^^^

.. image:: images/11.image_filter_gabor.png
   :alt: Image Filter Gabor
   :width: 100%

Texture and edge detection at various orientations and scales

**Key Parameters**
* **Gamma**: Controls filter shape (default: 1)
* **Lambda**: Wavelength of sinusoidal factor (default: 0.1)
* **Theta Initial**: Starting orientation of filter (default: 0.1)
* **Step**: Increment value for filter application (default: 0.001)
* **Response**: Type of filter response (default: "Abs")
* **Rotation Invariance**: Enable rotation invariance (default: False)
* **Pooling Method**: Method for combining filter responses (default: "Max")
* **Sigma**: Sigma value for Gabor kernel (default: 1)
* **Sigma Truncate**: Truncation factor for Gaussian kernel (default: 1)


Wavelet Filter
^^^^^^^^^^^^

.. image:: images/11.image_filter_wavelet.png
   :alt: Image Filter Wavelet
   :width: 100%
   
* **Wavelet Filter**: Multi-scale analysis for feature extraction

**Key Parameters**
* **Filter Configuration**: Specific wavelet decomposition level to use (default: "LL")
* **Filter Size**: Size of the filter kernel (default: 1)
* **Rotation Invariance**: Enable rotation invariance (default: False)
* **Pooling Method**: Method for combining filter responses (default: "Max")
* **Decomposition Level**: Number of wavelet transform levels (default: 1)
* **Wavelet Family**: Type of wavelet (default: "Db")
* **Wavelet Type**: Specific wavelet implementation (default: "Db1")
* **Riesz Steered**: Apply Riesz transform (default: False)
* **Riesz Parameters**: Parameters for Riesz transform (default: "1,0,2")


Common Parameters
^^^^^^^^^^^^^^^^^^

* **Slice/Volume Processing**: 2D or 3D filtering  
* **Boundary Condition**: Handling of image boundaries (Nearest, Zero, etc.)



Workflow Integration
^^^^^^^^^^^^^^^^^^^^
.. image:: images/11.filter_workflow.png
   :alt: Filter Workflow Integration
   :width: 100%

* Takes image input
* Applies selected filtering techniques
* Outputs filtered image for further processing
