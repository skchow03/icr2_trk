# TRK-CSV File Converter

This repository contains Python scripts for converting TRK files to CSV and vice versa.

## Description

The TRK-CSV file converter includes two Python scripts:

1. `trk2csv.py`: This script takes a TRK file as an argument and converts it into multiple CSV files, each representing a specific part of the TRK file structure.
2. `csv2trk.py`: This script takes the previously generated CSV files and rebuilds the original TRK file.

These scripts are useful for inspecting and modifying TRK files in a human-readable format.

## Getting Started

### Dependencies

- Python 3.7 or later
- NumPy library

### Installing

1. Clone the repository to your local machine:

    ```
    git clone https://github.com/yourusername/trk-csv-converter.git
    ```

2. Navigate into the project directory:

    ```
    cd trk-csv-converter
    ```

3. Install the required dependencies:

    ```
    pip install numpy
    ```

### Usage

1. To convert a TRK file to CSV:

    ```
    python trk2csv.py <TRK file>
    ```

2. To convert CSV files back to a TRK file:

    ```
    python csv2trk.py <CSV file prefix>
    ```

## License

Distributed under the MIT License. See `LICENSE` for more information.

## Contact

Project Link: https://github.com/skchow03/icr2_trk/
