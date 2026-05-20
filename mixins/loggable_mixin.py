from datetime import datetime


class LoggableMixin:

    def buat_log(self, pesan):
        waktu = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"[LOG {waktu}] {pesan}")