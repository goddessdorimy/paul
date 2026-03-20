import os
import re

# CONFIGURACIÓN: 'PalabraOriginal': 'TuPalabra'
REEMPLAZOS = {
    'nomenclaturavieja': 'NomenclaturaNueva',
    'oldprojectname': 'MyCustomProject',
    '.claude': '.opencode',
    'claude code': 'opencode',
    'claude': 'opencode',
    'AskUserQuestion': 'Question'
}

def ejecutar_reemplazo():
    for root, dirs, files in os.walk("."):
        if ".git" in dirs: dirs.remove(".git")
        for file in files:
            if file == "transformar.py" or file.endswith(".yml"): continue
            path = os.path.join(root, file)
            try:
                with open(path, 'r', encoding='utf-8') as f:
                    data = f.read()
                
                nuevo_contenido = data
                for viejo, nuevo in REEMPLAZOS.items():
                    # El flag re.IGNORECASE hace la magia
                    insensible = re.compile(re.escape(viejo), re.IGNORECASE)
                    nuevo_contenido = insensible.sub(nuevo, nuevo_contenido)
                
                if nuevo_contenido != data:
                    with open(path, 'w', encoding='utf-8') as f:
                        f.write(nuevo_contenido)
            except: pass

if __name__ == "__main__":
    ejecutar_reemplazo()
