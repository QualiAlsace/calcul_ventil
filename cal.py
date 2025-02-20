import streamlit as st

def calculer_puissance_chauffe(debit_air, delta_T):
    return 0.34 * debit_air * delta_T / 1000  # Conversion en kW

def calculer_debit_insufflation(debit_extraction, ratio_compensation=0.75):
    return debit_extraction * ratio_compensation

def calculer_debit_volume(surface, hauteur, renouvellement_horaire):
    return surface * hauteur * renouvellement_horaire

def calculer_pertes_thermiques(surface, isolation_coeff):
    return surface * isolation_coeff  # Approximation des pertes thermiques en kW

def main():
    st.title("Calculateur Professionnel de Ventilation et Insufflation d'Air Chaud")
    
    st.header("1. Calcul du débit d'insufflation")
    debit_extraction = st.number_input("Débit d'extraction de la hotte (m³/h)", min_value=0.0, step=10.0)
    ratio_compensation = st.slider("Ratio de compensation (%)", min_value=50, max_value=100, value=75, step=5) / 100
    
    st.header("2. Définition des caractéristiques de la pièce")
    surface = st.number_input("Surface de la pièce (m²)", min_value=0.0, step=1.0)
    hauteur = st.number_input("Hauteur sous plafond (m)", min_value=0.0, step=0.1)
    renouvellement_horaire = st.slider("Renouvellements d'air par heure", min_value=10, max_value=40, value=25, step=1)
    isolation_coeff = st.slider("Coefficient d'isolation thermique (W/m²K)", min_value=0.1, max_value=5.0, value=1.5, step=0.1)
    
    debit_volume = calculer_debit_volume(surface, hauteur, renouvellement_horaire)
    pertes_thermiques = calculer_pertes_thermiques(surface, isolation_coeff)
    
    if debit_extraction:
        debit_insufflation = max(calculer_debit_insufflation(debit_extraction, ratio_compensation), debit_volume)
        st.write(f"\nDébit d'insufflation recommandé : **{debit_insufflation:.2f} m³/h**")
    
    st.header("3. Calcul de la puissance de chauffe")
    delta_T = st.number_input("Différence de température souhaitée (ΔT en °C)", min_value=0.0, step=1.0)
    
    if debit_insufflation and delta_T:
        puissance_chauffe = calculer_puissance_chauffe(debit_insufflation, delta_T) + pertes_thermiques
        st.write(f"\nPuissance de chauffe nécessaire (avec pertes thermiques) : **{puissance_chauffe:.2f} kW**")
    
    st.header("4. Choix du type de chauffage")
    type_chauffage = st.selectbox("Type de chauffage", ["Électrique", "Eau chaude", "Gaz"])
    
    if type_chauffage:
        st.write(f"\nSolution recommandée : **Caisson d'insufflation {type_chauffage}** avec **{debit_insufflation:.2f} m³/h** et **{puissance_chauffe:.2f} kW**")
    
    st.header("5. Résumé et conseils")
    st.write("- Assurez-vous que l'insufflation est bien répartie dans la pièce.")
    st.write("- Vérifiez les pertes thermiques pour adapter la puissance de chauffe.")
    st.write("- Privilégiez un caisson avec régulation pour optimiser la consommation énergétique.")
    
if __name__ == "__main__":
    main()
