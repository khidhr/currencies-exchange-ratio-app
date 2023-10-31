import streamlit as st
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Taux de change entre devises", page_icon=":bar_chart:")

st.title(":bar_chart: TP 2: Finance de Marché")
st.subheader('Réalisé par : Halab Khidhr & Marzoug Nabil')
st.write("Sélectionnez les devises de base et cibles pour comparer leurs variations de taux de change.")

currencies = ["MAD","USD", "EUR", "GBP", "JPY", "AUD", "CAD", "CHF", "CNY", "INR", "MXN"]  # Add more currencies as needed

base_currency = st.selectbox("Selectionnez le devise de base: ", currencies)
target_currency = st.selectbox("Selectionnez le devise cible: ", currencies)

days = st.slider("Select Number of Days", min_value=1, max_value=30, value=7)

def get_exchange_rates(base_currency, target_currency, days):
    ticker = f"{base_currency}{target_currency}=X"
    data = yf.download(ticker, period=f"{days}d")
    return data['Close']

if base_currency and target_currency:
    try:
        exchange_rate_data = get_exchange_rates(base_currency, target_currency, days)
        
        plt.figure(figsize=(10, 6))
        plt.plot(exchange_rate_data.index, exchange_rate_data, marker='o', color='b', label=f'{base_currency}-{target_currency} Exchange Rate')
        plt.xlabel("Date")
        plt.ylabel(f"Taux de change: ({base_currency}-{target_currency})")
        plt.title(f"Taux de change entre: {base_currency}-{target_currency}")
        plt.xticks(rotation=45)
        plt.legend()
        st.pyplot(plt)

        # Display raw data
        st.write("Les données du taux de change:", exchange_rate_data)

    except Exception as e:
        st.write("Erreur, pas de données pour le devise selectionné!")
