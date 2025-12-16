import streamlit as st

st.header(":green[CALCULATEUR D'IMC]")

c1, c2 = st.columns(2)

IMC = None  # ✅ Initialisation

with c1:
    st.image("imc.jpeg")
    poids = st.number_input("Entrez votre poids (kg) :", min_value=0.0)
    taille = st.number_input("Entrez votre taille (m) :", min_value=0.0)

    if poids > 0 and taille > 0:
        if st.button("Calculer"):
            IMC = poids / (taille ** 2)
            st.write(f"Votre IMC est **{IMC:.2f}**")

            # Interprétation
            if IMC < 18.5:
                st.warning("Vous êtes en insuffisance pondérale.")
            elif IMC < 25:
                st.success("Vous avez une corpulence normale.")
            elif IMC < 30:
                st.info("Vous êtes en surpoids.")
            else:
                st.error("Vous êtes en situation d’obésité.")

with c2:
    st.subheader("CONSEILS DE SANTÉ")

    if IMC is not None:  # ✅ Vérification propre
        if IMC < 18.5:
            st.info("""
- Mangez des repas riches en calories  
- Privilégiez les protéines  
- Consultez un nutritionniste  
- Dormez suffisamment  
            """)
        elif IMC < 25:
            st.success("""
- Continuez une alimentation équilibrée  
- Faites du sport régulièrement  
- Hydratez-vous bien  
            """)
        elif IMC < 30:
            st.warning("""
- Réduisez sucres et graisses  
- Marchez 30 minutes par jour  
- Mangez plus de fruits et légumes  
            """)
        else:
            st.error("""
- Consultez un médecin  
- Activité physique adaptée  
- Suivi médical régulier  
            """)
