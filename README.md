# Projet-PYTHON
Projet python

Ce projet consiste à faire du web scraping. 
Mon code récupère des données boursières Tesla à partir de l'API Yahoo Finance, les stocke dans une base de données MongoDB, et affiche ces données dans un dashboard Streamlit. Les fonctionnalités offertes par ce dashboard comprennent :

    L'affichage des données boursières Tesla dans un tableau
    La création d'un graphique interactif avec Plotly Express, permettant d'explorer les prix de clôture de Tesla sur une période donnée.
    La possibilité de filtrer les données en fonction de critères tels que la date, le volume, le prix minimum et maximum, etc. 
    
    
    Prérequis

    Avoir installé les librairies yfinance, pandas, pymongo, pprint, streamlit, plotly.express, ta, et plotly.graph_objects.
    Avoir une base de données MongoDB et les informations de connexion correspondantes.
    
    
    Utilisation

    Récupérez les données boursières Tesla en exécutant la ligne suivante :

    data = yf.download('TSLA', '2020-12-01','2021-12-01')
    Stockez ces données dans une collection MongoDB
    Exécutez le script dans un environnement Streamlit pour visualiser les données : streamlit run script.py
    Utilisez le dashboard Streamlit pour explorer les données et filtrer les résultats en fonction de vos critères.
    
    Notes

    Les données récupérées de Yahoo Finance peuvent être différentes selon la date d'exécution du script. Veuillez adapter les dates de récupération des données ('2020-12-01' et '2021-12-01') à votre convenance.
    Ce code ne fournit qu'un exemple simple de visualisation de données boursières Tesla. Il peut être adapté à d'autres sources de données ou d'autres critères de filtrage en fonction de vos besoins.
