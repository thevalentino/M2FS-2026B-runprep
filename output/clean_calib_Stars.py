import pandas as pd

calib = pd.read_csv("J2259_CFG05_calib_stars.csv", sep="\t")
# calib = pd.read_csv("J0140_CFG07_calib_stars.csv", sep="\t")
# calib = pd.read_csv("J0140_CFG08_calib_stars.csv", sep="\t")
calib["Epoch"] = "J2000"
calib["Type"] = "T"
calib["Priority"] = 9

calib["pmRA"] = calib["pmRA"] * 0.001
calib["pmDE"] = calib["pmDE"] * 0.001

print(
    calib[
        [
            "_RAJ2000",
            "_DEJ2000",
            "Epoch",
            "Source",
            "Type",
            "Priority",
            "pmRA",
            "pmDE",
            "Gmag",
        ]
    ]
)

(
    (
        calib[
            [
                "_RAJ2000",
                "_DEJ2000",
                "Epoch",
                "Source",
                "Type",
                "Priority",
                "pmRA",
                "pmDE",
                "Gmag",
            ]
        ]
    )
    .round({"pmRA": 6, "pmDE": 6, "Gmag": 2})
    .to_csv("J2259_CFG05_calibs_clean.csv", index=False)
)
