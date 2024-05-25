import matplotlib.pyplot as plt
from utils import *

# model = "stylegan3.pkl"
model = "generated.photos.pkl"
extractor = "arcface"
# extractor = "adaface"
dataset = "lfw"
quantile = 0.05

# getting feature vectors
X, df = get_features(extractor, model, 'unconditional')
dim = X.shape[1]

capacity_full, cos_delta = do_capacity_ops(X, df, extractor, dataset, quantile, "unconditional")

print(capacity_full)

plt.plot(cos_delta, capacity_full, "-o")
plt.yscale('log')
plt.xlabel("cos delta")
plt.ylabel("Capacity")
plt.title(extractor+" "+model)
plt.show()

male_capacity, female_capacity = get_gender_capacity(X, df, extractor, dataset, quantile)

print(male_capacity)
print(female_capacity)

plt.plot(cos_delta, male_capacity, "-o")
plt.plot(cos_delta, female_capacity, "-o")
plt.yscale('log')
plt.xlabel("cos delta")
plt.ylabel("Capacity")
plt.title(extractor+" "+model)
plt.legend(['male', 'female'])
plt.show()

age_capacities = get_age_capacity(X, df, extractor, dataset, quantile, model_type="unconditional")

for age_capacity in age_capacities:
    plt.plot(cos_delta, age_capacity, "-o")

plt.yscale('log')
plt.xlabel("cos delta")
plt.ylabel("Capacity")
plt.title(extractor+" "+model)
plt.legend([f"{x}-{x+10}" for x in range(0, 60, 10)])
plt.show()



