from pengaduan.factories import MasyarakatFactory, PetugasFactory, PengaduanFactory, TanggapanFactory

def run():
    print("📌 Mengisi database dengan data dummy...")

    # Buat 10 masyarakat
    masyarakat_list = MasyarakatFactory.create_batch(10)

    # Buat 5 petugas (termasuk admin)
    petugas_list = PetugasFactory.create_batch(5)

    # Buat 15 laporan pengaduan
    pengaduan_list = PengaduanFactory.create_batch(15)

    # Buat 10 tanggapan untuk laporan
    tanggapan_list = TanggapanFactory.create_batch(10)

    print("✅ Data dummy berhasil dimasukkan!")
