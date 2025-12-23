import pandas as pd
import os

def run_preprocessing():
    # 1. Tentukan folder sumber (raw) dan tujuan (preprocessing)
    raw_dir = 'namadataset_raw'
    output_dir = 'preprocessing/namadataset_preprocessing'

    # Buat folder tujuan jika belum ada
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        print(f"Membuat folder: {output_dir}")

    # 2. Cek apakah folder raw ada
    if not os.path.exists(raw_dir):
        print(f"Error: Folder '{raw_dir}' tidak ditemukan!")
        return

    # 3. Cari file CSV di folder raw
    try:
        raw_files = [f for f in os.listdir(raw_dir) if f.endswith('.csv')]
        if not raw_files:
            print(f"Tidak ada file CSV di folder {raw_dir}")
            return

        raw_path = os.path.join(raw_dir, raw_files[0])
        print(f"Membaca data dari: {raw_path}")
        df = pd.read_csv(raw_path)

        # 4. PROSES PREPROCESSING (Sesuai eksperimen Anda)
        # Menyeragamkan kolom menjadi text dan sentiment
        df.columns = [col.lower() for col in df.columns]
        df = df.dropna() # Hapus baris kosong

        # 5. Simpan hasil ke folder preprocessing
        output_path = os.path.join(output_dir, 'youtube_preprocessed.csv')
        df.to_csv(output_path, index=False)
        print(f"BERHASIL! Data tersimpan di: {output_path}")

    except Exception as e:
        print(f"Terjadi kesalahan: {e}")

if __name__ == '__main__':
    run_preprocessing()
