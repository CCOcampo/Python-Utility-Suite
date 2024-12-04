import streamlit as st
import pandas as pd
from utilities import nth_letter_word

if "dictionary" not in st.session_state:
    st.session_state["dictionary"] = {}

st.markdown(
    """
    <style>
    .appview-container {
        zoom: 1.3;
    }
    .stColumn {
        padding: 20px;
    }
    .stSubheader {
        font-size: 30px;  /* Increase the font size of the subheader */
        font-weight: bold;
        color: #333;  /* Optional: change color for better visibility */
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.title("Dictionary, Costs, and Word Management")

st.markdown("### Upload Database")
uploaded_file = st.file_uploader("Upload a CSV file with format: Product, Description, Price", type="csv")

if uploaded_file is not None:
    try:
        df = pd.read_csv(uploaded_file, header=None, names=["Product", "Description", "Price"])
        if df.shape[1] == 3:
            for _, row in df.iterrows():
                product = row["Product"]
                description = row["Description"]
                try:
                    price = float(row["Price"])
                    st.session_state["dictionary"][product] = {
                        "definition": description,
                        "price": price,
                    }
                except ValueError:
                    st.error(f"Error with the price of the product '{product}', it must be a numeric value.")
            st.success("Database uploaded successfully.")
        else:
            st.error("The CSV file must have exactly 3 columns: Product, Description, Price.")
    except Exception as e:
        st.error(f"Error processing the file: {e}")

st.markdown("### Add New Entry to Dictionary")
col1, col2, col3 = st.columns(3, gap="large") 

with col1:
    word = st.text_input("Word:", placeholder="Enter a word")
with col2:
    definition = st.text_input("Definition:", placeholder="Enter the definition")
with col3:
    price = st.number_input("Price ($):", min_value=0.0, step=0.01)

if st.button("Add to dictionary"):
    if word and definition and price >= 0:
        st.session_state["dictionary"][word] = {"definition": definition, "price": price}
        st.success(f"'{word}' was added with the definition '{definition}' and price ${price:.2f}")
    else:
        st.error("Please complete all fields correctly.")

st.markdown("--")
col1, col2, col3 = st.columns(3, gap="large")

with col1:
    st.subheader("Dictionary")
    if st.session_state["dictionary"]:
        for word, data in st.session_state["dictionary"].items():
            st.write(f"**{word}**: {data['definition']} (${data['price']:.2f})")
    else:
        st.info("The dictionary is empty. Add new words above.")

with col2:
    st.subheader("Cost Calculation")
    if st.session_state["dictionary"]:
        selected_items = st.multiselect(
            "Select products:",
            options=list(st.session_state["dictionary"].keys()),
        )

        if selected_items:
            quantities = {}
            for item in selected_items:
                quantity = st.number_input(f"Quantity of {item}:", min_value=0, step=1, key=f"quantity_{item}")
                if quantity > 0:
                    quantities[item] = quantity

            tax_rate = st.number_input("Tax rate (%):", min_value=0.0, step=0.1, value=10.0)

            if st.button("Calculate total cost"):
                if quantities:
                    subtotal = sum(
                        st.session_state["dictionary"][item]["price"] * qty for item, qty in quantities.items()
                    )
                    tax = (tax_rate / 100) * subtotal
                    total = subtotal + tax
                    st.write(f"**Subtotal:** ${subtotal:.2f}")
                    st.write(f"**Tax ({tax_rate}%):** ${tax:.2f}")
                    st.write(f"**Total cost:** ${total:.2f}")
                else:
                    st.info("Select at least one product with a quantity greater than 0.")
        else:
            st.info("Select products to include in the calculation.")
    else:
        st.info("The dictionary is empty. Add new words above.")

with col3:
    st.subheader("Generate Words")
    words_input = st.text_area("Enter words separated by commas:")
    if st.button("Create word"):
        if words_input:
            word_list = [word.strip() for word in words_input.split(",")]
            new_word = nth_letter_word(word_list)
            if new_word:
                st.success(f"Generated word: {new_word}")
            else:
                st.error("Could not generate a new word.")
        else:
            st.error("Enter words to generate a new word.")