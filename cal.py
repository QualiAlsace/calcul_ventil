import streamlit as st

def calculer_puissance_chauffe(debit_air, delta_T):
    return round(0.34 * debit_air * delta_T / 1000, 1)  # Conversion en kW et arrondi

def calculer_debit_insufflation(debit_extraction, ratio_compensation=0.75):
    return debit_extraction * ratio_compensation

def calculer_debit_volume(surface, hauteur, renouvellement_horaire):
    return surface * hauteur * renouvellement_horaire

def calculer_pertes_thermiques(U, surface, hauteur, delta_T):
    return round(U * surface * hauteur * delta_T / 1000, 1)  # Conversion en kW et arrondi

def main():
    st.title("Calculateur Professionnel de Ventilation et Insufflation d'Air Chaud")
    
    st.header("1. Calcul du débit d'insufflation")
    debit_extraction = st.number_input("Débit d'extraction de la hotte (m³/h)", min_value=0.0, step=10.0)
    ratio_compensation = st.slider("Ratio de compensation (%)", min_value=50, max_value=100, value=75, step=5) / 100
    
    st.header("2. Définition des caractéristiques de la pièce")
    surface = st.number_input("Surface de la pièce (m²)", min_value=0.0, step=1.0)
    hauteur = st.number_input("Hauteur sous plafond (m)", min_value=0.0, step=0.1)
    renouvellement_horaire = st.selectbox("Renouvellement d'air (vol/h)", [6, 8, 10, 12, 15, 20, 25, 30, 35, 40])
    
    U = st.selectbox("Niveau d'isolation du bâtiment", [
        ("Très bien isolé (RT 2020)", 0.3),
        ("Isolation standard (RT 2012)", 0.8),
        ("Mal isolé (ancien bâtiment)", 2.0),
        ("Pas isolé (tôle, hangar)", 4.0)
    ], format_func=lambda x: x[0])[1]
    
    debit_volume = calculer_debit_volume(surface, hauteur, renouvellement_horaire)
    
    if debit_extraction:
        debit_insufflation = max(calculer_debit_insufflation(debit_extraction, ratio_compensation), debit_volume)
        st.write(f"\n🔹 Débit d'insufflation recommandé : **{debit_insufflation:.1f} m³/h**")
    
    st.header("3. Calcul de la puissance de chauffe")
    delta_T = st.number_input("Différence de température souhaitée (ΔT en °C)", min_value=0.0, step=1.0)
    
    if debit_insufflation and delta_T:
        pertes_thermiques = calculer_pertes_thermiques(U, surface, hauteur, delta_T)
        puissance_chauffe = calculer_puissance_chauffe(debit_insufflation, delta_T) + pertes_thermiques
        st.write(f"\n🔥 Puissance de chauffe nécessaire (avec pertes thermiques) : **{puissance_chauffe:.1f} kW**")
    
    st.header("4. Choix du type de chauffage")
    type_chauffage = st.selectbox("Type de chauffage", ["Électrique", "Eau chaude", "Gaz"])
    
    if type_chauffage:
        st.write(f"\n✅ Solution recommandée : **Caisson d'insufflation {type_chauffage}** avec **{debit_insufflation:.1f} m³/h** et **{puissance_chauffe:.1f} kW**")
    
    st.header("5. Résumé et conseils")
    st.write("✔ Sélectionnez un bon taux de renouvellement d'air selon le type de local.")
    st.write("✔ Vérifiez les pertes thermiques du bâtiment pour éviter une sous-estimation.")
    st.write("✔ Utilisez un caisson avec régulation pour optimiser la consommation énergétique.")
    
if __name__ == "__main__":
    main()
