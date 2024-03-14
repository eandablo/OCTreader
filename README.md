# Dataset Content

The database containes a total of 84495 Optical coherence tomography (OCT) retinal images organised in three folders: train, val and test. In each folder, images are split in four different sets pertaining to three different abnormal conditions, namely, CNV, DME, DRUNSEN, and healthy maculas (NORMAL).

# Bussiness Requirements

A health care provider offers its patients OCT scans for early detection of dibeties and age related macular conditions. The analysis of scans is high time consuming and requires highly specialised medical staff. The client is finding difficult to meet current deadlines to deliver results to patients.

- The client requires to understand visual differences between the different macular conditions and healthy maculas.
- The client requires an effective tool to determine the medical condition of a macula based on a OCT scan. The client needs to distinguish amongst CNV, DME, DRUNSEN, and healthy maculas.

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

* We want to build a ML model to analyse OCT images and predict one of the following macular conditions: Normal, CNV, DME or DRUNSEN. The supervised model is a multiclass classification model.

* The ideal outcome is to provide the means to interpret OCT macular images with high reliability.

* The model is expected to have an accuracy above 70%.

* The model will determine from an OCT image if a macula is healthy (Normal) or suffers from one of three conditions: CNV, DME or DRUNSEN. Technicians will obtain the OCT images in a regular procedure and they will not require any additional pre-processing to be fed to the model. The automated analysis (prediction) can be performed immediately after obtaining the image.

* Normally, macular condition is detected by highly trained medical professionals carefully inspecting the OCT images. On a patient consultation, the image is ontained in a non-invasive procedure using a Optical Coherence Tomography (OCT) Equipment by a trainned technician. The current optical procedure in combination with high demand for analysis is known to produce considerable errors. This model should serve to reduce misinterpretation of the images and more reliable advice to patients.

* The training data is accessible in [Kaggle dataset directory](https://www.kaggle.com/datasets/paultimothymooney/kermany2018/data) with non-commercial license [CC BY-NC-SA 4.0 DEED](https://creativecommons.org/licenses/by-nc-sa/4.0/). In agreement to kaggle the dataset is a product of a multi-institutional effort and involved cohorts of adult patients wich OCT retina scans were taken between July 1, 2013 and March 1, 2017 in one of the following institutions: the Shiley Eye Institute of the University of California San Diego, the California Retinal Research Foundation, Medical Center Ophthalmology Associates, the Shanghai First People’s Hospital, and Beijing Tongren Eye Center.
