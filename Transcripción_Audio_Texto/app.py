import tempfile
import os
import wave
import pyaudio
import keyboard 
import pyautogui
import pyperclip    
from groq import Groq
from Key import Api_Key

client = Groq(api_key=Api_Key)

def Audio(frecuencia_muestreo=1600,canales=1,fragmento=2048):
    p = pyaudio.PyAudio()
    stream = p.open(
        format=pyaudio.paInt16,
        channels=canales,
        rate=frecuencia_muestreo,
        input=True,
        frames_per_buffer=fragmento)
    print("Presiona 'shift' para empezar la grabación...")
    frames = []
    keyboard.wait('shift')
    print("Grabación... Suelta la tecla 'shift' para detener")
    while keyboard.is_pressed('shift'):
        data = stream.read(fragmento)
        frames.append(data)
    print("Grabación detenida")
    stream.stop_stream()
    stream.close()
    p.terminate()
    return  frames, frecuencia_muestreo

def GuardarAudio(frames, frecuencia_muestreo):
    with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as tmpfile:
        wf = wave.open(tmpfile.name, 'wb')
        wf.setnchannels(1)
        wf.setsampwidth(pyaudio.PyAudio().get_sample_size(pyaudio.paInt16))
        wf.setframerate(frecuencia_muestreo)
        wf.writeframes(b''.join(frames))
        wf.close()
        return tmpfile.name
    
def transcribir_audio(ruta):
    try:
        with open(ruta, 'rb') as archivo:
            transcripcion = client.audio.transcriptions.create(
                file=(os.path.basename(ruta), archivo.read()),
                model='whisper-large-v3',
                prompt='El audio es de una persona realizando actividades generales',
                response_format='text',
                language='es'
            )
        return transcripcion
    except Exception as e:
        print(f'Ocurrió un error: {e}')
        return None
    
def copiar_transcripcion_porta_papeles(text):
    if text:
        pyperclip.copy(text)
        pyautogui.hotkey('command', 'v')
    else:
        print("El texto está vacío y no se puede copiar.")

def main():
    while True:
        frames, frecuencia_muestreo = Audio()
        audio_temporal = GuardarAudio(frames, frecuencia_muestreo)
        print("Transcribiendo...")
        transcripcion = transcribir_audio(audio_temporal)
        if transcripcion:
            print('\nTranscribiendo')
            print('copiando transcripción al portapapeles')
            copiar_transcripcion_porta_papeles(transcripcion)
            print('transcripción copiada al portapapeles y pegada a la app')
        else:
            print('transcripción fallo')

        os.unlink(audio_temporal)
        print('Proxima grabación: presiona "fn" para iniciar')
if __name__ == '__main__':
    main()


