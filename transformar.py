import os

# CONFIGURACIÓN: 'PalabraOriginal': 'TuPalabra'
REEMPLAZOS = {
    'NomenclaturaVieja': 'NomenclaturaNueva',
    'OldProjectName': 'MyCustomProject',
    'api_endpoint_v1': 'mi_api_v2'
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
                for viejo, nuevo in REEMPLAZOS.items():
                    data = data.replace(viejo, nuevo)
                with open(path, 'w', encoding='utf-8') as f:
                    f.write(data)
            except: pass

if __name__ == "__main__":
    ejecutar_reemplazo()