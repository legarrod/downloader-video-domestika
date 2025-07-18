#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys, re
from pathlib import Path

# No sólo vídeos, ahora también subtítulos .srt
VIDEO_EXTS = {'.mp4', '.mkv', '.avi', '.mov', '.flv', '.wmv', '.srt'}

def renombrar_videos(ruta_raiz: Path, texto_base: str):
    contador = 0
    # Limpiamos un posible "- U# -" del texto base
    m = re.match(r'^(.*?)(?:\s*-\s*[Uu]\d+\s*-\s*)?$', texto_base)
    texto_fijo = m.group(1).strip()

    for archivo in ruta_raiz.rglob('*'):
        if not archivo.is_file() or archivo.suffix.lower() not in VIDEO_EXTS:
            continue

        # Extraemos el nombre de la carpeta padre, ej. "Unidad_1"
        carpeta = archivo.parent.name

        # Buscamos un número al final de "Unidad_1" o "U1", caso insensible
        m2 = re.match(r'(?i)^(?:unidad[_ ]?|m|u)(\d+)(?:[_\-].*)?$', carpeta)
        if not m2:
            continue

        unidad = m2.group(1)
        # Construimos el prefijo que queremos eliminar
        prefijo = f"{texto_fijo} - U{unidad} - "

        if archivo.name.startswith(prefijo):
            # Lo que viene después del prefijo
            nuevo_nombre = archivo.name[len(prefijo):].lstrip()
            destino = archivo.with_name(nuevo_nombre)
            try:
                archivo.rename(destino)
                print(f"✔ «{archivo.name}» → «{destino.name}»")
                contador += 1
            except Exception as e:
                print(f"❌ Error con «{archivo.name}»: {e}")

    if contador:
        print(f"\n🎉 ¡{contador} archivo(s) renombrado(s)!") 
    else:
        print("\n⚠️  No se encontró ningún archivo para renombrar.")

def main():
    print("\n📁  Renombrador de vídeos y subtítulos recursivo\n")
    ruta_input = input("→ Ruta de la carpeta principal: ").strip()
    texto_base = input("→ Texto base a eliminar (sin ‘- U# -’): ").strip()

    ruta = Path(ruta_input).expanduser()
    if not ruta.is_dir():
        print(f"\n❌ ERROR: «{ruta}» no es carpeta válida.")
        sys.exit(1)

    print(f"\n🔍 Procesando «{ruta}»…\n")
    renombrar_videos(ruta, texto_base)
    print("\n— Tu biblioteca renombrada con precisión poética —\n")

if __name__ == "__main__":
    main()
