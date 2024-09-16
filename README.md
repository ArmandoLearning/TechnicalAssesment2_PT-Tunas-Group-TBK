# Modul Manajemen Ruangan

Modul ini memungkinkan Anda untuk mengelola ruangan dan pemesanan dengan validasi dan pembaruan status.

## Instalasi

1. **Tempatkan modul di direktori addons Odoo Anda:**

   ```bash
   cp -r C:\odoo14\ruangan_module\ruangan_management C:\odoo14\odoo14
Perbarui Daftar Aplikasi Odoo:

bash
Salin kode
./odoo-bin -u all
Instal modul melalui antarmuka web Odoo:

Masuk ke aplikasi (Apps), cari "Manajemen Ruangan", dan klik "Install".

Penggunaan
Master Ruangan: Mengelola detail ruangan.
Pemesanan Ruangan: Membuat dan mengelola pemesanan ruangan.
Fitur
Kendala Unik: Menjamin tidak ada nama ruangan atau nama pemesanan yang duplikat.
Validasi: Mencegah pemesanan yang tumpang tindih untuk ruangan yang sama pada tanggal yang sama.
Pembaruan Status: Memproses dan menandai pemesanan sebagai selesai.
Contoh
Untuk membuat pemesanan:

Masuk ke Pemesanan Ruangan.
Klik Create dan isi detail pemesanan.
Gunakan Proses Pemesanan untuk memperbarui status menjadi 'On Going'.
Gunakan Tandai Selesai untuk menandai pemesanan sebagai selesai.
Struktur Modul

Model:

Master Ruangan: Menyimpan data tentang ruangan seperti nama, tipe, lokasi, foto, kapasitas, dan keterangan.
Pemesanan Ruangan: Menyimpan data tentang pemesanan seperti nomor pemesanan, ruangan, nama pemesanan, tanggal pemesanan, status pemesanan, dan catatan pemesanan.
Views:

Daftar Master Ruangan: Menampilkan daftar ruangan dengan informasi dasar.
Form Master Ruangan: Menampilkan formulir untuk mengedit detail ruangan.
Daftar Pemesanan Ruangan: Menampilkan daftar pemesanan dengan informasi dasar dan status.
Form Pemesanan Ruangan: Menampilkan formulir untuk mengedit dan memperbarui pemesanan.

Validasi:

Tidak diperbolehkan memesan ruangan yang sama pada tanggal yang sama.
Nama pemesanan tidak boleh sama dengan pemesanan lain.
Nama ruangan harus unik.
