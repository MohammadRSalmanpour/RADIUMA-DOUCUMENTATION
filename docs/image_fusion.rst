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
