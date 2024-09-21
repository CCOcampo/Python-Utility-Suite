# Transcripción de Audio a Texto 🎙️➡️📝

Este proyecto te permite grabar audio y transcribirlo automáticamente a texto para utilizarlo en la transcripción de reuniones, entrevistas, notas de voz o cualquier tipo de grabación de audio.

La transcripción se realiza mediante **Groq**, una empresa estadounidense de inteligencia artificial que ha desarrollado un circuito integrado específico de aplicación llamado **Unidad de Procesamiento del Lenguaje**. Este hardware está diseñado para acelerar el rendimiento de inferencia de las cargas de trabajo de IA.

## Características principales 🚀

- 🎙️ **Grabación de Audio en Tiempo Real**: Captura audio directamente desde tu micrófono.
- 🔊 **Transcripción precisa**: Utiliza el potente modelo **whisper-large-v3** para transcribir el audio con precisión.
- 📋 **Copia automática al portapapeles**: La transcripción resultante se copia automáticamente al portapapeles para su uso inmediato en otras aplicaciones.
- 🌐 **Compatible con Español**: El modelo está optimizado para trabajar con audios en español, ideal para usuarios hispanohablantes.

## Herramientas utilizadas 🛠️

Este proyecto está construido con las siguientes herramientas y tecnologías:

- **Python**: El lenguaje base utilizado para desarrollar este proyecto.
- **PyAudio**: Para la grabación de audio desde el micrófono.
- **Groq API**: Utiliza la infraestructura de Groq para la transcripción de audio mediante su Unidad de Procesamiento del Lenguaje.
- **Whisper-large-v3**: Modelo utilizado para convertir el audio en texto.
- **Pyperclip y PyAutoGUI**: Herramientas utilizadas para copiar la transcripción al portapapeles y automatizar el pegado del texto en otras aplicaciones.

## Requisitos de instalación 🖥️

### 1. Clonar el repositorio:

```bash
 git clone https://github.com/tu_usuario/transcripcion-audio-texto.git
 cd transcripcion-audio-texto
```

### 2. Instalar dependencias:

Instala las librerías necesarias desde el archivo requirements.txt:

```python
 pip install -r requirements.txt
```

### 3. Crear una cuenta en Groq:

Para utilizar el servicio de transcripción, regístrate en Groq y obtén una API key:

1. Regístrate en Groq.
2. Accede a tu cuenta y genera una API key.
3. Guarda tu API key en un archivo llamado `Key.py` con el siguiente formato:

   ```python
   Api_Key = 'tu_api_key_aqui'
   ```

## Uso

Para iniciar la grabación y transcripción del audio, ejecuta el siguiente comando:
python app.py

### Proceso de Grabación

1. Presiona la tecla `Shift` para comenzar a grabar.
2. Mantén presionada la tecla `Shift` mientras grabas el audio.
3. Suelta la tecla `Shift` para detener la grabación.

El audio grabado será transcrito automáticamente y el texto resultante se copiará al portapapeles para su uso inmediato.
