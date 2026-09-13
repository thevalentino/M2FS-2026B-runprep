"""
Checking the adjustment in position for the SH stars made by XiaoXu.
"""

import astropy.units as u
from astropy.coordinates import SkyCoord
from astropy.time import Time

# J0022_CFG1_SH
pos_gaia_dr3 = (5.241082979, -0.717018477)
pos_gaia_dr2 = (5.241083496, -0.717018158)
pos_simbad = "00:20:57.8639100322", "-00:43:01.233521373"
pos_xiao = (5.2410717956, -0.7170246351)

# Are the gaia and simbad positions the same?
sh_gaia_dr3 = SkyCoord(
    ra=pos_gaia_dr3[0] * u.deg,
    dec=pos_gaia_dr3[1] * u.deg,
    frame="icrs",
    equinox="J2000",
    obstime=Time("J2016.0"),
    pm_ra_cosdec=-3.745 * u.mas / u.yr,
    pm_dec=-2.062 * u.mas / u.yr,
)
sh_gaia_dr2 = SkyCoord(
    ra=pos_gaia_dr2[0] * u.deg,
    dec=pos_gaia_dr2[1] * u.deg,
    frame="icrs",
    equinox="J2000",
    obstime=Time("J2015.5"),
    pm_ra_cosdec=-3.745 * u.mas / u.yr,
    pm_dec=-2.062 * u.mas / u.yr,
)
sh_simbad = SkyCoord(
    ra=pos_simbad[0],
    dec=pos_simbad[1],
    unit=(u.hourangle, u.deg),
    frame="icrs",
    equinox="J2000",
    obstime=Time("J2000.0"),
    pm_ra_cosdec=-3.745 * u.mas / u.yr,
    pm_dec=-2.062 * u.mas / u.yr,
)
sh_xiao = SkyCoord(
    ra=pos_xiao[0] * u.deg,
    dec=pos_xiao[1] * u.deg,
    frame="icrs",
    equinox="J2000",
    obstime=Time("J2026.10"),
    pm_ra_cosdec=-3.745 * u.mas / u.yr,
    pm_dec=-2.062 * u.mas / u.yr,
)


print(
    sh_gaia_dr3.apply_space_motion(new_obstime=Time("2026-10-07")).to_string(
        "hmsdms", precision=6
    )
)
print(
    sh_gaia_dr2.apply_space_motion(new_obstime=Time("2026-10-07")).to_string(
        "hmsdms", precision=6
    )
)
print(
    sh_simbad.apply_space_motion(new_obstime=Time("2026-10-07")).to_string(
        "hmsdms", precision=6
    )
)
print(sh_xiao.to_string("hmsdms", precision=6))
