import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

st.set_option('deprecation.showPyplotGlobalUse', False)
st.set_page_config(page_title="Comércio Livre e Globalização - Comércio Livre e Globalização")
st.title("Porque é que os países que trocam, crescem?")
st.header("Pós-Graduação em Pensamento Liberal - Comércio Livre e Globalização")
st.write("por Pedro Schuller")

st.write("O comércio internacional contribui para a prosperidade dos países que nele participam de várias formas.")

st.subheader("Vantagem comparativa e especialização")

st.write("A teoria das vantagens comparativa de David Ricardo destaca os benefícios da especialização no comércio internacional. Cada país tem recursos, competências e níveis de tecnologia diferentes, o que cria diferenças nos seus custos de oportunidade de produção. Ao especializarem-se na produção de bens ou serviços nos quais têm uma vantagem comparativa, os países podem afectar os seus recursos de forma mais eficiente. Este facto conduz a um aumento da produtividade, permitindo que os países produzam mais daquilo em que são melhores e troquem por bens e serviços em que são menos eficientes. Como resultado, ambos os países podem registar níveis de consumo mais elevados, uma vez que têm acesso a uma gama mais vasta de bens e serviços a custos mais baixos.")

st.write("Por exemplo, considere-se um cenário em que o país A tem um custo de oportunidade mais baixo na produção de trigo, enquanto o país B tem um custo de oportunidade mais baixo na produção de têxteis. Se ambos os países se especializarem na produção do bem em que têm uma vantagem comparativa e efectuarem trocas comerciais entre si, podem maximizar a sua produção global. O país A pode concentrar-se na produção de mais trigo e exportar o excedente, enquanto o país B pode especializar-se na produção de têxteis e exportá-los. Esta especialização permite que ambos os países beneficiem de uma maior produtividade e de um aumento das trocas comerciais, o que conduz ao crescimento económico e à prosperidade. Vamos experimentar:")

def simulate_comparative_advantage(total_hours, hours_a_wheat, hours_a_textiles, hours_b_wheat, hours_b_textiles):
    # Calculate the number of units produced without trade
    units_a_no_trade_wheat = total_hours / (hours_a_wheat+hours_a_textiles)
    units_a_no_trade_textiles = units_a_no_trade_wheat
    units_b_no_trade_wheat = total_hours / (hours_b_wheat + hours_b_textiles)
    units_b_no_trade_textiles = units_b_no_trade_wheat

    units_a_trade_wheat = units_a_no_trade_wheat
    units_a_trade_textiles = units_a_no_trade_textiles
    units_b_trade_wheat = units_b_no_trade_wheat
    units_b_trade_textiles = units_b_no_trade_textiles

    # Calculate opportunity costs
    opportunity_cost_a_wheat = hours_a_wheat / hours_a_textiles
    opportunity_cost_a_textiles = 1/opportunity_cost_a_wheat
    opportunity_cost_b_wheat = hours_b_wheat / hours_b_textiles
    opportunity_cost_b_textiles = 1/opportunity_cost_b_wheat

    # Determine the comparative advantage
    comparative_advantage_country_textiles = "Ninguém"
    if (opportunity_cost_a_wheat) > (opportunity_cost_b_wheat):
        comparative_advantage_country_textiles = "O País A" 
        units_a_trade_wheat = 0
        units_b_trade_wheat = total_hours / hours_b_wheat
        units_a_trade_textiles = total_hours / hours_a_textiles
        units_b_trade_textiles = 0    
    if (opportunity_cost_a_wheat) < (opportunity_cost_b_wheat):
        comparative_advantage_country_textiles = "O País B"
        units_a_trade_wheat = total_hours / hours_a_wheat
        units_b_trade_wheat = 0
        units_a_trade_textiles = 0
        units_b_trade_textiles = total_hours / hours_b_textiles

    st.write(f"{comparative_advantage_country_textiles} tem a vantagem comparativa a produzir tecidos.")

    # NO TRADE
    st.write("Quantidades produzidas sem trocas comerciais:")

    df_no_trade = pd.DataFrame(
                [
                {"": "País A", "Produção de trigo": units_a_no_trade_wheat, "Produção de tecidos": units_a_no_trade_textiles, "Consumo de trigo": units_a_no_trade_wheat, "Consumo de tecidos": units_a_no_trade_textiles},
                {"": "País B", "Produção de trigo": units_b_no_trade_wheat, "Produção de tecidos": units_b_no_trade_textiles, "Consumo de trigo": units_b_no_trade_wheat, "Consumo de tecidos": units_b_no_trade_textiles}
                ]
    )

    st.dataframe(df_no_trade, hide_index=True)
    st.write(f"Total consumido sem trocas comerciais: {units_a_no_trade_wheat+units_a_no_trade_textiles+units_b_no_trade_wheat+units_b_no_trade_textiles:.0f}")

    # TRADE    
    # find fair price to trade wheat (meet halfway)
    fair_price_wheat = np.sqrt(opportunity_cost_a_wheat*opportunity_cost_b_wheat)
    
    # determine trade quantities
    trade_quantity_wheat = (units_a_trade_wheat+units_b_trade_wheat)/(fair_price_wheat+1)

    # determine trade direction (who sells what to whom)
    if comparative_advantage_country_textiles == "O País B":
        trade_quantity_wheat = -trade_quantity_wheat

    trade_quantity_textiles = trade_quantity_wheat*fair_price_wheat

    # determine consumption after trade
    units_a_consume_wheat = np.round(units_a_trade_wheat + trade_quantity_wheat)
    units_b_consume_wheat = np.round(units_b_trade_wheat - trade_quantity_wheat)
    units_a_consume_textiles = np.round(units_a_trade_textiles - trade_quantity_textiles)
    units_b_consume_textiles = np.round(units_b_trade_textiles + trade_quantity_textiles)

    st.write("Quantidades produzidas recorrendo a trocas comerciais:")
    df_trade = pd.DataFrame(
                [
                {"": "País A", "Produção de trigo": units_a_trade_wheat, "Produção de tecidos": units_a_trade_textiles, "Consumo de trigo*": units_a_consume_wheat, "Consumo de tecidos*": units_a_consume_textiles},
                {"": "País B", "Produção de trigo": units_b_trade_wheat, "Produção de tecidos": units_b_trade_textiles, "Consumo de trigo*": units_b_consume_wheat, "Consumo de tecidos*": units_b_consume_textiles}
                ]
    )
    st.dataframe(df_trade, hide_index=True)

    st.write(f"Total consumido com comércio livre: {units_a_trade_wheat+units_a_trade_textiles+units_b_trade_wheat+units_b_trade_textiles:.0f}")

    st.write("*Assumindo que os países se encontram um preço a meio caminho dos respetivos custos de oportunidade")


