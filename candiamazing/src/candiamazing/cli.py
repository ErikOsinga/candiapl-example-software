"""Command-line interface to compute Faraday rotation.

Given an input configuration file, will print the amount of Faraday rotation expected
under various assumptions about the electron density and magnetic field along the line
of sight.
"""

import argparse
from pathlib import Path

from candiamazing.config import load_config
from candiamazing.core import rotation_measure_uniform


def parse_args():
    """Parse arguments from CLI."""
    parser = argparse.ArgumentParser(
        description="Compute rotation measure from a configuration file.",
    )
    parser.add_argument(
        "-c",
        "--config",
        type=Path,
        default=Path("config_example.toml"),
        help="Path to the TOML configuration file.",
    )
    return parser.parse_args()


def main():
    """Compute Faraday rotation given input file."""
    args = parse_args()

    cfg = load_config(args.config)
    rm = rotation_measure_uniform(
        cfg.electron_density,
        cfg.magnetic_field,
        cfg.path_length,
    )

    # Astropy quantities support formatting with f-strings
    print(
        f"Electron density: {cfg.electron_density.value} [{cfg.electron_density.unit}]"
    )
    print(f"Magnetic field:   {cfg.magnetic_field.value} [{cfg.magnetic_field.unit}]")
    print(f"Path length:      {cfg.path_length.value} [{cfg.path_length.unit}]")
    print("---")
    print(f"Rotation measure: {rm.value:.3g} [{rm.unit}]")


if __name__ == "__main__":
    main()
