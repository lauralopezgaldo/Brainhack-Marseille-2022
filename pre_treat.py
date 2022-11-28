import numpy as np
from scipy import signal


def filter_lfp(lfps):
    """Basic filtering of the continuous LFP before cutting it into epochs.
    The signal is expected to be already low-pass filtered at 250Hz

    """
    fs_lfp = 1000  # sampling frequency of the LFP signal in Hz
    fc_hp = 1  # cut-off frequency of the high pass filter in Hz
    fc_notch = [
        49.5,
        50.5,
    ]  # band of frequencies to be attenuated in the notch filter in Hz

    # perform a High pass filter - butterworth filter of order 6 at 1Hz
    sos = signal.butter(6, fc_hp, "hp", fs=fs_lfp, output="sos")
    LFP_hp = signal.sosfilt(sos, lfps)

    # perform a Notch filter of order 4 at 50 Hz
    sos_notch = signal.butter(4, fc_notch, "bandstop", fs=fs_lfp, output="sos")
    lfp_nf = signal.sosfilt(sos_notch, LFP_hp)

    return lfp_nf
