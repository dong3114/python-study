import pandas as pd
import matplotlib.pyplot as plt

data = {
    'index': ['math', 'english', 'science'],
    'score': [85, 90, 78]
}
df = pd.DataFrame(data)
plt.bar(df['index'], df['score'])
plt.title("idx score")
plt.show()