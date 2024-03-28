import numpy as np
import pandas as pd
import os
import base64
from datetime import datetime
import joblib


def download_dataframe_as_csv(df):

    datetime_now = datetime.now().strftime("%d%b%Y_%Hh%Mmin%Ss")
    csv = df.to_csv().encode()
    b64 = base64.b64encode(csv).decode()
    href = (
        f'<a href="data:file/csv;base64,{b64}" download="Report {datetime_now}.csv" '
        f'target="_blank">Download Report</a>'
    )
    return href


def write_classification_report(report_dict):
    labels = list(report_dict.keys())
    column_values = ['precision', 'recall', 'support', 'f1-score']
    labels = labels[:4]
    df = pd.DataFrame(columns=column_values)
    for label in labels:
        temp_dict = report_dict[label]
        df2 = pd.DataFrame(data=temp_dict, index=[label])
        df = df.append(df2.round(2))
    return df