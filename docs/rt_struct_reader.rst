RT Struct Reader
----------------

.. image:: images/7.rt_struct_reader.png
   :alt: RT Struct Reader
   :width: 100%

Specialized tool for importing radiotherapy structure sets, supporting the standardized DICOM-RT format used in radiation oncology.

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
