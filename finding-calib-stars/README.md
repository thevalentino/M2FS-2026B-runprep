These stars are found following this procedure:

- Open image of the field in DS9
- Use Catalog tool to query GAIA DR2
- Request sources within 14.5 arcmin of the Shack-Hartmann star
- Limit their G band magnitude to within 16.5-17 mag (`$Gmag < 17 && $Gmag>16.5`)


This was the original selection.
After meeting with Mario Mateo on 12:00 pm Sept 13 2026, we think that the issue we are seeing with the coordinates of the calibration stars has to do with the way that GAIA reports their positions.


The fields I have to work with are:

- J0022_CFG01 SH: 5.2410717956,-0.7170246351,00:20:57.86,-00:43:01.29,2542218565870416000 
- J0022_CFG02 SH: 
- J0140_CFG07
- J0140_CFG08
- J2259_CFG04
- J2259_CFG05

I will start by making a new selection of stars requiring them to have small proper motions.

### J0022_CFG01

- The coordinates that XiaoXu provides for the SH star does not coincide with the one provided in the GAIA catalog. This is because XiaoXu provided the corrdinates as they would be on Oct 2026, that is, already corrected for proper motion. I will check if I can reproduce this transformation in position.

    - I can reproduce now the transformation to 2026-10 positions:
        - ICRS does not make use of equinoxes, what needs to be set is obstime
        - For dr3 obstime is J2016.0
        - For dr2 obstime is J2015.5
        - For Simbad obstime is J2000.0
        - For XiaoXu obstime is 2026-10-07

- I will try now to reproduce the "drift" that Mario Mateo observes when he propagates the positions of the calibration stars.
    - I tried several posibilities to explain the drift but nothing worked.

- I am preparing the .field files just as before with the only difference being that I will restrict pm to be less than 10 mas.
This is the filter I need to apply in DS9:
`$Gmag>16.5 && $Gmag < 17 && $pmRA<10 && $pmRA>-10 && $pmDE<10 && $pmDE>-10`


## Solution

At the end, I did my own selection again and made sure to report everything in FK5 epoch 2000.0 and this seems to have solved the issue. The transformation from J20000.0 to J2026.10 was being interpreted differently between Mario and I.

While doing this selection, which is in v5, I created multiple tsv files for the guide stars and the acquisition stars, on top of the calibration stars. There is information inthe script `format_stars_for_catalog.py` regarding what constraints were used to select these stars.