# Input the total number of hours available and the hours required by each country to produce one unit of wheat and textiles
total_hours = 1800
total_hours = st.slider('Quantas horas tem cada país disponíveis para trabalhar?: ', 900, 3600, step = 100, value = 1800)

df = pd.DataFrame(
    [
       {"": "País A", "Horas necessárias para produzir trigo": 40, "Horas necessárias para produzir tecidos": 80},
       {"": "País B", "Horas necessárias para produzir trigo": 80, "Horas necessárias para produzir tecidos": 40}
    ]
)
edited_df = st.data_editor(df, hide_index=True)

hours_a_wheat = int(edited_df.loc[edited_df[""]=="País A"]["Horas necessárias para produzir trigo"])
hours_a_textiles = int(edited_df.loc[edited_df[""]=="País A"]["Horas necessárias para produzir tecidos"])
hours_b_wheat = int(edited_df.loc[edited_df[""]=="País B"]["Horas necessárias para produzir trigo"])
hours_b_textiles = int(edited_df.loc[edited_df[""]=="País B"]["Horas necessárias para produzir tecidos"])

# Simulate and display the results
simulate_comparative_advantage(total_hours, hours_a_wheat, hours_a_textiles, hours_b_wheat, hours_b_textiles)


st.subheader("Dotação de factores e ganhos de produtividade")

st.write("A teoria da dotação de factores de Heckscher-Ohlin sugere que os países tendem a especializar-se na produção de bens que utilizam intensivamente os factores de produção que possuem em abundância. Esta especialização conduz a ganhos de produtividade e a um aumento dos salários dos factores de produção.")

st.write("Por exemplo, um país rico em recursos naturais, como o petróleo ou os minerais, pode especializar-se na extracção e exportação desses recursos. Esta especialização permite ao país tirar partido da sua dotação de recursos e gerar receitas de exportação. O rendimento gerado pelas exportações de recursos pode ser investido noutros sectores, como a educação, as infra-estruturas ou a tecnologia, o que leva ao desenvolvimento de outras indústrias e à diversificação da economia. Como resultado, o país regista um aumento da produtividade e dos salários dos seus trabalhadores, contribuindo para a prosperidade geral.")

st.subheader("Concorrência, inovação e economias de escala")

st.write("O comércio internacional fomenta a concorrência entre empresas nacionais e estrangeiras, o que pode levar a um aumento da inovação, da eficiência produtiva e dos avanços tecnológicos. Quando os produtores nacionais enfrentam a concorrência de empresas estrangeiras, são incentivados a melhorar a sua eficiência e a qualidade dos produtos para se manterem competitivos no mercado global. Este impulso para a inovação pode resultar no desenvolvimento de novas tecnologias, processos de produção e produtos, beneficiando tanto os países exportadores como os importadores.")

st.write("Além disso, o comércio internacional permite que os países beneficiem de economias de escala e de aprendizagem. Ao especializarem-se em determinados sectores e ao aumentarem a escala de produção, os países podem tirar partido de reduções de custos através de economias de escala. Maiores volumes de produção conduzem a custos médios mais baixos, tornando os bens mais acessíveis aos consumidores. Além disso, o aumento do comércio proporciona oportunidades de partilha de conhecimentos, colaborações transfronteiriças e aprendizagem com as melhores práticas estrangeiras, o que conduz a novas melhorias na produtividade e na competitividade. Finalmente, a internacionalização permite ao setor privado escapar a redes de corporativismo ou monopólios públicos quando é exposto a um mercado internacional, deixando de estar limitado ao mercado doméstico. De certa forma, o comércio internacional é também um fator de liberalização dos mercados domésticos e de alívio do jugo de regimes autocráticos sobre a economia.")

st.write("É importante notar que manifestação das vantagens comparativas pode deixar os trabalhadores menos qualificados dos países mais desenvolvidos expostos à exportação dos seus postos de trabalho para países de menores salários. É sensato que o excedente resultante dos ganhos de eficiência trazidos pela globalização seja em parte também destinado a qualificar estes trabalhadores e numa rede de segurança para situações de desemprego e dificuldades inesperadas ou incontrolaveis, sob pena de o apoio popular ao comércio internacional desaparecer e isso dar aso ao surgimento da pior espécie de populismos, nacionalismos, extremismos e colectivismos.")



