from dataclasses import dataclass
from pathlib import Path
import tomllib

from astropy import units as u


@dataclass
class RMConfig:
    """
    Dataclass to hold rotation measure configuration parameters.
    
    Parameters
    ----------
        electron_density: Free electron density as an astropy Quantity.
        magnetic_field: Magnetic field component along the line of sight as an astropy Quantity.
        path_length: Path length along the line of sight as an astropy Quantity.
    """
    electron_density: u.Quantity
    magnetic_field: u.Quantity
    path_length: u.Quantity


def load_config(path: str | Path) -> RMConfig:
    """Load RM configuration from a TOML file.

    The file is expected to have a section like:

        [rm]
        electron_density_cm3 = 0.03
        magnetic_field_uG = 5.0
        path_length_pc = 1000.0
    """
    path = Path(path)
    with path.open("rb") as f:
        data = tomllib.load(f)

    rm_section = data["rm"]

    ne = rm_section["electron_density_cm3"] * (u.cm**-3)
    b = rm_section["magnetic_field_uG"] * u.uG
    length = rm_section["path_length_pc"] * u.pc

    return RMConfig(
        electron_density=ne,
        magnetic_field=b,
        path_length=length,
    )

