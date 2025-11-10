#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
import subprocess
import time
import requests

def iniciar_ngrok():
    try:
        print("🚀 Iniciando ngrok...")
        subprocess.Popen(["ngrok", "http", "8000"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        time.sleep(3)  # espera o túnel abrir

        # obtém o link público ativo
        resp = requests.get("http://127.0.0.1:4040/api/tunnels")
        data = resp.json()
        url = data["tunnels"][0]["public_url"]
        print(f"🌐 Ngrok ativo em: {url}")
        os.environ["NGROK_URL"] = url  # armazena em variável de ambiente
    except Exception as e:
        print(f"⚠️ Erro ao iniciar ngrok: {e}")

def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ecommerce.settings')

    if "runserver" in sys.argv:
        iniciar_ngrok()

    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    main()
