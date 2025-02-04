from django.db import models

# 🧑‍🤝‍🧑 Model untuk Masyarakat (User yang Melaporkan)
class Masyarakat(models.Model):
    nik = models.CharField(max_length=16, unique=True)  # NIK harus unik
    nama = models.CharField(max_length=35)
    username = models.CharField(max_length=25, unique=True)
    password = models.CharField(max_length=255)  # Gunakan hashing nanti
    telp = models.CharField(max_length=15)

    def __str__(self):
        return self.nama


# 🏢 Model untuk Petugas (Admin/Petugas yang Menangani Laporan)
class Petugas(models.Model):
    LEVEL_CHOICES = [
        ('admin', 'Administrator'),
        ('petugas', 'Petugas'),
    ]
    nama_petugas = models.CharField(max_length=35)
    username = models.CharField(max_length=25, unique=True)
    password = models.CharField(max_length=255)  # Gunakan hashing nanti
    telp = models.CharField(max_length=15)
    level = models.CharField(max_length=10, choices=LEVEL_CHOICES)

    def __str__(self):
        return f"{self.nama_petugas} ({self.level})"


# 📢 Model untuk Pengaduan (Laporan dari Masyarakat)
class Pengaduan(models.Model):
    STATUS_CHOICES = [
        ('0', 'Belum Diproses'),
        ('proses', 'Sedang Diproses'),
        ('selesai', 'Selesai'),
    ]
    tgl_pengaduan = models.DateTimeField(auto_now_add=True)  # Otomatis tanggal saat laporan dibuat
    nik = models.ForeignKey(Masyarakat, on_delete=models.CASCADE)  # Relasi ke masyarakat yang melapor
    isi_laporan = models.TextField()
    foto = models.ImageField(upload_to='pengaduan_foto/', blank=True, null=True)  # Penyimpanan file gambar
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='0')

    def __str__(self):
        return f"Laporan {self.id} - {self.nik.nama}"


# 🗂 Model untuk Tanggapan (Respons dari Petugas/Admin)
class Tanggapan(models.Model):
    tgl_tanggapan = models.DateTimeField(auto_now_add=True)  # Otomatis tanggal saat tanggapan dibuat
    id_pengaduan = models.ForeignKey(Pengaduan, on_delete=models.CASCADE)  # Relasi ke pengaduan
    tanggapan = models.TextField()
    id_petugas = models.ForeignKey(Petugas, on_delete=models.CASCADE)  # Relasi ke petugas yang menangani

    def __str__(self):
        return f"Tanggapan untuk Laporan {self.id_pengaduan.id}"