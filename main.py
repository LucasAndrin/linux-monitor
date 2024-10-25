import streamlit as st
import pandas as pd
import numpy as np
import time
import os

def get_process_count():
    return int(os.popen('ps aux | wc -l').read().strip())

data = []
chart = st.empty()

while True:
    data.append({
        'Time': time.strftime("%H:%M:%S"),
        'Processes': get_process_count()
    })

    data_frame = pd.DataFrame(data)

    chart.line_chart(data_frame, x="Time", y="Processes")

    time.sleep(1)