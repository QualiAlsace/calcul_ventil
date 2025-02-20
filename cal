import streamlit as st

def calculer_puissance_chauffe(debit_air, delta_T):
    return 0.34 * debit_air * delta_T

def calculer_debit_insufflation(debit_extraction, ratio_compensation=0.75):
    return debit_extraction * ratio_compensation

def main():
    st.title("Calculateur de Ventilation et Insufflation d'Air Chaud")
    
    st.header("1. Calcul du débit d'insufflation")
    debit_extraction = st.number_input("Débit d'extraction de la hotte (m³/h)", min_value=0.0, step=10.0)
    ratio_compensation = st.slider("Ratio de compensation (%)", min_value=50, max_value=100, value=75, step=5) / 100
    
    if debit_extraction:
        debit_insufflation = calculer_debit_insufflation(debit_extraction, ratio_compensation)
        st.write(f"\nDébit d'insufflation recommandé : **{debit_insufflation:.2f} m³/h**")
    
    st.header("2. Calcul de la puissance de chauffe")
    delta_T = st.number_input("Différence de température souhaitée (ΔT en °C)", min_value=0.0, step=1.0)
    
    if debit_insufflation and delta_T:
        puissance_chauffe = calculer_puissance_chauffe(debit_insufflation, delta_T)
        st.write(f"\nPuissance de chauffe nécessaire : **{puissance_chauffe:.2f} kW**")
    
    st.header("3. Choix du type de chauffage")
    type_chauffage = st.selectbox("Type de chauffage", ["Électrique", "Eau chaude", "Gaz"])
    
    if type_chauffage:
        st.write(f"\nSolution recommandée : **Caisson d'insufflation {type_chauffage}** avec **{debit_insufflation:.2f} m³/h** et **{puissance_chauffe:.2f} kW**")

if __name__ == "__main__":
    main()
