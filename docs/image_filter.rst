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
