import os
import pickle
import numpy as np
import pandas as pd


def get_features(extractor, model, model_type):
    feature_file = os.path.join("features", extractor, model)
    print(feature_file)
    data = pickle.load(open(feature_file, 'rb'))
    X = data['feats']
    index = np.where(np.sum(np.abs(X), axis=1) == 0)  # some features had all values as zero, removing those

    X = np.delete(X, index, axis=0)
    X = X[:10000]

    if model_type == "conditional":
        new_keys = ["ids", "age", "gender"]  # throwing away extra data
        new_data = {key: data[key] for key in new_keys}

        for key in new_keys:
            new_data[key] = np.delete(new_data[key], index)

        df = pd.DataFrame(new_data)
        df = df[:10000]
        return X, df

    elif model_type == 'unconditional':
        new_keys = ["age", "gender"]  # throwing away extra data
        new_data = {key: data[key] for key in new_keys}

        for key in new_keys:
            new_data[key] = np.delete(new_data[key], index)

        df = pd.DataFrame(new_data)
        df = df[:10000]
        return X, df
