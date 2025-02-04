import factory
from faker import Faker
from pengaduan.models import Masyarakat, Petugas, Pengaduan, Tanggapan

fake = Faker()

class MasyarakatFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Masyarakat

    nik = factory.LazyAttribute(lambda _: fake.unique.numerify(text="###############"))
    nama = factory.Faker('name')
    username = factory.Faker('user_name')
    password = factory.Faker('password')
    telp = factory.LazyAttribute(lambda _: fake.numerify(text="08##########"))  # Maksimal 13 karakter

# 🏢 Factory untuk Petugas
class PetugasFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Petugas

    nama_petugas = factory.LazyAttribute(lambda _: fake.name())
    username = factory.LazyAttribute(lambda _: fake.user_name())
    password = factory.LazyAttribute(lambda _: fake.password())
    telp = factory.LazyAttribute(lambda _: fake.numerify(text="08##########"))
    level = factory.Iterator(["admin", "petugas"])

# 📢 Factory untuk Pengaduan
class PengaduanFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Pengaduan

    nik = factory.SubFactory(MasyarakatFactory)
    isi_laporan = factory.LazyAttribute(lambda _: fake.text())
    status = factory.Iterator(["0", "proses", "selesai"])

# 🗂 Factory untuk Tanggapan
class TanggapanFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Tanggapan

    id_pengaduan = factory.SubFactory(PengaduanFactory)
    tanggapan = factory.LazyAttribute(lambda _: fake.text())
    id_petugas = factory.SubFactory(PetugasFactory)
