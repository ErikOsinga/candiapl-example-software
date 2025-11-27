from astropy import units as u


def rotation_measure_uniform(
    electron_density: u.Quantity,
    magnetic_field: u.Quantity,
    path_length: u.Quantity,
) -> u.Quantity:
    """Compute the Faraday rotation measure for a uniform medium.

    This uses the standard approximation

        RM = 0.812 * n_e * B_parallel * L

    where n_e is in cm-3, B_parallel in microGauss, L in pc, and RM in rad m-2.

    Parameters
    ----------
    electron_density
        Free electron density as an astropy Quantity, with units convertible
        to cm-3.
    magnetic_field
        Magnetic field component along the line of sight as an astropy Quantity,
        with units convertible to microGauss.
    path_length
        Path length along the line of sight as an astropy Quantity, with units
        convertible to parsec.

    Returns
    -------
    rm
        Rotation measure as an astropy Quantity with units rad / m**2.
    """
    ne_val = electron_density.to(u.cm**-3).value
    b_val = magnetic_field.to(u.uG).value
    l_val = path_length.to(u.pc).value

    factor = 0.812 * u.rad / (u.m**2)
    rm = factor * ne_val * b_val * l_val
    return rm

