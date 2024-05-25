import numpy as np

from preprocess import *
from math_functions import *


def do_capacity_ops(X, df, extractor, dataset, quantile=0.05, model_type="unconditional"):
    dim = X.shape[1]

    # getting inter class angle in radians
    inter_class = get_inter_class(X, quantile)
    print(f"Inter class angle: {inter_class}")

    # getting intra class angle in radians
    intra_class = None
    if model_type == "unconditional":
        intra_class = get_intra_class_unconditional(extractor, dataset)
    elif model_type == "conditional":
        intra_class = get_intra_class_conditional(X, df)
    print(f"Intra class angle: {intra_class}")

    # getting thresholds
    thresholds = get_thresholds(extractor, dataset)

    # extrapolating cos delta values for graph
    cos_delta = np.arange(min(thresholds) - 0.01, max(thresholds) + 0.02, 0.01)

    # getting capacity values
    capacity = get_capacity(inter_class, intra_class, cos_delta, dim)

    return capacity, cos_delta


def get_gender_capacity(X, df, extractor, dataset, quantile, model_type="unconditional"):
    male_index = np.where(df['gender'] == 0.0)[0]
    female_index = np.where(df['gender'] == 1.0)[0]

    X_male = X[male_index]
    X_female = X[female_index]

    df_male = df.iloc[male_index]
    df_male = df_male.reset_index(drop=True)
    df_female = df.iloc[female_index]
    df_female = df_female.reset_index(drop=True)

    male_capacity, _ = do_capacity_ops(X_male, df_male, extractor, dataset, quantile, model_type)
    female_capacity, _ = do_capacity_ops(X_female, df_female, extractor, dataset, quantile, model_type)

    return male_capacity, female_capacity


def get_age_capacity(X, df, extractor, dataset, quantile, model_type="unconditional"):
    age_capacities = []
    for i in range(0, 6):
        lb = i * 10
        rb = lb + 10
        age_index1 = np.where(lb <= df['age'])[0]
        age_index2 = np.where(rb > df['age'])[0]
        age_index = np.intersect1d(age_index1, age_index2)

        X_age = X[age_index]
        df_age = df.iloc[age_index]
        df_age = df_age.reset_index(drop=True)

        age_capacity, _ = do_capacity_ops(X_age, df_age, extractor, dataset, quantile, model_type)
        age_capacities.append(age_capacity)

    return age_capacities



