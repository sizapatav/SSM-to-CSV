import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import csv

def load_ssm(path_file, cut_in, cut_end):
    """Load an SSM file and extract wavelength and intensity data."""
    aux = pd.read_csv(path_file).to_numpy()
    wavelengths = np.zeros(np.shape(aux)[0])
    intensities = np.zeros(np.shape(aux)[0])

    for i in range(np.shape(aux)[0]):
        wavelengths[i], intensities[i] = np.fromstring(aux[i][0], dtype=float, sep='  ')
    
    wavelengths = wavelengths[cut_in:cut_end]
    intensities = intensities[cut_in:cut_end]
    
    return wavelengths, intensities

def save_csv(filename, wavelengths, intensities):
    """Save extracted data to a CSV file."""
    with open(filename, mode="w", newline="") as file:
        csv_writer = csv.writer(file)
        csv_writer.writerow(["Wavelength (nm)", "Counts"])
        for x, y in zip(wavelengths, intensities):
            csv_writer.writerow([x, y])
    
    print(f"File '{filename}' successfully created.")

def plot_spectra(wavelengths, spectra_dict):
    """Plot multiple spectra with labels and colors."""
    plt.title('Emission spectrum with a 405nm excitation source')

    for label, (color, intensities) in spectra_dict.items():
        plt.plot(wavelengths, intensities, color=color, label=label)

    plt.xlabel('Wavelength [nm]')
    plt.ylabel('Counts')
    plt.legend()
    plt.show()

def main():
    # Define wavelength range
    cut_i = 450
    cut_f = 1300

    # Load data
    wavelengths, green = load_ssm('fluo_green.SSM', cut_i, cut_f)
    _, orange = load_ssm('fluo_orange.SSM', cut_i, cut_f)
    _, pink = load_ssm('fluo_pink.SSM', cut_i, cut_f)
    _, yellow = load_ssm('fluo_yellow.SSM', cut_i, cut_f)

    # Store spectra with colors
    spectra_dict = {
        "Green": ('g', green),
        "Orange": ([1, 0.5, 0], orange),
        "Pink": ([1, 0, 1], pink),
        "Yellow": ([0.8, 0.8, 0], yellow)
    }

    # Plot spectra
    plot_spectra(wavelengths, spectra_dict)

    # Save data to CSV
    save_csv('Export.csv', wavelengths, green)

if __name__ == "__main__":
    main()
