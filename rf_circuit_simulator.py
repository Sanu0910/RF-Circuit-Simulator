import numpy as np
import matplotlib.pyplot as plt
import skrf as rf  # Scikit-RF for handling S-parameters

def load_sparameter_file(filename):
    """Loads a Touchstone S-parameter file (.s2p)."""
    network = rf.Network(filename)
    return network

def plot_s_parameters(network):
    """Plots S-parameter magnitude and phase."""
    freq = network.f / 1e9  # Convert frequency to GHz
    plt.figure(figsize=(12, 5))
    
    for i in range(network.s.shape[1]):
        for j in range(network.s.shape[2]):
            plt.subplot(1, 2, 1)
            plt.plot(freq, 20*np.log10(abs(network.s[:, i, j])), label=f'S{i+1}{j+1}')
            plt.xlabel('Frequency (GHz)')
            plt.ylabel('Magnitude (dB)')
            plt.title('S-Parameters Magnitude')
            plt.legend()
            
            plt.subplot(1, 2, 2)
            plt.plot(freq, np.angle(network.s[:, i, j], deg=True), label=f'S{i+1}{j+1}')
            plt.xlabel('Frequency (GHz)')
            plt.ylabel('Phase (Degrees)')
            plt.title('S-Parameters Phase')
            plt.legend()
    
    plt.show()

def calculate_noise_figure(network):
    """Calculates the Noise Figure (NF) in dB."""
    s21_mag = abs(network.s[:, 1, 0])  # Gain |S21|
    noise_figure = 1 + (1 / (s21_mag ** 2))
    noise_figure_db = 10 * np.log10(noise_figure)
    
    plt.figure(figsize=(8, 4))
    plt.plot(network.f / 1e9, noise_figure_db, label='Noise Figure (dB)')
    plt.xlabel('Frequency (GHz)')
    plt.ylabel('Noise Figure (dB)')
    plt.title('Noise Figure vs Frequency')
    plt.legend()
    plt.grid()
    plt.show()

def main():
    filename = input("Enter the S-parameter file path: ")
    network = load_sparameter_file(filename)
    plot_s_parameters(network)
    calculate_noise_figure(network)

if __name__ == "__main__":
    main()
