import yfinance as yf
import pandas as pd
from pymongo import MongoClient
from pprint import pprint
import streamlit as st
import pandas as pd
import plotly.express as px
import ta
from pymongo import MongoClient
import plotly.graph_objects as go
import datetime



data = yf.download('TSLA', '2020-12-01','2021-12-01')
data.reset_index(inplace=True)
data['Date'] = data['Date'].dt.strftime('%Y-%m-%d')
#pprint( data.to_dict('records') )     



client = MongoClient()
db = client['Tesla']
collection = db['TSLA']
insert = collection.insert_many(data.to_dict('records')) 


# Création d'un DataFrame Pandas à partir des données récupérées
tesla_df = pd.DataFrame(list(collection.find()))

# Affichage des données boursières Tesla dans le dashboard Streamlit
st.write("## Données boursières Tesla")
st.write(tesla_df)



# Création d'un graphique interactif avec Plotly Express
fig = px.line(tesla_df, x="Date", y="Close", title="Prix de clôture de Tesla")

# Ajout de fonctionnalités d'interaction au graphique
fig.update_xaxes(rangeslider_visible=True)
fig.update_layout(transition_duration=500)

# Affichage du graphique dans le dashboard Streamlit
st.plotly_chart(fig)




# Charger les données boursières Tesla depuis MongoDB
@st.cache
def get_data():
    
    return tesla_df

# Fonction pour filtrer les données en fonction des critères sélectionnés
def filter_data(data, start_date, end_date, min_volume, max_volume, low, high):
    data['Date'] = pd.to_datetime(data['Date'], format="%Y/%m/%d")
    filtered_data = data[(data['Date'] >= pd.to_datetime(start_date)) & (data['Date'] <=  pd.to_datetime(end_date)) & 
                         (data['Volume'] >= min_volume) & (data['Volume'] <= max_volume) &
                         (data['Low'] >= low) & (data['High'] <= high)]
    return filtered_data

# Afficher les données boursières Tesla filtrées en fonction des critères sélectionnés
def display_filtered_data():
    data = get_data()
    st.sidebar.header("Filtres")
    data['Date'] = pd.to_datetime(data['Date'], format="%Y/%m/%d")
    start_date = st.sidebar.date_input("Date de début", data['Date'].min())
    end_date = st.sidebar.date_input("Date de fin", data['Date'].max())
    min_volume = st.sidebar.number_input("Volume minimum", min_value=0, max_value=data['Volume'].max())
    max_volume = st.sidebar.number_input("Volume maximum", min_value=0, max_value=data['Volume'].max(), value=data['Volume'].max())
    min_variation = st.sidebar.number_input("Variation minimum", min_value=data['Low'].min(), max_value=data['High'].max(), value=data['Low'].min())
    max_variation = st.sidebar.number_input("Variation maximum", min_value=data['Low'].min(), max_value=data['High'].max(), value=data['High'].max())
    filtered_data = filter_data(data, start_date, end_date, min_volume, max_volume, min_variation, max_variation)
    st.dataframe(filtered_data)

display_filtered_data()


# Obtenir la liste des champs dans la collection
fields = collection.find_one().keys()

# Demander à l'utilisateur de sélectionner les champs à afficher
selected_fields = st.multiselect('Sélectionner les champs à afficher', list(fields))

# Demander à l'utilisateur de sélectionner les critères de filtrage
# date_min = st.date_input('Date minimale', value=pd.to_datetime(collection.find_one()['Date'],format="%Y/%m/%d" ))

# date_max = st.date_input('Date maximale', value=datetime.datetime.today().date())


# Filtrer les données en fonction des critères de l'utilisateur
# query = {
   #  'date': {
  #       '$gte': date_min,
   #     '$lte': date_max
   #  }
# }
data = list(collection.find( projection={field: 1 for field in selected_fields}))

# Afficher les données dans un tableau
st.write(pd.DataFrame(data))


