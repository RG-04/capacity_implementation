import matplotlib.pyplot as plt
from utils import *

model = "dcface_0.5m.pkl"
extractor = "arcface"
dataset = "lfw"
quantile = 0.05

# getting feature vectors
X, df = get_features(extractor, model, 'conditional')
dim = X.shape[1]

# getting capacity values
capacity_full, cos_delta = do_capacity_ops(X, df, extractor, dataset, quantile, "conditional")

plt.plot(cos_delta, capacity_full, "-o")
plt.yscale('log')
plt.xlabel("cos delta")
plt.ylabel("Capacity")
plt.show()