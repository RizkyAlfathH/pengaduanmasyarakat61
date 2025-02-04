# pengaduan/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Masyarakat, Petugas, Pengaduan, Tanggapan
from .forms import MasyarakatForm, PetugasForm, PengaduanForm, TanggapanForm
from django.shortcuts import render
from .models import Masyarakat

def home(request):
    # Bisa menampilkan daftar masyarakat atau halaman lain
    masyarakat = Masyarakat.objects.all()
    return render(request, 'home.html', {'masyarakat': masyarakat})


# Masyarakat Views
def masyarakat_list(request):
    masyarakat = Masyarakat.objects.all()
    return render(request, 'masyarakat_list.html', {'masyarakat': masyarakat})

def masyarakat_create(request):
    if request.method == 'POST':
        form = MasyarakatForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('masyarakat_list')
    else:
        form = MasyarakatForm()
    return render(request, 'masyarakat_form.html', {'form': form})

def masyarakat_update(request, pk):
    masyarakat = get_object_or_404(Masyarakat, pk=pk)
    if request.method == 'POST':
        form = MasyarakatForm(request.POST, instance=masyarakat)
        if form.is_valid():
            form.save()
            return redirect('masyarakat_list')
    else:
        form = MasyarakatForm(instance=masyarakat)
    return render(request, 'masyarakat_form.html', {'form': form})

def masyarakat_delete(request, pk):
    masyarakat = get_object_or_404(Masyarakat, pk=pk)
    if request.method == 'POST':
        masyarakat.delete()
        return redirect('masyarakat_list')
    return render(request, 'masyarakat_confirm_delete.html', {'masyarakat': masyarakat})

# Petugas Views
def petugas_list(request):
    petugas = Petugas.objects.all()
    return render(request, 'petugas_list.html', {'petugas': petugas})

def petugas_create(request):
    if request.method == 'POST':
        form = PetugasForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('petugas_list')
    else:
        form = PetugasForm()
    return render(request, 'petugas_form.html', {'form': form})

def petugas_update(request, pk):
    petugas = get_object_or_404(Petugas, pk=pk)
    if request.method == 'POST':
        form = PetugasForm(request.POST, instance=petugas)
        if form.is_valid():
            form.save()
            return redirect('petugas_list')
    else:
        form = PetugasForm(instance=petugas)
    return render(request, 'petugas_form.html', {'form': form})

def petugas_delete(request, pk):
    petugas = get_object_or_404(Petugas, pk=pk)
    if request.method == 'POST':
        petugas.delete()
        return redirect('petugas_list')
    return render(request, 'petugas_confirm_delete.html', {'petugas': petugas})

# Pengaduan Views
def pengaduan_list(request):
    pengaduan = Pengaduan.objects.all()
    return render(request, 'pengaduan_list.html', {'pengaduan': pengaduan})

def pengaduan_create(request):
    if request.method == 'POST':
        form = PengaduanForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('pengaduan_list')
    else:
        form = PengaduanForm()
    return render(request, 'pengaduan_form.html', {'form': form})

def pengaduan_update(request, pk):
    pengaduan = get_object_or_404(Pengaduan, pk=pk)
    if request.method == 'POST':
        form = PengaduanForm(request.POST, request.FILES, instance=pengaduan)
        if form.is_valid():
            form.save()
            return redirect('pengaduan_list')
    else:
        form = PengaduanForm(instance=pengaduan)
    return render(request, 'pengaduan_form.html', {'form': form})

def pengaduan_delete(request, pk):
    pengaduan = get_object_or_404(Pengaduan, pk=pk)
    if request.method == 'POST':
        pengaduan.delete()
        return redirect('pengaduan_list')
    return render(request, 'pengaduan_confirm_delete.html', {'pengaduan': pengaduan})

# Tanggapan Views
def tanggapan_list(request):
    tanggapan = Tanggapan.objects.all()
    return render(request, 'tanggapan_list.html', {'tanggapan': tanggapan})

def tanggapan_create(request):
    if request.method == 'POST':
        form = TanggapanForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tanggapan_list')
    else:
        form = TanggapanForm()
    return render(request, 'tanggapan_form.html', {'form': form})
