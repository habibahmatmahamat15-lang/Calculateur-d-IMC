# --- IMC ---
import streamlit as st

st.header(":green[CALCULATEUR D'IMC]")

c1, c2 = st.columns(2)
with c1:
    st.image("imc.jpeg")
    poids = st.number_input("Entrez votre poids (kg) :")
    taille = st.number_input("Entrez votre taille (m) :")
    imc = poids / (taille ** 2)
    st.write(f"Votre IMC est {imc:.2f}")
    
   # if poids > 0 and taille > 0:
    if st.button("Calculer"):
           # imc = poids / (taille ** 2)
        #st.write(f"Votre IMC est **{imc:.2f}**")

        # Interprétation
        if imc < 18.5:
            st.warning("Vous êtes en insuffisance pondérale.")
        elif 18.5 <= imc <= 24.9:
            st.success("Vous avez une corpulence normale.")
        elif 25 <= imc <= 29.9:
            st.info("Vous êtes en surpoids.")
        else:
            st.error("Vous êtes en obésité.")

with c2:
    st.subheader("CONSEILS DE SANTE")

    if imc < 18.5:
        st.info("""
        -Mangez plus de repas riches en calories  
        -Privilégiez les protéines (poissons, viandes, légumineuses)  
        -Consultez un nutritionniste pour un suivi adapté  
        -Évitez le stress et dormez suffisamment  
            """)
    elif 18.5 <= imc <= 24.9:
        st.success("""
        Continuez vos bonnes habitudes :  
        - Maintenez une alimentation équilibrée  
        - Faites du sport régulièrement  
        - Surveillez votre poids chaque mois  
        - Buvez beaucoup d’eau  
            """)
    elif 25 <= imc <= 29.9:
        st.warning("""
        Conseils :  
        - Réduisez la consommation de sucre et d’aliments gras  
        - Marchez au moins 30 minutes par jour  
        - Privilégiez les fruits et légumes  
        - Consultez un médecin si le surpoids persiste  
            """)
    else:
        st.error("""
        Conseils importants :  
        - Consultez un médecin pour un suivi médical  
        - Adoptez une alimentation saine et contrôlée  
        - Pratiquez une activité physique adaptée  
        - Surveillez régulièrement votre tension et glycémie  
            """)
       