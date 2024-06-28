try:
    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt
    import seaborn as sns
    import jupyterlab
    print("libraries are imported")
except ImportError as e:
    print(f"an error occurred: {e}")


# testing pandas
df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
print(df.describe())

# testing NumPy
array = np.array([1, 2, 3])
print(array * 2)

# testing Matplotlib with Seaborn
plt.figure(figsize=(6, 4))
sns.lineplot(x=[1, 2, 3], y=[1, 4, 9])
plt.title("test Plot")
plt.show()
