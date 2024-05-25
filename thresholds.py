# Pre calculated threshold values for different FARs
THRESHOLDS = {"arcface": {}, "adaface": {}}

THRESHOLDS["arcface"]["lfw"] = [1.575, 1.713, 1.844]
THRESHOLDS["arcface"]["cfp_fp"] = [1.605, 1.696, 1.825]
THRESHOLDS["arcface"]["cplfw"] = [1.525, 1.691, 1.829]
THRESHOLDS["arcface"]["agedb_30"] = [1.530, 1.627, 1.798]
THRESHOLDS["arcface"]["calfw"] = [1.530, 1.662, 1.816]

THRESHOLDS["adaface"]["lfw"] = [1.610, 1.710, 1.847]
THRESHOLDS["adaface"]["cfp_fp"] = [1.641, 1.726, 1.849]
THRESHOLDS["adaface"]["cplfw"] = [1.550, 1.670, 1.832]
THRESHOLDS["adaface"]["agedb_30"] = [1.550, 1.663, 1.818]
THRESHOLDS["adaface"]["calfw"] = [1.530, 1.666, 1.823]