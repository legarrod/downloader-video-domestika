# Domestika Downloader

Herramienta para descargar y organizar cursos de Domestika, incluyendo videos y subtítulos.

## Requisitos Previos

- Node.js (v14 o superior)
- Python 3 (para el script de renombrado)
- NPM (viene con Node.js)
- FFmpeg (para incrustar subtítulos)
- N_m3u8DL-RE (incluido en el repositorio)

## Instalación

1. Clona este repositorio:
   ```bash
   git clone [URL_DEL_REPOSITORIO]
   cd domestika-downloader
   ```

2. Instala las dependencias de Node.js:
   ```bash
   npm install
   ```

3. Configura las credenciales de Domestika:
   - Copia el archivo `.env.example` a `.env`
   - Edita el archivo `.env` y agrega tu correo y contraseña de Domestika

## Uso

### Descargar un curso

1. Ejecuta el script principal:
   ```bash
   # Para macOS/Linux:
   npm run start:mac
   
   # O alternativamente:
   node index.mac.js
   ```

2. Sigue las instrucciones en pantalla:
   - Ingresa la URL del curso de Domestika
   - Selecciona el idioma de los subtítulos
   - Elige la calidad del video
   - Decide si deseas descargar solo los subtítulos o videos completos

### Renombrar archivos descargados

Después de descargar los videos, puedes usar el script de Python para organizar los nombres de los archivos:

```bash
# Navega al directorio del script
cd /ruta/a/domestika-downloader

# Ejecuta el script de renombrado
python3 rename_videos.py

# Sigue las instrucciones para ingresar:
# 1. La ruta de la carpeta con los videos
# 2. El texto base que deseas eliminar de los nombres de archivo
```

## Estructura de Carpetas

Los videos se descargan en la siguiente estructura:
```
domestika_courses/
└── Nombre_del_Curso/
    ├── Unidad_1/
    │   ├── video1.mp4
    │   ├── video1.srt
    │   └── ...
    ├── Unidad_2/
    └── ...
```

## Dependencias Principales

- **Node.js**:
  - puppeteer: Para la automatización del navegador
  - cheerio: Para el análisis de HTML
  - inquirer: Para la interfaz de línea de comandos
  - dotenv: Para manejar variables de entorno

- **Python**:
  - Solo requiere la biblioteca estándar de Python 3

## Solución de Problemas

- **Error de autenticación**: Asegúrate de que las credenciales en `.env` sean correctas.
- **Videos sin descargar**: Verifica tu conexión a internet y que la URL del curso sea accesible.
- **Problemas con FFmpeg**: Asegúrate de tener FFmpeg instalado y accesible desde la línea de comandos.

## Notas Importantes

- Este script es solo para uso personal y educativo.
- Respeta los términos de servicio de Domestika.
- Los cursos descargados deben ser solo para tu uso personal.

## Licencia

Este proyecto está bajo la licencia ISC. Ver el archivo `LICENSE` para más detalles.
