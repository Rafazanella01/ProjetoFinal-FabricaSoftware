import os
import subprocess
import platform

def run_django_server():
    # Caminho relativo para o diretório do projeto Django
    project_directory = os.path.join(os.path.dirname(__file__), 'src\PSF_GESTAO_FINANCEIRA')
    manage_py = os.path.join(project_directory, 'manage.py')
    
    # Navegar para o diretório do projeto
    os.chdir(project_directory)
    
    # Verificar o sistema operacional
    if platform.system() == 'Windows':
        python_executable = 'python'
    else:
        python_executable = 'python3'
    
    # Executar o comando para iniciar o servidor Django
    subprocess.run([python_executable, manage_py, 'runserver', '0.0.0.0:8000'])

if __name__ == "__main__":
    run_django_server()
