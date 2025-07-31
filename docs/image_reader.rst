Image Reader
------------

.. image:: images/6.image_reader.png
   :alt: Image Reader
   :width: 100%

A flexible tool for importing various medical image formats into the Radiuma workflow.

Key Parameters
^^^^^^^^^^^^^^

* **Source Type**: Choose between folder or single file import
* **Path**: Location of the medical image file(s) to import


Image Reader
============

.. image:: images/6.image_reader.png
   :alt: Image Reader
   :width: 100%

A flexible tool for importing various medical image formats into the Radiuma workflow.

Key Parameters
^^^^^^^^^^^^^^

* **Source Type**: Choose between folder or single file import
* **Path**: Location of the medical image file(s) to import

How to Import Data
------------------

Radiuma supports importing images from multiple sources and modalities, allowing users to efficiently bring in medical data for further processing. Here's how to import your data, whether you have **DICOM images**, **NIFTI files**, or other formats.

1. Selecting the Source Type
~~~~~~~~~~~~~~~~~~~~~~~~~~~
You can import your images either from a **folder** containing multiple files or a **single file**:

* **Folder Import**: Choose **Folder** if your data is organized in directories, such as when images are grouped by patient or modality (e.g., CT, MRI). You will select the main directory, and Radiuma will automatically detect and import all the relevant files from its subfolders.
* **Single File Import**: Choose **Single File** if you're importing one image, like a specific ``.nii``, ``.dcm``, or ``.nrrd`` file.

2. Importing Multi-DICOM Images for Multiple Patients
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Radiuma allows you to import **DICOM files** organized by **patient-specific subfolders**. If you have images for multiple patients with various modalities, you can organize DICOM files into separate subfolders for each patient and modality.

**Example Folder Structure for DICOM images**:

::

    /CT
        /patient_01
            patient_01_ct_001.dcm
            patient_01_ct_002.dcm
        /patient_02
            patient_02_ct_001.dcm
            patient_02_ct_002.dcm

In this example, Radiuma will process the DICOM files inside each patient's subfolder (e.g., ``/patient_01/`` and ``/patient_02/``). When importing, simply select the main directory (e.g., ``/CT``), and Radiuma will automatically organize and import the files.

**Important Notes**:

* Radiuma only supports DICOM images inside subfolders. Each patient should have their own folder (e.g., ``/patient_01/``) containing their corresponding DICOM files.
* Subfolder Structure: The DICOM files must be organized into subfolders (one subfolder per patient). Radiuma will not process files in a flat directory structure.

3. Importing NIFTI (.nii, .nii.gz) Files
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
NIFTI files are commonly used in medical imaging, especially in MRI data. Radiuma supports NIFTI files with extensions ``.nii`` and ``.nii.gz``. However, NIFTI files must be organized into modality and sequence-specific subfolders for Radiuma to process them properly.

**Correct Folder Structure for NIFTI Files**:

* ``/CT/`` for CT images.
* ``/MRI/T1/`` for T1-weighted MRI images.
* ``/MRI/T2/`` for T2-weighted MRI images.
* ``/MRI/DCE/`` for DCE (Dynamic Contrast Enhanced) MRI images.

**Example Folder Structure for NIFTI Files**:

::

    /CT
        /patient_01
            patient_01_ct_001.nii
            patient_01_ct_002.nii

    /MRI
        /T1
            patient_01_t1_001.nii
            patient_01_t1_002.nii
        /T2
            patient_01_t2_001.nii
            patient_01_t2_002.nii
        /DCE
            patient_01_dce_001.nii
            patient_01_dce_002.nii

**Important Notes**:

* Radiuma does not support importing NIFTI files from a single directory. Files must be organized into modality-based subfolders (e.g., ``/MRI/T1/``, ``/MRI/T2/``) for successful import.
* Subfolder Structure for NIFTI Files: Ensure that your NIFTI files are grouped in separate folders by modality (e.g., ``/MRI/T1/``, ``/MRI/T2/``) before importing them.

4. Handling Mixed Modalities in a Single Folder
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Radiuma requires that each modality (e.g., CT, MRI) has its own subfolder structure within the main folder. When importing images, ensure that different imaging modalities (e.g., CT, MRI) are stored in separate folders.

**How to Organize Mixed Modalities (CT, PET, MRI)**:

* CT: Store CT images in a dedicated ``/CT/`` folder.
* PET: Store PET images in a dedicated ``/PET/`` folder.
* MRI: Store MRI images in separate subfolders for each MRI sequence (e.g., ``/MRI/T1/``, ``/MRI/T2/``).

**Example Directory Structure for Mixed Modalities**:

::

    /data
        /CT
            /patient_01
                patient_01_ct_001.dcm
                patient_01_ct_002.dcm
        /PET
            /patient_01
                patient_01_pet_001.nii
                patient_01_pet_002.nii
        /MRI
            /T1
                patient_01_t1_001.nii
                patient_01_t1_002.nii
            /T2
                patient_01_t2_001.nii
                patient_01_t2_002.nii
            /DCE
                patient_01_dce_001.nii
                patient_01_dce_002.nii

**Important Notes**:

* Separate Processing: Radiuma cannot process CT and PET images together. You must process these modalities separately by selecting the corresponding modality folder (``/CT/`` or ``/PET/``).
* Subfolder Structure: Radiuma requires that images from each modality (e.g., CT, PET, MRI) be placed into distinct subfolders for proper processing. The images from the same modality (e.g., CT or MRI) can be placed in separate patient-specific folders (e.g., ``/CT/patient_01/``), but the modalities must not be mixed in the same folder.
* Radiuma will process each modality separately, meaning that CT and MRI images from the same patient will need to be processed in their respective folders (e.g., ``/CT/patient_01/`` and ``/MRI/T1/patient_01/``).

5. Supported Input Formats
~~~~~~~~~~~~~~~~~~~~~~~~~
Radiuma supports a variety of medical image formats, including:

* DICOM Files and Directories: Radiuma supports importing individual ``.dcm`` files or entire directories containing DICOM files. These should be organized into modality-specific subfolders (e.g., ``/CT/patient_01/``).
* NIFTI Files (``.nii``, ``.nii.gz`` and not directories): Radiuma can import individual NIFTI files (``.nii`` and ``.nii.gz``), but they must be organized in modality-based subfolders, such as ``/MRI/T1/`` for T1 images.
* NRRD Files (``.nrrd``): Radiuma supports importing ``.nrrd`` files, which are used for storing medical image data.
* Various Other Medical Image Formats: Radiuma can handle other formats commonly used in research or clinical settings.

**Example Directory Structure**:

::

    /data
        /CT
            /patient_01
                patient_01_ct_001.dcm
                patient_01_ct_002.dcm
            /patient_02
                patient_02_ct_001.dcm
                patient_02_ct_002.dcm
        /PET
            /patient_01
                patient_01_pet_001.nii
                patient_01_pet_002.nii
            /patient_02
                patient_02_pet_001.nii
                patient_02_pet_002.nii
        /MRI
            /T1
                patient_01_t1_001.nii
                patient_01_t1_002.nii
            /T2
                patient_01_t2_001.nii
                patient_01_t2_002.nii

Workflow Integration
^^^^^^^^^^^^^^^^^^^^

* Outputs to Image Convertor
* Outputs to Image Filter
* Outputs to Image Fusion
* Outputs to Image Registration

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
