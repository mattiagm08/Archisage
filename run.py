import subprocess
import os
import platform
import time
import webbrowser

def run_command(command, cwd):
    shell = True if platform.system() == "Windows" else False
    return subprocess.Popen(command, cwd=cwd, shell=shell)

if __name__ == "__main__":
    root_dir = os.path.dirname(os.path.abspath(__file__))
    backend_dir = os.path.join(root_dir, "backend")
    frontend_dir = os.path.join(root_dir, "frontend")

    print("🚀 Avvio Archisage in corso...\n")

    # AVVIA BACKEND
    print("🔧 Avvio backend...")
    backend = run_command(["npm", "run", "dev"], cwd=backend_dir)

    # ATTENDI
    time.sleep(3)

    # AVVIA FRONTEND
    print("\n💫 Avvio frontend...")
    frontend = run_command(["npx", "expo", "start", "--web"], cwd=frontend_dir)

    # ATTENDI
    time.sleep(10)

    print("\n✅ Tutto avviato. Premi CTRL+C per fermare entrambi i processi.\n")

    try:
        backend.wait()
        frontend.wait()
    except KeyboardInterrupt:
        print("\n🛑 Interruzione rilevata. Chiusura processi...")
        backend.terminate()
        frontend.terminate()
