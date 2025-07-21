Image Registration
------------------

.. image:: images/10.image_registration.png
   :alt: Image Registration
   :width: 100%
   
Tools for spatial alignment of images from different modalities or time points.
Note:

Registration Types
^^^^^^^^^^^^^^^^^^
.. image:: images/10.image_registration.png
   :alt: Image Registration
   :width: 100%

* **Rigid Registration**: Maintains shape and size, only allows rotation and translation

.. image:: images/10.image_registration_non_rigid.png
   :alt: Image Registration Non Rigid
   :width: 100%

* **Non-Rigid Registration**: Allows local deformations for better alignment

.. image:: images/10.image_registration_simple_non_rigid.png
   :alt: Image Registration Simple Non Rigid
   :width: 100%
   
* **Simple Non-Rigid**: Simplified version of non-rigid registration for faster processing


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


References
^^^^^^^^^^

* **Rigid Registration**: Besl, P.J. and McKay, N.D. (1992). "A Method for Registration of 3-D Shapes." IEEE Transactions on Pattern Analysis and Machine Intelligence, 14(2), 239-256.
* **Non-Rigid Registration**: Rueckert, D., Sonoda, L.I., Hayes, C., Hill, D.L.G., Leach, M.O., and Hawkes, D.J. (1999). "Nonrigid Registration Using Free-Form Deformations: Application to Breast MR Images." IEEE Transactions on Medical Imaging, 18(8), 712-721.
* **Simple Non-Rigid**: Thirion, J.P. (1998). "Image Matching as a Diffusion Process: An Analogy with Maxwell's Demons." Medical Image Analysis, 2(3), 243-260.

