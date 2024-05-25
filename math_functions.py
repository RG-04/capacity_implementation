import math
import numpy as np
from thresholds import *
import scipy.special as sp


def get_inter_class(X, quantile):
    similarity_scores = np.dot(X, X.transpose())
    min_cos_with_outliers = np.min(similarity_scores, axis=1)
    min_cos = np.quantile(min_cos_with_outliers, quantile)
    angle_radians = np.arccos(min_cos) / 2

    return angle_radians


def get_intra_class_unconditional(extractor, dataset):
    thresholds = get_thresholds(extractor, dataset)
    intra_class = math.acos(thresholds[0])

    return intra_class


def get_thresholds(extractor, dataset):
    new_thresholds = []
    for val in THRESHOLDS[extractor][dataset]:
        new_thresholds.append(math.cos(math.acos(1 - val / 2) / 2))

    return new_thresholds


def get_capacity(inter_class, intra_class, cos_delta, n, testing=0):
    a = (n-1)/2.0
    b = 0.5

    sin_delta = np.sqrt(1 - cos_delta**2)

    cos_theta = np.cos(inter_class)
    sin_theta = np.sqrt(1-cos_theta**2)

    cos_phi = np.cos(intra_class)
    sin_phi = np.sqrt(1-cos_phi**2)

    cos_omega1 = cos_theta*cos_delta - sin_theta*sin_delta
    cos_omega2 = cos_phi*cos_delta - sin_phi*sin_delta

    x1 = 1 - cos_omega1**2
    x2 = 1 - cos_omega2**2

    idx1 = np.where(cos_omega1 < 0)
    x1[idx1] = cos_omega1[idx1] ** 2  # sin^2(90-omega) where omega exceeds 90 degrees

    idx2 = np.where(cos_omega2 < 0)
    x2[idx2] = cos_omega2[idx2] ** 2  # sin^2(90-omega) where omega exceeds 90 degrees

    num = sp.betainc(a, b, x1)
    den = sp.betainc(a, b, x2)

    # range of beta is [0,1], so add surface area of hyper-hemisphere to places where omega > pi/2
    num[idx1] = num[idx1] + 1
    den[idx2] = den[idx2] + 1

    # print(num, cos_omega1)

    capacity = num / den

    return capacity


def get_intra_class_conditional(X, df):
    ids = df["ids"]
    ids = ids.drop_duplicates()
    min_cos_unique = []

    for i in ids:
        index = df.index[df['ids'] == i].tolist()
        feature_vectors = X[index]
        similarity_scores = np.dot(feature_vectors, feature_vectors.transpose())
        min_cos = np.min(similarity_scores, axis=1)
        min_cos_unique.append(np.min(min_cos))

    min_cos_unique = np.array(min_cos_unique)
    median_cos = np.median(min_cos_unique)
    intra_class = np.arccos(median_cos)/2
    return intra_class

