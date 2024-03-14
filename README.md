# Dataset Content

The database containes a total of 84495 images organised in three folders: train, val and test. In each folder, images are split in four different sets pertaining to three different abnormal conditions, namely, CNV, DME, DRUNSEN, and healthy maculas (NORMAL).

# Bussiness Requirements

A health care provider offers its patients OCT scans for early detection of dibeties and age related macular conditions. The analysis of scans is high time consuming and requires highly specialised medical staff. The client is finding difficult to meet current deadlines to deliver results to patients.

The client requires to understand visual differences between the different macular conditions and healthy maculas.
The client requires an effective tool to determine the medical condition of a macula based on a OCT scan. The client needs to distinguish amongst CNV, DME, DRUNSEN, and healthy maculas.

# Hypothesis and Validation

Specialists dedicated to OCT analysis are capable to distinguish certain anomalities in non-healthy macula images when compare to healthy ones. Based on this, It is plaussible to assume that patterns might emerge in OCT images that allow for automatic detection of macular anomalities using the appropriate techniques.

# Mapping Bussiness Requirements to Data Visualisation and ML Tasks

* **Business Requirement 1**: Data Visualisation

    - Display mean and standard deviation of images for maculas conditions: Normal, CNV, DME, DRUNSEN

    - Display difference between combination pairs of different macular conditions.

    - Display a montage with sample images for all conditions

* **Business Requirement 2**: Classification

    - Build a multiclass classifier to predict macular condition (Normal, CNV, DME or DRUNSEN) from an OCT image.

# ML Business Case