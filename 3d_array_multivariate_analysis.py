import numpy as np
from scipy.stats import multivariate_normal
import matplotlib.pyplot as plt
from scipy.signal import correlate
from scipy import signal
from scipy.signal import welch
from statsmodels.multivariate.manova import MANOVA
import pandas as pd
from mpl_toolkits.mplot3d import Axes3D


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
    'Trace2_Result1': np.random.rand(10),
    'Trace2_Result2': np.random.rand(10),
    'Trace2_Result3': np.random.rand(10),
    'Trace1_PassFail': np.random.choice(['Pass', 'Fail'], 10),
    'Trace2_PassFail': np.random.choice(['Pass', 'Fail'], 10)
}

# Create a DataFrame from the data
df = pd.DataFrame(data)

# Modify the dataset so that each trace result has a pass/fail result
for i in range(1, 4):
    df[f'Trace1_Result{i}_PassFail'] = np.random.choice(['Pass', 'Fail'], 10)
    df[f'Trace2_Result{i}_PassFail'] = np.random.choice(['Pass', 'Fail'], 10)


# Create a 3D matplotlib plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot each trace result as a point in 3D space
for i in range(1, 4):
    trace1_pass = df[df[f'Trace1_Result{i}_PassFail'] == 'Pass']
    trace1_fail = df[df[f'Trace1_Result{i}_PassFail'] == 'Fail']
    trace2_pass = df[df[f'Trace2_Result{i}_PassFail'] == 'Pass']
    trace2_fail = df[df[f'Trace2_Result{i}_PassFail'] == 'Fail']

    ax.scatter(trace1_pass[f'Trace1_Result{i}'], trace1_pass[f'Trace2_Result{i}'], np.repeat(i, len(trace1_pass)), c='green', label='Trace 1 Pass')
    ax.scatter(trace1_fail[f'Trace1_Result{i}'], trace1_fail[f'Trace2_Result{i}'], np.repeat(i, len(trace1_fail)), c='red', label='Trace 1 Fail')
    ax.scatter(trace2_pass[f'Trace2_Result{i}'], trace2_pass[f'Trace2_Result{i}'], np.repeat(i, len(trace2_pass)), c='blue', label='Trace 2 Pass')
    ax.scatter(trace2_fail[f'Trace2_Result{i}'], trace2_fail[f'Trace2_Result{i}'], np.repeat(i, len(trace2_fail)), c='yellow', label='Trace 2 Fail')
    
    # Add lines connecting the points
    for j in range(len(trace1_pass) - 1):
        ax.plot([trace1_pass.iloc[j][f'Trace1_Result{i}'], trace1_pass.iloc[j + 1][f'Trace1_Result{i}']],
                [trace1_pass.iloc[j][f'Trace2_Result{i}'], trace1_pass.iloc[j + 1][f'Trace2_Result{i}']],
                [i, i], c='green')
    for j in range(len(trace1_fail) - 1):
        ax.plot([trace1_fail.iloc[j][f'Trace1_Result{i}'], trace1_fail.iloc[j + 1][f'Trace1_Result{i}']],
                [trace1_fail.iloc[j][f'Trace2_Result{i}'], trace1_fail.iloc[j + 1][f'Trace2_Result{i}']],
                [i, i], c='red')
    for j in range(len(trace2_pass) - 1):
        ax.plot([trace2_pass.iloc[j][f'Trace2_Result{i}'], trace2_pass.iloc[j + 1][f'Trace2_Result{i}']],
                [trace2_pass.iloc[j][f'Trace2_Result{i}'], trace2_pass.iloc[j + 1][f'Trace2_Result{i}']],
                [i, i], c='blue')
    for j in range(len(trace2_fail) - 1):
        ax.plot([trace2_fail.iloc[j][f'Trace2_Result{i}'], trace2_fail.iloc[j + 1][f'Trace2_Result{i}']],
                [trace2_fail.iloc[j][f'Trace2_Result{i}'], trace2_fail.iloc[j + 1][f'Trace2_Result{i}']],
                [i, i], c='yellow')

# Set labels and title
ax.set_xlabel('Trace 1')
ax.set_ylabel('Trace 2')
ax.set_zlabel('Trace Result')
ax.set_title('3D Scatter Plot with Lines Connecting Traces')

# Show plot
plt.show()
# Perform MANOVA
columns = ['Trace1_Result1', 'Trace1_Result2', 'Trace1_Result3', 'Trace2_Result1', 'Trace2_Result2', 'Trace2_Result3']
groups = ['Trace1_PassFail', 'Trace2_PassFail']
manova = MANOVA.from_formula(f"{'+'.join(columns)} ~ {'+'.join(groups)}", data=df)
print(manova.mv_test())