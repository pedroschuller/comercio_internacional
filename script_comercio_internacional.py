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

def calculate_production_consumption(max_limited_product, max_ltd_comp_advantage, max_unlimited, fair_price_ltd):
            # intersecção entre as curvas X = Y e os limites de produção da economia devolve a seguinte equação:
            total_production = (max_unlimited*max_limited_product)/(max_unlimited-max_ltd_comp_advantage+max_limited_product)

            #produção de cada país
            units_unltd_produce_ltd = total_production - max_ltd_comp_advantage
            units_unltd_produce_unltd = total_production
            units_ltd_produce_ltd = max_ltd_comp_advantage
            units_ltd_produce_unltd = 0 

            #consumo de cada país
            units_unltd_consume_ltd = units_unltd_produce_ltd + units_ltd_produce_ltd/(1+fair_price_ltd)
            units_unltd_consume_unltd = units_unltd_consume_ltd
            units_ltd_consume_unltd = total_production - units_unltd_consume_ltd
            units_ltd_consume_ltd = units_ltd_consume_unltd 

            return units_unltd_produce_ltd, units_unltd_produce_unltd, units_ltd_produce_ltd, units_ltd_produce_unltd, units_unltd_consume_ltd, units_unltd_consume_unltd, units_ltd_consume_unltd, units_ltd_consume_ltd

