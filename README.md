
## Cara Penggunaan

1. Siapkan folder yang berisi gambar-gambar yang akan dikolase
2. Gambar harus diberi nama dengan format angka, contoh: "1.jpeg", "2.jpeg", dst
3. Sesuaikan parameter pada script sesuai kebutuhan:
   ```python
   create_collage(
       images_folder='materi',     # Folder berisi gambar input
       output_folder='output',     # Folder untuk menyimpan hasil
       images_per_row=3,           # Jumlah gambar per baris
       rows=5,                     # Jumlah baris
       padding=30,                 # Jarak antar gambar (dalam piksel)
       margin=50                   # Jarak dari tepi (dalam piksel)
   )
   ```

## Parameter yang Dapat Disesuaikan

- `images_folder`: Path folder yang berisi gambar input
- `output_folder`: Path folder untuk menyimpan hasil kolase
- `images_per_row`: Jumlah gambar per baris
- `rows`: Jumlah baris gambar
- `padding`: Jarak antar gambar dalam piksel
- `margin`: Jarak dari tepi halaman dalam piksel

## Output

- Script akan menghasilkan file kolase dengan format: `kolase_page_X.jpeg` (X adalah nomor halaman)
- Setiap file output memiliki resolusi 300 DPI
- Kualitas JPEG diset ke 95% untuk hasil optimal

## Catatan

- Pastikan gambar input memiliki format .jpeg
- Gambar akan diresize secara otomatis untuk menyesuaikan dengan ukuran kolase
- Script menggunakan algoritma LANCZOS untuk proses resize untuk hasil terbaik
