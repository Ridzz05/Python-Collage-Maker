from PIL import Image
import os
import math

def create_collage(images_folder, output_folder, images_per_row=5, rows=5, padding=10, margin=20):
    # Membuat folder output jika belum ada
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    # Ukuran A4 landscape dalam piksel (pada 300 DPI)
    A4_WIDTH = 3508  # 297 mm
    A4_HEIGHT = 2480 # 210 mm
    
    # Mengambil daftar file gambar dari folder dan mengurutkannya
    image_files = []
    for i in range(1, 51):  # Diubah dari 27 menjadi 51 untuk mengakomodasi lebih banyak gambar
        filename = f"{i}.jpeg"
        if os.path.exists(os.path.join(images_folder, filename)):
            image_files.append(filename)
    
    if not image_files:
        print("Tidak ada file gambar ditemukan")
        return
    
    # Menghitung ukuran gambar yang sesuai untuk A4 landscape
    usable_width = A4_WIDTH - (2 * margin) - ((images_per_row - 1) * padding)
    usable_height = A4_HEIGHT - (2 * margin) - ((rows - 1) * padding)
    
    img_width = usable_width // images_per_row
    img_height = usable_height // rows
    
    # Menghitung jumlah gambar per halaman dan total halaman
    images_per_page = images_per_row * rows  # 5x5 = 25 gambar per halaman
    total_pages = math.ceil(len(image_files) / images_per_page)
    
    for page in range(total_pages):
        # Membuat canvas A4 landscape putih
        canvas = Image.new('RGB', (A4_WIDTH, A4_HEIGHT), 'white')
        
        # Menghitung gambar untuk halaman ini
        start_idx = page * images_per_page
        end_idx = min(start_idx + images_per_page, len(image_files))
        page_images = image_files[start_idx:end_idx]
        
        for idx, img_file in enumerate(page_images):
            # Menghitung posisi baris dan kolom
            row = idx // images_per_row
            col = idx % images_per_row
            
            # Menghitung koordinat x dan y
            x = margin + (col * (img_width + padding))
            y = margin + (row * (img_height + padding))
            
            # Membuka, resize, dan menempelkan gambar
            img = Image.open(os.path.join(images_folder, img_file))
            img = img.resize((img_width, img_height), Image.Resampling.LANCZOS)
            canvas.paste(img, (x, y))
            
            print(f"Menempatkan gambar {img_file} pada posisi baris {row+1}, kolom {col+1} di halaman {page+1}")
        
        # Menyimpan kolase
        output_path = os.path.join(output_folder, f'kolase_page_{page + 1}.jpeg')
        canvas.save(output_path, quality=95, dpi=(300, 300))
        print(f"Halaman kolase {page + 1} telah dibuat: {output_path}")

# Penggunaan fungsi
images_folder = 'materi'  # Folder berisi gambar input
output_folder = 'output'  # Folder untuk menyimpan hasil kolase

create_collage(
    images_folder=images_folder,
    output_folder=output_folder,
    images_per_row=3,     # Jumlah gambar per baris
    rows=5,               # Jumlah baris
    padding=30,           # Jarak antar gambar diubah dari 10 menjadi 50 piksel
    margin=50           # Jarak dari tepi canvas diubah dari 20 menjadi 100 piksel
)
