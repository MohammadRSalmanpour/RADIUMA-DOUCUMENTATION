Visual Node-Based Workflow System
=================================

ViSERA uses a visual programming approach where modules are represented as nodes that can be connected to create complete data processing pipelines. This intuitive interface allows users with minimal programming experience to build sophisticated workflows.

Creating Workflows
------------------

1. **Adding Modules**: Double-click on a module from the module palette to add it to the workspace
2. **Configuring Modules**: Double-click on a module node to open its configuration dialog
3. **Connecting Modules**: Click and drag from an output port to an input port to create connections
4. **Running Workflows**: Click the "Run" button on a node to execute it and all its prerequisite nodes
5. **Stopping Execution**: Click the "Stop" button to halt execution of a running workflow

Module Compatibility
--------------------

Each module explicitly defines which other modules can connect to its inputs and outputs, ensuring that only valid connections can be made:

* **Image Reader**: Outputs to Image Convertor, Filter, Fusion, and Registration modules
* **RT Struct Reader**: Outputs to Radiomic Feature Generator and Image Writer modules
* **Image Filter**: Takes image input, outputs to multiple imaging modules
* **Radiomic Feature Generator**: Takes image and mask inputs, outputs to data analysis modules
* **Preprocessing**: Takes feature data, connects to machine learning modules
* **Classification/Regression/Clustering**: Take preprocessed data as input, connect to visualization

Example Workflows
-----------------

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
-----------------

* **Layout Management**: Automatically arrange nodes with the "Align Modules" function
* **Module Search**: Quickly find modules using the search function (Tab key)
* **Copy/Paste**: Duplicate node configurations to create similar processing steps
* **Save/Load**: Save entire workflows and reload them for future use

Keyboard Shortcuts
------------------

* **Tab**: Open module search
* **Ctrl+C / Cmd+C**: Copy selected nodes
* **Ctrl+V / Cmd+V**: Paste nodes
* **Delete**: Remove selected nodes
* **D**: Lock/Unlock nodes 