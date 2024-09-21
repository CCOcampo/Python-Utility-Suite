import os
from PIL import Image
from rembg import remove
import streamlit as st

def save_uploaded_file(uploadedfile):
    upload_dir = 'Imagenes_Procesadas'
    if not os.path.exists(upload_dir):
        os.makedirs(upload_dir)
    filepath = os.path.join(upload_dir, uploadedfile.name)
    with open(filepath, 'wb') as f:
        f.write(uploadedfile.getbuffer())
    return  filepath

def run_background_remover(input_img):
    input_img = save_uploaded_file(input_img)
    output_img = input_img.replace('.','_rmbg.').replace('jpg','png').replace('jpeg','png')
    try:
        image = Image.open(input_img)
        output = remove(image)
        output.save(output_img, 'PNG')

        col1, col2 = st.columns(2)
        with col1:
            st.header("Antes")
            st.image(input_img, caption='Imagen Original')
            with open(input_img, "rb") as file:
                st.download_button(label="Descargar imagen original", 
                                   data=file, 
                                   file_name= os.path.basename(input_img),
                                   mime='image/jpeg'
                                   )
        
        with col2:
            st.header("Despues")
            st.image(output_img, caption='Imagen con fondo removido')
            with open(input_img, "rb") as file:
                st.download_button(label="Descargar imagen procesada", 
                                   data=file, 
                                   file_name= os.path.basename(input_img),
                                   mime='image/jpeg'
                                   )
                
        st.success('Imagen procesada con éxito')
    
    except Exception as e:
        st.error('Error al procesar la imagen')
        st.error(e)

def main():
    st.title('Remover Fondo de Imágenes')
    save_uploaded_file = st.file_uploader("Subir imagen", type=['jpg','jpeg','png'])
    if save_uploaded_file is not None:
        run_background_remover(save_uploaded_file)

if __name__ == '__main__':
    main()