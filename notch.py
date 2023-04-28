import numpy as np
from scipy.io import wavfile
from scipy import signal

# wavファイルの読み込み
sample_rate, data = wavfile.read('input.wav')

# ノッチフィルタのパラメータ設定
f0 = 2000.0  # カットする周波数
Q = 35     # フィルタの品質係数

# ノッチフィルタの周波数応答を計算
w0 = f0 / (sample_rate / 2)
b, a = signal.iirnotch(w0, Q)

# フィルタリング
filtered_data = signal.filtfilt(b, a, data)

# 出力ファイルに書き込み
wavfile.write('output_notch.wav', sample_rate, np.int16(filtered_data))
