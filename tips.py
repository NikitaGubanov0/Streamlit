import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.title("Визуализация данных по чаевым")

uploaded_file = st.sidebar.file_uploader("Загрузите CSV файл", type="csv")

def load_data(file):
    df = pd.read_csv(file)
    return df

# Если файл загружен
if uploaded_file is not None:
    df = load_data(uploaded_file)
    
    st.write("### Данные о чаевых")
    st.dataframe(df)

    st.sidebar.header("Настройки визуализации")
    chart_type = st.sidebar.selectbox(
        "Выберите тип графика",
        ["Корреляция", "Общие чаевые", "Чаевые в зависимости от пола"]
    )

    df_encoded = pd.get_dummies(df, drop_first=True)
    if chart_type == "Корреляция":
        st.write("### Корреляционная матрица")
        fig, ax = plt.subplots(figsize=(10, 6))
        sns.heatmap(df_encoded.corr(), annot=True, cmap="coolwarm", ax=ax)
        st.pyplot(fig)

    elif chart_type == "Общие чаевые":
        st.write("### График зависимости суммы чаевых от общего счета")
        fig, ax = plt.subplots()
        sns.scatterplot(data=df, x="total_bill", y="tip", hue="sex", ax=ax)
        st.pyplot(fig)

    elif chart_type == "Чаевые в зависимости от пола":
        st.write("### Распределение чаевых по полу")
        fig, ax = plt.subplots()
        sns.boxplot(x="sex", y="tip", data=df, ax=ax)
        st.pyplot(fig)

    # Функционал скачивания графиков
    st.sidebar.header("Скачать график")
    st.sidebar.write("Выберите график для скачивания:")
    
    # Сохраняем выбранный график
    if st.sidebar.button('Скачать график'):
        fig.savefig("tips_plot.png")
        with open("tips_plot.png", "rb") as file:
            btn = st.sidebar.download_button(
                label="Скачать как PNG",
                data=file,
                file_name="tips_plot.png",
                mime="image/png"
            )
else:
    st.write("Загрузите CSV файл для начала работы")
