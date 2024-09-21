import streamlit as st
from faker import Faker
import pandas as pd
from io import BytesIO

fake = Faker('es_CO')
available_fields = {
    'Nombre': fake.first_name,
    'Apellido': fake.last_name,
    'Dirección': fake.address,
    'Correo Electronico': fake.email,
    'Teléfono': fake.phone_number,
    'Empresa': fake.company,
    'Fecha': fake.date,
    'Tarjeta de Crédito': fake.credit_card_number,
    'Placa de Auto': fake.license_plate,
    'Profesión': fake.job,
}

def generate_fake_data(fields, num_row):
    data = {field: [func() for _ in range(num_row)] for field, func in fields.items()}
    return pd.DataFrame(data)

st.title('Generador de Datos Falsos')
st.write('Este es un generador de datos falsos para pruebas de concepto.')
st.write('Selecciona los campos que deseas generar y la cantidad de filas.')

selected_fields = st.multiselect('Campos', 
                                 options = list(available_fields.keys()), 
                                 default=list(available_fields.keys())
                                 )
num_row = st.number_input('Número de filas', 
                          min_value=1, 
                          max_value=1000000,
                          value=100)

if st.button('Generar datos'):
    selected_funcs = {field: available_fields[field] for field in selected_fields}
    df = generate_fake_data(selected_funcs, num_row)
    output = BytesIO()
    with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
        writer.book.use_constant_memory = True
        df.to_excel(writer, index=False)
    output.seek(0)

    st.success('Datos generados')
    st.write(df)
    
    st.download_button(label='Descargar archivo',
                            data=output,
                            file_name='fake_data.xlsx',
                            mime='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')