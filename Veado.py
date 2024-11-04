from pathlib import Path

import streamlit as st

dir_path = Path(__file__).parent

def deer_page():
    st.set_page_config(
        page_title="Análise das migrações do veado-vermelho",
        page_icon=":deer", 
        initial_sidebar_state="collapsed"
    )

    st.title("Veado-vermelho 🦌")
    st.image(str(dir_path / "images/female_red_deer.jpg"))
    st.write("O veado-vermelho ou cervo-vermelho (Cervus elaphus) é uma\
             espécie de veado de grande porte do hemisfério norte,\
             distribuído pela Europa, Ásia e Norte da África. A espécie foi\
             também introduzida em várias regiões do mundo.")
    st.write("Um estudo analisou o comportamento de 13 veados da cordilheira\
             dos Apeninos do Norte na Itália, entre 2011 e 2017 e apresentou\
             os seguintes resultados:")
    st.markdown("- Os veados vermelhos exibiram duas estratégias coexistentes\
                , ou seja, migratória e estacionária.")
    st.markdown("- Na amostra, as fêmeas tenderam a migrar mais que os machos")
    st.markdown("- Foi encontrado um alto nível de variabilidade\
                 interindividual na data de migração/retorno, enquanto cada\
                 cervo migratório foi muito conservador durante o período de\
                estudo.")
    st.markdown("- As faixas de migração foram em média 12 ± 4,2 km da área\
                 de residência.")
    st.markdown("- Tanto os cervos migratórios quanto os residentes exibiram\
                 alta fidelidade ao local. Nenhuma mudança da estratégia\
                 migratória para estacionária foi observada em nenhum cervo\
                 durante o período do estudo. No entanto, o período poderia\
                 ter sido demasiado curto para detectar qualquer mudança.")
    st.write("O presente projeto, visa simular a rota de veados vermelhos \
             fêmeas da região de Alberta no Canadá em seu período migratório\
             e como essa rota se altera ao longo do tempo em relação às\
             mudanças climáticas.")

if __name__ == "__main__":
   deer_page()