Table Reader
------------

.. image:: images/8.table_reader.png 
   :alt: Table Reader
   :width: 100%

The **Table Reader** module provides a flexible data import interface within Radiuma for loading and integrating tabular data from various sources and formats. This essential tool enables researchers and clinicians to efficiently import structured data including CSV files, Excel spreadsheets, and analysis exports while offering powerful data integration capabilities through row concatenation for vertical table merging and column merging for horizontal data combination. With automatic format detection and intuitive parameter configuration, the module streamlines the process of creating comprehensive datasets from multiple sources, making it ideal for combining feature tables, clinical data, and analysis results into unified formats ready for machine learning, statistical analysis, and research applications across diverse medical and scientific workflows.

.. image:: images/8.table_reader_column.png
   :alt: Table Reader Column
   :width: 100%

The column merge capability enables combining tables horizontally by joining columns from different tables. This feature is essential when working with related data sets that need to be analyzed together, allowing users to create comprehensive views of their data.

Reader Parameters
^^^^^^^^^^^^^^^^^

* **File Path**: Location of the input data file
* **Format Detection**: Automatic detection of file format

Supported Formats
^^^^^^^^^^^^^^^^^

* CSV files
* Excel spreadsheets
* Structured data exports from analysis tools
