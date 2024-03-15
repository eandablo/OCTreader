import streamlit as st
import matplotlib.pyplot as plt

def page_introduction_body():

    st.write('## Project Introduction and Summary')

    st.info(
        f'**General Information**\n'
        f'The macula is a small area that sits around the central area of the retina at the back of the eye. The macula'
        f'plays an important Due to different factors being responsible to process frontal vision. Some factors such as'
        f'age and chronic diseases can be detrimental to the structural integrity of the macula decreasing a person'
        f'vision quality. This project concerns with three well known conditions:\n'
        f'**Drunsen:** Age related celular degeneration of the macula causing yellow deposits in the retina. In the'
        f'more serious cases Drunsen can cause loss of peripherial vision. Prevalence of Drunsen in a world'
        f'population is estimated between 0.3 to 2.5%.\n'
        f'**CNV:** It is detected by the abnormal growth of vessels from the choroidal vasculature to the neurosensory'
        f"retina through the Bruch's membrane. CNV can lead to age related macular degeneration which is"
        f'linked to 8.7 % of all legal blindness worldwide.\n'
        f'**DME:** Causes thickening of the retinal tissue due to fluid accumulation and it is associated with diabetic'
        f'retinopathy. Just in the USA estimates the WHO estimates 15 million undiagnosed cases of DME, with'
        f'25-30% risk of vision loss.\n'
        f'All mention conditions cuase structural changes on the macular tissue. Thus, their detection is based on'
        f'imaging techniques, most common is OCT. Normally, a qualified medical practisioner will inspect the images'
        f'carefully to diagnose a condition.\n'
        f'**Project Dataset**\n'
        f'The database containes a total of 84495 Optical coherence tomography (OCT) retinal images organised in'
        f'three folders: train, val and test. In each folder, images are split in four different sets pertaining to three'
        f'different abnormal conditions, namely, CNV (Choroidal Neovascularization), DME (Diabetic macular edema),'
        f'DRUNSEN, and healthy maculas (NORMAL). The training data is accessible in Kaggle dataset directory with'
        f'non-commercial license CC BY-NC-SA 4.0 DEED. In agreement to kaggle the dataset is a product of a multi-institutional'
        f'effort and involved cohorts of adult patients wich OCT retina scans were taken between July 1,'
        f'2013 and March 1, 2017 in one of the following institutions: the Shiley Eye Institute of the University of'
        f'California San Diego, the California Retinal Research Foundation, Medical Center Ophthalmology Associates,'
        f'the Shanghai First People’s Hospital, and Beijing Tongren Eye Center.\n'
    )
    st.write(
        f'Additional info can be found in the [project readme file](https://github.com/eandablo/OCTreader/blob/main/README.md)'
    )
    st.sucess(
        f'**Project Requirements:\n**'
        f'1. The client requires to understand visual differences between the different macular conditions and healthy maculas.'
        f'2. The client requires an effective tool to determine the medical condition of a macula based on a OCT scan. The'
        f'   client needs to distinguish amongst CNV, DME, DRUNSEN, and healthy maculas.'
    )