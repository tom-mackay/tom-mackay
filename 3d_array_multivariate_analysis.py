import numpy as np
from scipy.stats import multivariate_normal
import matplotlib.pyplot as plt
from scipy.signal import correlate
from scipy import signal
from scipy.signal import welch
from statsmodels.multivariate.manova import MANOVA


# Define the traces
trace1 = {
    'x': np.array([1, 2, 3, 4, 5]),
    'y': np.array([0, 0, 0, 0, 0]),
    'z': np.array([10, 11, 12, 13, 14])
}
trace2 = {
    'x': np.array([1, 2, 3, 4, 5]),
    'y': np.array([1, 1, 1, 1, 1]),
    'z': np.array([10, 11, 12, 13, 14])
}
trace3 = {
    'x': np.array([1, 2, 3, 4, 5]),
    'y': np.array([2, 2, 2, 2, 2]),
    'z': np.array([10, 11, 12, 13, 14])
}

# Convert traces to arrays
trace1_arr = np.column_stack((trace1['x'], trace1['y'], trace1['z']))
trace2_arr = np.column_stack((trace2['x'], trace2['y'], trace2['z']))
trace3_arr = np.column_stack((trace3['x'], trace3['y'], trace3['z']))

# Stack traces into a 3D array
traces_array = np.stack((trace1_arr, trace2_arr, trace3_arr))










# # Calculate cross-correlation between traces
# corr_12 = correlate(trace1_arr, trace2_arr)
# corr_13 = correlate(trace1_arr, trace3_arr)
# corr_23 = correlate(trace2_arr, trace3_arr)

# print("Cross-correlation between trace 1 and trace 2:", corr_12)
# print("Cross-correlation between trace 1 and trace 3:", corr_13)
# print("Cross-correlation between trace 2 and trace 3:", corr_23)







# # Perform spectral analysis on each trace
# frequencies_1, psd_1 = welch(trace1_arr.T, axis=1)
# frequencies_2, psd_2 = welch(trace2_arr.T, axis=1)
# frequencies_3, psd_3 = welch(trace3_arr.T, axis=1)

# print("Spectral analysis for trace 1:", frequencies_1, psd_1)
# print("Spectral analysis for trace 2:", frequencies_2, psd_2)
# print("Spectral analysis for trace 3:", frequencies_3, psd_3)




# Example data (replace with your actual data)
data = {
    'Trace1_Result1': np.random.rand(10),
    'Trace1_Result2': np.random.rand(10),
    'Trace1_Result3': np.random.rand(10),
    'Trace1_PassFail': np.random.choice(['Pass', 'Fail'], 10),
    'Trace2_Result1': np.random.rand(10),
    'Trace2_Result2': np.random.rand(10),
    'Trace2_Result3': np.random.rand(10),
    'Trace2_PassFail': np.random.choice(['Pass', 'Fail'], 10)
}

df = pd.DataFrame(data)

# Perform MANOVA
results_cols = ['Trace1_Result1', 'Trace1_Result2', 'Trace1_Result3']
mv = MANOVA.from_formula(' + '.join(results_cols) + ' ~ Trace1_PassFail', data=df)
print(mv.mv_test())