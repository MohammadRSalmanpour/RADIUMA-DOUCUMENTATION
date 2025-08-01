RT Struct Reader
----------------

.. image:: images/7.rt_struct_reader.png 
   :alt: RT Struct Reader
   :width: 100%

Specialized tool for importing radiotherapy structure sets, supporting the standardized DICOM-RT format used in radiation oncology.


Important Notes
^^^^^^^^^^^^^^^^

To ensure proper pairing between RTSTRUCT and image data:

* If the RTSTRUCT is a **single DICOM file**, its **filename** must exactly match the **name of the corresponding image folder**.

.. image:: images/7.rt_struct_reader_data.png 
   :alt: RT Struct Reader
   :width: 100%
   
The name of RTSTRUCT single dicom file  must exactly match the name of the corresponding image folder.


.. image:: images/7.rt_struct_reader_rt.png 
   :alt: RT Struct Reader
   :width: 100%

* Both RTSTRUCT and main image directories must follow a **single-level nested folder structure**, where each case is stored in its own folder or file (depending on the format).

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

.. image:: images/7.rt_struct_reader_workflow.png 
   :alt: RT Struct Reader
   :width: 100%

* Outputs to Radiomic Feature Generator
* Outputs to Image Writer
* Outputs to Image Viewer
