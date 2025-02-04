from django.core.management.base import BaseCommand
from pengaduan.seeder import run

class Command(BaseCommand):
    help = "Generate dummy data for the database"

    def handle(self, *args, **kwargs):
        run()
        self.stdout.write(self.style.SUCCESS("✅ Seeder berhasil dijalankan!"))
