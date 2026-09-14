import astropy.units as u
import matplotlib.pyplot as plt
import numpy as np
from astropy.coordinates import SkyCoord
from astropy.table import Table
from astropy.time import Time

data = {
    "J0022_CFG01": {
        "sh_ra": 5.2410717956,
        "sh_dec": -0.7170246351,
        "file": "J0022_CFG01_calibs.tsv",
    },
    "J0022_CFG02": {
        "sh_ra": 5.5886277698,
        "sh_dec": -0.485957954,
        "file": "J0022_CFG02_calibs.tsv",
    },
    "J0140_CFG07": {
        "sh_ra": 25.0843522142,
        "sh_dec": 2.945202523,
        "file": "J0140_CFG07_calibs.tsv",
    },
    "J0140_CFG08": {
        "sh_ra": 25.3484249366,
        "sh_dec": 2.6489896963,
        "file": "J0140_CFG08_calibs.tsv",
    },
    "J2259_CFG04": {
        "sh_ra": 344.5743205643,
        "sh_dec": 13.9021129124,
        "file": "J2259_CFG04_calibs.tsv",
    },
    "J2259_CFG05": {
        "sh_ra": 345.0547871036,
        "sh_dec": 13.8353116299,
        "file": "J2259_CFG05_calibs.tsv",
    },
}


rad = (14.5 * u.arcmin).to("deg")

# source_data = data["J0022_CFG01"]
for key in data:
    source_data = data[key]

    circle = plt.Circle(
        (source_data["sh_ra"], source_data["sh_dec"]),
        radius=rad.value,
        edgecolor="blue",
        facecolor="lightblue",
        linewidth=2,
    )
    catalog = Table.read(source_data["file"], format="ascii.tab")
    stars = SkyCoord(
        ra=catalog["_RAJ2000"] * u.deg,
        dec=catalog["_DEJ2000"] * u.deg,
        frame="icrs",
        obstime="J2000.0",
        pm_ra_cosdec=catalog["pmRA"] * u.mas / u.yr,
        pm_dec=catalog["pmDE"] * u.mas / u.yr,
    )
    stars = stars.apply_space_motion(new_obstime=Time("2026-10-07"))

    plt.figure(1)
    plt.clf()

    plt.plot(source_data["sh_ra"], source_data["sh_dec"], marker="*", ms=12)
    plt.plot(stars.ra.to("deg"), stars.dec.to("deg"), "o")
    plt.gca().add_patch(circle)

    plt.gca().set_aspect("equal")
    plt.xlabel("RA [deg]")
    plt.ylabel("DEC [deg]")
    plt.title(f"{key}")

    plt.plot()
    plt.savefig(f"{key}.png")