def simulate_comparative_advantage(total_hours, hours_a_wheat, hours_a_textiles, hours_b_wheat, hours_b_textiles):
    # Calculate the number of units produced without trade
    units_a_no_trade_wheat = total_hours / (hours_a_wheat + hours_a_textiles)
    units_a_no_trade_textiles = units_a_no_trade_wheat
    units_b_no_trade_wheat = total_hours / (hours_b_wheat + hours_b_textiles)
    units_b_no_trade_textiles = units_b_no_trade_wheat

    # Calculate opportunity costs
    opportunity_cost_a_wheat = hours_a_wheat / hours_a_textiles
    opportunity_cost_a_textiles = 1 / opportunity_cost_a_wheat
    opportunity_cost_b_wheat = hours_b_wheat / hours_b_textiles
    opportunity_cost_b_textiles = 1 / opportunity_cost_b_wheat


    df_opportunity = pd.DataFrame(
                [
                {"": "País A", "C. oportunidade de produzir trigo em un. de tecidos": "{:.2f}".format(opportunity_cost_a_wheat), "C. oportunidade de produzir tecidos em un. de trigo": "{:.2f}".format(opportunity_cost_a_textiles)},
                {"": "País B", "C. oportunidade de produzir trigo em un. de tecidos": "{:.2f}".format(opportunity_cost_b_wheat), "C. oportunidade de produzir tecidos em un. de trigo": "{:.2f}".format(opportunity_cost_b_textiles)}
                ]
    )

    st.dataframe(df_opportunity.style.highlight_min(axis=0, subset=["C. oportunidade de produzir trigo em un. de tecidos","C. oportunidade de produzir tecidos em un. de trigo"]), hide_index=True)

    # Determine the comparative advantage
    comparative_advantage_country_textiles = "Ninguém"

    if (opportunity_cost_a_wheat) > (opportunity_cost_b_wheat):
        comparative_advantage_country_textiles = "O País A"  
    if (opportunity_cost_a_wheat) < (opportunity_cost_b_wheat):
        comparative_advantage_country_textiles = "O País B"

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

    #produções máximas:
    max_a_wheat = total_hours / hours_a_wheat
    max_a_textiles = total_hours / hours_a_textiles
    max_b_wheat = total_hours / hours_b_wheat
    max_b_textiles = total_hours / hours_b_textiles

    max_wheat = max_a_wheat + max_b_wheat
    max_textiles = max_a_textiles + max_b_textiles

    # find fair price to trade wheat (meet halfway)
    fair_price_wheat_inicial = np.sqrt(opportunity_cost_a_wheat*opportunity_cost_b_wheat)
    fair_price_wheat = st.slider('Os países só têm interesse em trocar se o preço do trigo em unidades de tecidos se compreender entre os respetivos custos de oportunidade: ', min(opportunity_cost_a_wheat, opportunity_cost_b_wheat), max(opportunity_cost_a_wheat, opportunity_cost_b_wheat), value = float(fair_price_wheat_inicial))
    fair_price_textiles = 1/fair_price_wheat

    if comparative_advantage_country_textiles == "O País A":
        if hours_a_textiles <= hours_b_wheat: # se o país A consegue produzir todo o tecido da economia:
            # país limitado = B | produto limitado: trigo
            units_a_produce_wheat, units_a_produce_textiles, units_b_produce_wheat, units_b_produce_textiles, units_a_consume_wheat, units_a_consume_textiles, units_b_consume_wheat, units_b_consume_textiles = calculate_production_consumption(max_wheat, max_b_wheat, max_a_textiles, fair_price_wheat)
        else:
            # país limitado = A | produto limitado: tecidos
            units_b_produce_textiles, units_b_produce_wheat, units_a_produce_textiles, units_a_produce_wheat, units_b_consume_textiles, units_b_consume_wheat, units_a_consume_wheat, units_a_consume_textiles = calculate_production_consumption(max_textiles, max_a_textiles, max_b_wheat, fair_price_textiles)
    if comparative_advantage_country_textiles == "O País B":
        if hours_b_textiles <= hours_a_wheat: # se o país B consegue produzir todo o tecido da economia:
            # país limitado = A | produto limitado: trigo
            units_b_produce_wheat, units_b_produce_textiles, units_a_produce_wheat, units_a_produce_textiles, units_b_consume_wheat, units_b_consume_textiles, units_a_consume_wheat, units_a_consume_textiles = calculate_production_consumption(max_wheat, max_a_wheat, max_b_textiles, fair_price_wheat)
        else:
            # país limitado = B | produto limitado: tecidos
            units_a_produce_textiles, units_a_produce_wheat, units_b_produce_textiles, units_b_produce_wheat, units_a_consume_textiles, units_a_consume_wheat, units_b_consume_wheat, units_b_consume_textiles = calculate_production_consumption(max_textiles, max_b_textiles, max_a_wheat, fair_price_textiles)


    # TRADE    
    if comparative_advantage_country_textiles != "Ninguém":

        st.write("Quantidades produzidas recorrendo a trocas comerciais:")
        df_produce = pd.DataFrame(
                    [
                    {"": "País A", "Produção de trigo": "{:.2f}".format(units_a_produce_wheat), "Produção de tecidos": "{:.2f}".format(units_a_produce_textiles), "Consumo de trigo*": "{:.2f}".format(units_a_consume_wheat), "Consumo de tecidos*": "{:.2f}".format(units_a_consume_textiles)},
                    {"": "País B", "Produção de trigo": "{:.2f}".format(units_b_produce_wheat), "Produção de tecidos": "{:.2f}".format(units_b_produce_textiles), "Consumo de trigo": "{:.2f}".format(units_b_consume_wheat), "Consumo de tecidos": "{:.2f}".format(units_b_consume_textiles)}
                    ]
        )
        st.dataframe(df_produce, hide_index=True)

        st.write(f"Total consumido com comércio livre: {units_a_consume_wheat+units_a_consume_textiles+units_b_consume_wheat+units_b_consume_textiles:.0f}")
         
# Input the total number of hours available and the hours required by each country to produce one unit of wheat and textiles
total_hours = 1800
total_hours = st.slider('Quantas horas tem cada país disponíveis para trabalhar?: ', 900, 3600, step = 100, value = 1800)

st.write("Quantas horas demora cada país a produzir uma unidade de cada bem?")

df = pd.DataFrame(
    [
       {"": "País A", "Horas necessárias para produzir trigo": 40, "Horas necessárias para produzir tecidos": 60},
       {"": "País B", "Horas necessárias para produzir trigo": 60, "Horas necessárias para produzir tecidos": 120}
    ]
)
edited_df = st.data_editor(df, disabled = [""], hide_index=True) 

hours_a_wheat = int(edited_df.loc[edited_df[""]=="País A"]["Horas necessárias para produzir trigo"])
hours_a_textiles = int(edited_df.loc[edited_df[""]=="País A"]["Horas necessárias para produzir tecidos"])
hours_b_wheat = int(edited_df.loc[edited_df[""]=="País B"]["Horas necessárias para produzir trigo"])
hours_b_textiles = int(edited_df.loc[edited_df[""]=="País B"]["Horas necessárias para produzir tecidos"])

