import pandas as pd
import streamlit as st
import joblib
import plotly.express as px

# Load the trained model
model = joblib.load('random_forest_model.pkl')

# Map cbwd to numerical values
cbwd_mapping = {'NW': 0, 'SW': 1, 'NE': 2, 'SE': 3}

# Función para predecir PM2.5
def predict_pm25(input_df):
    # Map cbwd to numerical values
    input_df['cbwd'] = input_df['cbwd'].map(cbwd_mapping)

    # Ensure the input DataFrame has the same columns as the training data
    expected_columns = ['year', 'month', 'day', 'hour', 'DEWP', 'TEMP', 'PRES', 'cbwd', 'Iws', 'Is', 'Ir']
    for col in expected_columns:
        if col not in input_df.columns:
            input_df[col] = 0

    input_df = input_df[expected_columns]

    # Predict PM2.5
    predictions = model.predict(input_df)
    input_df['PM2.5'] = predictions
    return input_df

st.header('Predicción de polución (pm2.5)')

st.subheader('Fecha y Hora')
col1, col2, col3, col4 = st.columns(4)
with col1:
    year = st.number_input('Year', min_value=2000, max_value=2030, value=2024)
with col2:
    month = st.number_input('Month', min_value=1, max_value=12, value=9)
with col3:
    day = st.number_input('Day', min_value=1, max_value=31, value=20)
with col4:
    hour = st.number_input('Hour', min_value=0, max_value=24, value=1)

st.subheader('Condiciones Climáticas')
col1, col2, col3 = st.columns(3)
with col1:
    DEWP = st.number_input('Dew Point (DEWP)', value=-21.0)
with col2:
    TEMP = st.number_input('Temperature (TEMP)', value=-11.0)
with col3:
    PRES = st.number_input('Pressure (PRES)', value=1021.0)


col1, col2 = st.columns(2)
with col1:
    cbwd = st.selectbox('Combined Wind Direction (cbwd)', ['NW', 'SW', 'NE', 'SE'])
with col2:
    Iws = st.number_input('Cumulated Wind Speed (Iws)', value=1.79)

st.subheader('Precipitaciones')
col1, col2  = st.columns(2)
with col1:
    Is = st.number_input('Cumulated Hours of Snow (Is)', value=0)
with col2:
    Ir = st.number_input('Cumulated Hours of Rain (Ir)', value=0)

# Crear un DataFrame para la entrada manual
if not (1 <= day <= 31):
    st.error('Day must be between 1 and 31')
elif not (0 <= hour <= 24):
    st.error('Hour must be between 0 and 24')
elif not (1 <= month <= 12):
    st.error('Month must be between 1 and 12')
elif not (2000 <= year <= 2100):
    st.error('Year must be between 2000 and 2030')
else:
    input_data = pd.DataFrame({
        'year': [year],
        'month': [month],
        'day': [day],
        'hour': [hour],
        'DEWP': [DEWP],
        'TEMP': [TEMP],
        'PRES': [PRES],
        'cbwd': [cbwd],
        'Iws': [Iws],
        'Is': [Is],
        'Ir': [Ir]
    })

# Predecir PM2.5 para la entrada manual
if st.button('Predict PM2.5'):
    prediction_df = predict_pm25(input_data)
    st.write(f'Predicted PM2.5: {prediction_df["PM2.5"].iloc[0]}')

# Widget para cargar archivo Excel
st.header('Cargar Archivo Excel')
uploaded_file = st.file_uploader("Choose an Excel file", type="xlsx")

if uploaded_file is not None:
    # Leer el archivo Excel
    df = pd.read_excel(uploaded_file)

    # Predecir PM2.5 para cada fila del archivo
    prediction_df = predict_pm25(df)

    # Mostrar el DataFrame resultante
    st.write(prediction_df)

    # Mostrar la gráfica dinámica de la frecuencia de los datos
    st.subheader("Frecuencia de PM2.5 estimados")
    fig = px.histogram(prediction_df, x='PM2.5', title="Distribución de PM2.5")
    st.plotly_chart(fig)

    # Exportar el DataFrame resultante a un archivo Excel
    output_file = 'predicted_pm25.xlsx'
    prediction_df.to_excel(output_file, index=False)

    # Proveer un enlace para descargar el archivo
    st.download_button(
        label="Download Excel file",
        data=open(output_file, 'rb').read(),
        file_name=output_file,
        mime='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    )