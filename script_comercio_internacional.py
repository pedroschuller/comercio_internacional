import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.set_option('deprecation.showPyplotGlobalUse', False)
st.set_page_config(page_title="Comércio Livre e Globalização - Comércio Livre e Globalização")
st.title("Porque é que os países que trocam, crescem?")
st.header("Pós-Graduação em Pensamento Liberal - Comércio Livre e Globalização")
st.write("por Pedro Schuller")

st.write("O comércio internacional contribui para a prosperidade dos países que nele participam de várias formas.")

st.subheader("Vantagem comparativa e especialização")

st.write("A teoria das vantagens comparativa de David Ricardo destaca os benefícios da especialização no comércio internacional. Cada país tem recursos, competências e níveis de tecnologia diferentes, o que cria diferenças nos seus custos de oportunidade de produção. Ao especializarem-se na produção de bens ou serviços nos quais têm uma vantagem comparativa, os países podem afectar os seus recursos de forma mais eficiente. Este facto conduz a um aumento da produtividade, permitindo que os países produzam mais daquilo em que são melhores e troquem por bens e serviços em que são menos eficientes. Como resultado, ambos os países podem registar níveis de consumo mais elevados, uma vez que têm acesso a uma gama mais vasta de bens e serviços a custos mais baixos.")

st.write("Por exemplo, considere-se um cenário em que o país A tem um custo de oportunidade mais baixo na produção de trigo, enquanto o país B tem um custo de oportunidade mais baixo na produção de têxteis. Se ambos os países se especializarem na produção do bem em que têm uma vantagem comparativa e efectuarem trocas comerciais entre si, podem maximizar a sua produção global. O país A pode concentrar-se na produção de mais trigo e exportar o excedente, enquanto o país B pode especializar-se na produção de têxteis e exportá-los. Esta especialização permite que ambos os países beneficiem de uma maior produtividade e de um aumento das trocas comerciais, o que conduz ao crescimento económico e à prosperidade.")

def simulate_comparative_advantage(total_hours, hours_a_wheat, hours_a_textiles, hours_b_wheat, hours_b_textiles):
    # Calculate the number of units produced without trade
    units_a_no_trade_wheat = total_hours / (hours_a_wheat+hours_a_textiles)
    units_a_no_trade_textiles = units_a_no_trade_wheat
    units_b_no_trade_wheat = total_hours / (hours_b_wheat + hours_b_textiles)
    units_b_no_trade_textiles = units_b_no_trade_wheat

    units_a_trade_wheat = units_a_no_trade_wheat
    units_b_trade_wheat = units_a_no_trade_textiles
    units_a_trade_textiles = units_b_no_trade_wheat
    units_b_trade_textiles = units_b_no_trade_textiles

    # Determine the comparative advantage
    comparative_advantage_country_textiles = "No one"
    if (hours_a_wheat / hours_a_textiles) > (hours_b_wheat / hours_b_textiles):
        comparative_advantage_country_textiles = "Country A" 
        units_a_trade_wheat = 0
        units_b_trade_wheat = total_hours / hours_b_wheat
        units_a_trade_textiles = total_hours / hours_a_textiles
        units_b_trade_textiles = 0    
    if (hours_a_wheat / hours_a_textiles) < (hours_b_wheat / hours_b_textiles):
        comparative_advantage_country_textiles = "Country B"
        units_a_trade_wheat = total_hours / hours_a_wheat
        units_b_trade_wheat = 0
        units_a_trade_textiles = 0
        units_b_trade_textiles = total_hours / hours_b_textiles


    # Print the results
    st.write(f"{comparative_advantage_country_textiles} has the comparative advantage in producing textiles.")
    st.write("Production quantities without trade:")
    st.write("Country A: {:.2f} units of wheat, {:.2f} units of textiles".format(units_a_no_trade_wheat, units_a_no_trade_textiles))
    st.write("Country B: {:.2f} units of wheat, {:.2f} units of textiles".format(units_b_no_trade_wheat, units_b_no_trade_textiles))
    st.write(f"Total consumptionwithout trade: {units_a_no_trade_wheat+units_a_no_trade_textiles+units_b_no_trade_wheat+units_b_no_trade_textiles:.0f}")


    st.write("\nProduction quantities with trade (comparative advantage):")
    st.write("Country A: {:.2f} units of wheat, {:.2f} units of textiles".format(units_a_trade_wheat, units_a_trade_textiles))
    st.write("Country B: {:.2f} units of wheat, {:.2f} units of textiles".format(units_b_trade_wheat, units_b_trade_textiles))
    st.write(f"Total consumption with trade: {units_a_trade_wheat+units_a_trade_textiles+units_b_trade_wheat+units_b_trade_textiles:.0f}")