# Simulate and display the results
simulate_comparative_advantage(total_hours, hours_a_wheat, hours_a_textiles, hours_b_wheat, hours_b_textiles)


st.subheader("Dotação de factores e ganhos de produtividade")

st.write("A teoria da dotação de factores de Heckscher-Ohlin sugere que os países tendem a especializar-se na produção de bens que utilizam intensivamente os factores de produção que possuem em abundância. Esta especialização conduz a ganhos de produtividade e a um aumento dos salários dos factores de produção.")

st.write("Por exemplo, um país rico em recursos naturais, como o petróleo ou os minerais, pode especializar-se na extracção e exportação desses recursos. Esta especialização permite ao país tirar partido da sua dotação de recursos e gerar receitas de exportação. O rendimento gerado pelas exportações de recursos pode ser investido noutros sectores, como a educação, as infra-estruturas ou a tecnologia, o que leva ao desenvolvimento de outras indústrias e à diversificação da economia. Como resultado, o país regista um aumento da produtividade e dos salários dos seus trabalhadores, contribuindo para a prosperidade geral. Vamos novamente simular esta teoria:")


df_ohlin = pd.DataFrame(
    [
       {"": "Trigo", "Unidades de trabalho necessárias": 6, "Unidades de capital necessárias": 2, "Intensidade de trabalho":6/2},
       {"": "Tecidos", "Unidades de trabalho necessárias": 8, "Unidades de capital necessárias": 4, "Intensidade de trabalho":8/4}
    ]
)
edited_df_ohlin = st.data_editor(df_ohlin, disabled = ["", "Intensidade de trabalho"], hide_index=True) 
edited_df_ohlin["Intensidade de trabalho"] = (edited_df_ohlin["Unidades de trabalho necessárias"] / edited_df_ohlin["Unidades de capital necessárias"])


st.subheader("Concorrência, inovação e economias de escala")

st.write("O comércio internacional fomenta a concorrência entre empresas nacionais e estrangeiras, o que pode levar a um aumento da inovação, da eficiência produtiva e dos avanços tecnológicos. Quando os produtores nacionais enfrentam a concorrência de empresas estrangeiras, são incentivados a melhorar a sua eficiência e a qualidade dos produtos para se manterem competitivos no mercado global. Este impulso para a inovação pode resultar no desenvolvimento de novas tecnologias, processos de produção e produtos, beneficiando tanto os países exportadores como os importadores.")

st.write("Além disso, o comércio internacional permite que os países beneficiem de economias de escala e de aprendizagem. Ao especializarem-se em determinados sectores e ao aumentarem a escala de produção, os países podem tirar partido de reduções de custos através de economias de escala. Maiores volumes de produção conduzem a custos médios mais baixos, tornando os bens mais acessíveis aos consumidores. Além disso, o aumento do comércio proporciona oportunidades de partilha de conhecimentos, colaborações transfronteiriças e aprendizagem com as melhores práticas estrangeiras, o que conduz a novas melhorias na produtividade e na competitividade. Finalmente, a internacionalização permite ao setor privado escapar a redes de corporativismo ou monopólios públicos quando é exposto a um mercado internacional, deixando de estar limitado ao mercado doméstico. De certa forma, o comércio internacional é também um fator de liberalização dos mercados domésticos e de alívio do jugo de regimes autocráticos sobre a economia.")

st.write("É importante notar que manifestação das vantagens comparativas pode deixar os trabalhadores menos qualificados dos países mais desenvolvidos expostos à exportação dos seus postos de trabalho para países de menores salários. É sensato que o excedente resultante dos ganhos de eficiência trazidos pela globalização seja em parte também destinado a qualificar estes trabalhadores e numa rede de segurança para situações de desemprego e dificuldades inesperadas ou incontrolaveis, sob pena de o apoio popular ao comércio internacional desaparecer e isso dar aso ao surgimento da pior espécie de populismos, nacionalismos, extremismos e colectivismos.")

st.divider()

st.write("Check the source code @ https://github.com/pedroschuller/comercio_internacional/blob/main/script_comercio_internacional.py")




