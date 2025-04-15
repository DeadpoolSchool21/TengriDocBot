import subprocess
import sys

# Список необходимых библиотек
required_modules = [
    'requests',
    'beautifulsoup4',
    'PyMuPDF',
    'sentence_transformers'
]

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

def check_and_install():
    for module in required_modules:
        try:
            __import__(module)
            print(f"{module} уже установлен.")
        except ImportError:
            print(f"{module} не найден. Устанавливаем...")
            install(module)
            print(f"{module} успешно установлен.")

if __name__ == "__main__":
    check_and_install()
