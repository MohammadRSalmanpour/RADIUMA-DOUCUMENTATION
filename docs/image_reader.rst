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


**How to Import Data**
--------------------

Radiuma supports importing medical images from multiple sources and modalities. Follow the steps below for proper import:

1. **Selecting the Source Type**:  
   - Choose **Folder** to import a directory containing DICOM images for multiple patients or to import NIFTI files from folders.
   - Choose **Single File** if you're importing a specific image file (e.g., a single DICOM, NIFTI, or NRRD file).

2. **Importing Multi-DICOM Images for Multiple Patients**:  
   If you have a **main folder** containing multiple subfolders for each patient, Radiuma will process the images within each patient folder.  
   - Example structure:
     ```plaintext
     /CT
        /patient_01
           patient_01_ct_001.dcm
           patient_01_ct_002.dcm
        /patient_02
           patient_02_ct_001.dcm
           patient_02_ct_002.dcm
     ```
   - **Important**: Radiuma only supports DICOM images within **subfolders** of each modality (e.g., **CT**, **MRI**, etc.). If you have a main folder like `/CT`, you must structure it with **subfolders** for each patient. Radiuma will not work if all images are in the same folder; they must be placed into **patient-specific subfolders**.

3. **Importing NIFTI (.nii, .nii.gz) Files**:  
   For formats like **NIFTI**, Radiuma requires that images be organized into **modality-specific folders**.  
   - **Correct Folder Structure**:
     - `/CT/` for CT images.
     - `/MRI/T1/` for T1 MRI images.
     - `/MRI/T2/` for T2 MRI images.
     - `/MRI/DCE/` for DCE MRI images.
     
     Example structure:
     ```plaintext
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
     ```
   - Radiuma **does not** support importing NIFTI files if they are located in a general folder (e.g., `/MRI/`) without the subfolder organization (e.g., `/MRI/T1/`, `/MRI/T2/`).

4. **Handling Mixed Modalities in a Single Folder**:  
   Radiuma **requires that each modality (e.g., CT, MRI)** has its own **subfolder structure** for each patient. Images should be placed in these **subfolders** based on the type of modality or sequence.
   - **Example for MRI**:
     ```plaintext
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
     ```
     In this case, Radiuma will correctly identify and process NIFTI images from the **T1**, **T2**, or **DCE** subfolders.

**Supported Input Formats**
^^^^^^^^^^^^^^^^^^^^^^^

Radiuma supports importing a variety of medical image formats, including:

* **DICOM Files and Directories**: Radiuma supports importing individual `.dcm` files or entire directories of DICOM files. Directories should be organized by patient subfolders (e.g., `/CT/patient_01/`).
  
* **NIFTI Files (.nii, .nii.gz and not directories)**: Radiuma can import individual NIFTI files with extensions `.nii` or `.nii.gz`, but it does not support importing NIFTI files from directories. Files must be placed in modality-specific subfolders, such as `/MRI/T1/` for T1 images.

* **NRRD Files (.nrrd)**: Radiuma supports importing `.nrrd` files, which are used for storing medical image data.

* **Various other medical image formats**: Radiuma can also handle other common medical image formats that may not be explicitly listed here.

**Example Directory Structure**:
```plaintext
/data
    /CT
        /patient_01
            patient_01_ct_001.dcm
            patient_01_ct_002.dcm
        /patient_02
            patient_02_ct_001.dcm
            patient_02_ct_002.dcm
    /MRI
        /T1
            patient_01_t1_001.nii
            patient_01_t1_002.nii
        /T2
            patient_01_t2_001.nii
            patient_01_t2_002.nii






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
