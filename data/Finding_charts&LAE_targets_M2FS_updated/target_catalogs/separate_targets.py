import pandas as pd
from astropy import units as u
from astropy.coordinates import ICRS, SkyCoord

# targets = pd.read_csv("SDSS_J0022_targets.csv")
# targets = pd.read_csv("SDSS_J2259_targets.csv")
targets = pd.read_csv("SDSS_J0140_targets.csv")
sh_star = SkyCoord(
    # ra=5.2410717956 * u.deg, dec=-0.7170246351 * u.deg, frame=ICRS, obstime="J2026.10"
    #
    # J0022 CFG02
    # ra=5.5886277698 * u.deg,
    # dec=-0.485957954 * u.deg,
    # J2259 GFG04
    # ra=344.5743205643 * u.deg,
    # dec=13.9021129124 * u.deg,
    # J2259 CFG05
    # ra=345.0547871036 * u.deg,
    # dec=13.8353116299 * u.deg,
    # J0140 CFG07
    # ra=25.0843522142 * u.deg,
    # dec=2.945202523 * u.deg,
    # J0140 CFG08
    ra=25.3484249366 * u.deg,
    dec=2.6489896963 * u.deg,
    frame=ICRS,
    obstime="J2026.10",
)
target_coords = SkyCoord(
    ra=targets["RA"].values * u.deg,
    dec=targets["Dec"].values * u.deg,
    frame=ICRS,
    obstime="J2026.10",
)

separations = sh_star.separation(target_coords)
in_plate = separations < 14.65 * u.arcmin

targets_selected = targets[in_plate]
targets_selected["Epoch"] = "J2026.10"
targets_selected["Type"] = "T"
targets_selected["Redshift"] = 2.25

targets_selected[
    [
        "RA",
        "Dec",
        "Epoch",
        "source_id",
        "Type",
        "priority",
        "Redshift",
        "line_flux_erg_cm2_s",
    ]
].to_csv("J0140_CFG08_targets.csv", index=False)