# Input the total number of hours available and the hours required by each country to produce one unit of wheat and textiles

total_hours = 1800
total_hours = st.slider('Enter the total number of hours available to work: ', 500, 2000, step = 100)

hours_a_wheat = 40
hours_a_wheat = st.slider('Enter the number of hours Country A requires to produce one unit of wheat: ', 10, 200, step = 10)
hours_a_textiles = 80
hours_a_textiles = st.slider('Enter the number of hours Country A requires to produce one unit of textiles: ', 10, 200, step = 10)
hours_b_wheat = 80
hours_b_wheat = st.slider('Enter the number of hours Country B requires to produce one unit of wheat: ', 10, 200, step = 10)
hours_b_textiles = 40
hours_b_textiles = st.slider('Enter the number of hours Country B requires to produce one unit of textiles: ', 10, 200, step = 10)


# Simulate and display the results
simulate_comparative_advantage(total_hours, hours_a_wheat, hours_a_textiles, hours_b_wheat, hours_b_textiles)


st.subheader("Dotação de factores e ganhos de produtividade")

st.write("A teoria da dotação de factores de Heckscher-Ohlin sugere que os países tendem a especializar-se na produção de bens que utilizam intensivamente os factores de produção que possuem em abundância. Esta especialização conduz a ganhos de produtividade e a um aumento dos salários dos factores de produção.")

st.write("Por exemplo, um país rico em recursos naturais, como o petróleo ou os minerais, pode especializar-se na extracção e exportação desses recursos. Esta especialização permite ao país tirar partido da sua dotação de recursos e gerar receitas de exportação. O rendimento gerado pelas exportações de recursos pode ser investido noutros sectores, como a educação, as infra-estruturas ou a tecnologia, o que leva ao desenvolvimento de outras indústrias e à diversificação da economia. Como resultado, o país regista um aumento da produtividade e dos salários dos seus trabalhadores, contribuindo para a prosperidade geral.")

st.subheader("Concorrência, inovação e economias de escala")

st.write("O comércio internacional fomenta a concorrência entre empresas nacionais e estrangeiras, o que pode levar a um aumento da inovação, da eficiência produtiva e dos avanços tecnológicos. Quando os produtores nacionais enfrentam a concorrência de empresas estrangeiras, são incentivados a melhorar a sua eficiência e a qualidade dos produtos para se manterem competitivos no mercado global. Este impulso para a inovação pode resultar no desenvolvimento de novas tecnologias, processos de produção e produtos, beneficiando tanto os países exportadores como os importadores.")

st.write("Além disso, o comércio internacional permite que os países beneficiem de economias de escala e de aprendizagem. Ao especializarem-se em determinados sectores e ao aumentarem a escala de produção, os países podem tirar partido de reduções de custos através de economias de escala. Maiores volumes de produção conduzem a custos médios mais baixos, tornando os bens mais acessíveis aos consumidores. Além disso, o aumento do comércio proporciona oportunidades de partilha de conhecimentos, colaborações transfronteiriças e aprendizagem com as melhores práticas estrangeiras, o que conduz a novas melhorias na produtividade e na competitividade. Finalmente, a internacionalização permite ao setor privado escapar a redes de corporativismo ou monopólios públicos quando é exposto a um mercado internacional, deixando de estar limitado ao mercado doméstico. De certa forma, o comércio internacional é também um fator de liberalização dos mercados domésticos e de alívio do jugo de regimes autocráticos sobre a economia.")

st.write("É importante notar que manifestação das vantagens comparativas pode deixar os trabalhadores menos qualificados dos países mais desenvolvidos expostos à exportação dos seus postos de trabalho para países de menores salários. É sensato que o excedente resultante dos ganhos de eficiência trazidos pela globalização seja em parte também destinado a qualificar estes trabalhadores e numa rede de segurança para situações de desemprego e dificuldades inesperadas ou incontrolaveis, sob pena de o apoio popular ao comércio internacional desaparecer e isso dar aso ao surgimento da pior espécie de populismos, nacionalismos, extremismos e colectivismos.")



