# Dataset Content

The database containes a total of 84495 Optical coherence tomography (OCT) retinal images organised in three folders: train, val and test. In each folder, images are split in four different sets pertaining to three different abnormal conditions, namely, CNV (Choroidal Neovascularization), DME (Diabetic macular edema), DRUNSEN, and healthy maculas (NORMAL).

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

# Dashboard Design

Page 1: Brief Project Summary

* Introduction

    - The macula is a small area that sits around the central area of the retina at the back of the eye. The macula plays an important  Due to different factors being responsible to process frontal vision. Some factors such as age and chronic diseases can be detrimental to the structural integrity of the macula decreasing a person vision quality. This project concerns with three well known conditions:

        * **Drunsen:** Age related celular degeneration of the macula causing yellow deposits in the retina. In the more serious cases Drunsen can cause loss of peripherial vision. Prevalence of Drunsen in a world population is estimated between 0.3 to 2.5% [1].

        * **CNV:**  It is detected by the abnormal growth of vessels from the choroidal vasculature to the neurosensory retina through the Bruch's membrane[3]. CNV can lead to age related macular degeneration which is linked to 8.7 % of all legal blindness worldwide[4].

        * **DME:** Causes thickening of the retinal tissue due to fluid accumulation and it is associated with diabetic retinopathy. Just in the USA estimates the WHO estimates 15 million undiagnosed cases of DME[5], with 25-30% risk of vision loss. 
    
    - All mention conditions cuase structural changes on the macular tissue. Thus, their detection is based on imaging techniques, most common is OCT. Normally, a qualified medical practisioner will inspect the images carefully to diagnose a condition.


* Dataset

    - The database containes a total of 84495 Optical coherence tomography (OCT) retinal images organised in three folders: train, val and test. In each folder, images are split in four different sets pertaining to three different abnormal conditions, namely, CNV (Choroidal Neovascularization), DME (Diabetic macular edema), DRUNSEN, and healthy maculas (NORMAL). The training data is accessible in [Kaggle dataset directory](https://www.kaggle.com/datasets/paultimothymooney/kermany2018/data) with non-commercial license [CC BY-NC-SA 4.0 DEED](https://creativecommons.org/licenses/by-nc-sa/4.0/). In agreement to kaggle the dataset is a product of a multi-institutional effort and involved cohorts of adult patients wich OCT retina scans were taken between July 1, 2013 and March 1, 2017 in one of the following institutions: the Shiley Eye Institute of the University of California San Diego, the California Retinal Research Foundation, Medical Center Ophthalmology Associates, the Shanghai First People’s Hospital, and Beijing Tongren Eye Center.


# References

1. Auw-Haedrich C, Staubach F, Witschel H. Optic disk drusen. Surv Ophthalmol. 2002;47:515–32.

2. Turbert, D. (2020, March 18). What are Choroidal Neovascular membranes? Reviewed by Ninel Z Gregori, MD. American Academy of Ophthalmology. https://www.aao.org/eye-health/diseases/choroidal-neovascular-membranes.

3. Congdon N, O’Colmain B, Klaver CCW, et al. Causes and prevalence of visual impairment among adults in the United States. Arch Ophthalmol. 2004;122:477–85.

4. Albert and Jakobiec’s Principles and Practice of Ophthalmology. Third edition, second volume. Canada: SAUNDERS ELSEVIER; 2008. pp. 1793–1996. 