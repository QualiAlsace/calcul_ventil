import streamlit as st

def calculer_debit_extraction(surface, hauteur, renouvellement_horaire):
    return surface * hauteur * renouvellement_horaire

def calculer_puissance_ventilateur(debit_air, perte_charge, rendement):
    return round((debit_air * perte_charge) / (3600 * rendement), 2)  # Puissance en kW

def main():
    st.title("Calculateur Professionnel de Caisson d'Extraction VMC")
    
    st.header("1. Définition du type de local")
    type_local = st.selectbox("Type de bâtiment", [
        ("Bureaux, salles de réunion (4-8 vol/h)", 6),
        ("Commerces, boutiques (6-10 vol/h)", 8),
        ("Restaurants - salle (8-12 vol/h)", 10),
        ("Cuisines professionnelles (20-40 vol/h)", 25),
        ("Salles de sport (10-20 vol/h)", 15),
        ("Laboratoires, salles propres (15-30 vol/h)", 20),
        ("Locaux industriels, entrepôts (5-20 vol/h)", 10),
        ("Sanitaires publics (6-15 vol/h)", 8)
    ], format_func=lambda x: x[0])
    renouvellement_horaire = type_local[1]
    
    st.header("2. Définition des caractéristiques de la pièce")
    surface = st.number_input("Surface du local (m²)", min_value=0.0, step=1.0)
    hauteur = st.number_input("Hauteur sous plafond (m)", min_value=0.0, step=0.1)
    
    debit_extraction = calculer_debit_extraction(surface, hauteur, renouvellement_horaire)
    
    if surface and hauteur:
        st.write(f"🔹 Débit d'extraction recommandé : **{debit_extraction:.1f} m³/h**")
    
    st.header("3. Calcul de la puissance du ventilateur")
    perte_charge = st.number_input("Perte de charge du réseau aéraulique (Pa)", min_value=0.0, step=5.0, value=100.0)
    rendement = st.slider("Rendement du ventilateur (%)", min_value=50, max_value=100, value=85, step=1) / 100
    
    if debit_extraction and perte_charge and rendement:
        puissance_ventilateur = calculer_puissance_ventilateur(debit_extraction, perte_charge, rendement)
        st.write(f"⚡ Puissance du ventilateur requise : **{puissance_ventilateur:.2f} kW**")
    
    st.header("4. Sélection du type de ventilateur")
    type_ventilateur = st.selectbox("Type de ventilateur", ["Centrifuge", "Axial", "Hélicoïde"])
    
    st.write(f"✅ Solution recommandée : **Ventilateur {type_ventilateur}** avec **{debit_extraction:.1f} m³/h** et **{puissance_ventilateur:.2f} kW**")
    
    st.header("5. Conseils et recommandations")
    st.write("✔ Vérifiez les pertes de charge du réseau aéraulique pour un bon dimensionnement.")
    st.write("✔ Choisissez un ventilateur avec un bon rendement énergétique pour réduire la consommation.")
    st.write("✔ Utilisez des gaines adaptées pour éviter des pertes de pression excessives.")
    
if __name__ == "__main__":
    main()
