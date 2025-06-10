# SSM-to-CSV
A simple python script for converting `.ssm` files exported by the Black Comet spectrometer from SpectraNet into `.csv` files.

The file `SSMtoCSV.py` contains a set of functions for extracting, plotting and saving the acquired spectral information.

Usage example 
```
import SSMtoCSV as ssm

# Define wavelength range
cut_i = 450  # Initial wavelength cutoff
cut_f = 1300 # Final wavelength cutoff

# Load spectral data from an SSM file
wavelength, counts = ssm.load_ssm('TestSpect.SSM', cut_i, cut_f)

# Plot the spectrum
ssm.plot_spectra(wavelength, {"Green": ("g", counts)})
```
