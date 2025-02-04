# pengaduan/forms.py
from django import forms
from .models import Masyarakat, Petugas, Pengaduan, Tanggapan

class MasyarakatForm(forms.ModelForm):
    class Meta:
        model = Masyarakat
        fields = ['nik', 'nama', 'username', 'password', 'telp']

class PetugasForm(forms.ModelForm):
    class Meta:
        model = Petugas
        fields = ['nama_petugas', 'username', 'password', 'telp', 'level']

class PengaduanForm(forms.ModelForm):
    class Meta:
        model = Pengaduan
        fields = ['nik', 'isi_laporan', 'foto', 'status']

class TanggapanForm(forms.ModelForm):
    class Meta:
        model = Tanggapan
        fields = ['id_pengaduan', 'tanggapan', 'id_petugas']
