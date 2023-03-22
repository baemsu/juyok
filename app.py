import streamlit as st
import pandas as pd
import random

df_64 = pd.read_csv("juyok_DB.csv", encoding='UTF8') 
df_est = pd.read_csv("juyok_DB_est.csv", encoding='UTF8') 

# st.write(df_64)

st.write('당신이 궁금한 사항을 입력해 주세요.')
question = st.text_input("질문: ")

df_64_count = pd.DataFrame(df_64["Name"])
df_64_count["Count"] = 0

for i in range(0,1):
  l1 = random.randrange(0,2)
  l2 = random.randrange(0,2)
  l3 = random.randrange(0,2)
  l4 = random.randrange(0,2)
  l5 = random.randrange(0,2)
  l6 = random.randrange(0,2)

  a = df_64["Name"].loc[(df_64.layer1 == l1)&(df_64.layer2 == l2)&(df_64.layer3 == l3)&(df_64.layer4 == l4)&(df_64.layer5 == l5)&(df_64.layer6 == l6)]
  index = df_64.index[df_64["Name"] == a.values[0]][0]

  df_64_count.at[index, "Count"] += 1

max_index = df_64_count["Count"].idxmax()
max_row = df_64_count.loc[max_index]



#print(df_est.at[index2, "step2"])
#print(df_est.at[index2, "step3"])
#print(df_est.at[index2, "step4"])


if st.button("실행"):

    index = df_64.index[df_64["Name"] == max_row["Name"]][0]
    st.write('현재- ', max_row["Name"],":", df_64.at[index, "explain_short"])

    index2 = df_est.index[df_est["step1"] == max_row["Name"]][0]

    con = st.container()
    con.caption("Result")
    
    index1 = df_64.index[df_64["Name"] == df_est.at[index2, "step2"]][0]
    st.write( "3개월후","-",df_est.at[index2, "step2"],":", df_64.at[index1, "explain_short"])

    index1 = df_64.index[df_64["Name"] == df_est.at[index2, "step3"]][0]
    st.write( "6개월후","-",df_est.at[index2, "step3"],":", df_64.at[index1, "explain_short"])

    index1 = df_64.index[df_64["Name"] == df_est.at[index2, "step4"]][0]
    st.write( "9개월후","-",df_est.at[index2, "step4"],":", df_64.at[index1, "explain_short"])
