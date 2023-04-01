import streamlit as st
import pandas as pd
import random
from stqdm import stqdm

df_64 = pd.read_csv("juyok_DB.csv", encoding='UTF8') 
df_est = pd.read_csv("juyok_DB_est.csv", encoding='UTF8') 

# st.write(df_64)

st.markdown("## **당신의 이름은 무엇인가요?**")
name = st.text_input("이름: ")

st.markdown("## **당신의 성별은 무엇인가요?**")
sex = st.selectbox("성별: ",("여성","남성") )
st.write('성별:', sex)

st.markdown('## **당신이 궁금한 사항을 입력해 주세요.**')
question = st.text_input("질문: ")

df_64_count = pd.DataFrame(df_64["Name"])
df_64_count["Count"] = 0


# for _ in stqdm(range(50)):
#print(df_est.at[index2, "step2"])
#print(df_est.at[index2, "step3"])
#print(df_est.at[index2, "step4"])



if st.button("실행"):

    output_area = st.empty()

    for i in range(0,1):
      l1 = random.randrange(0,2)
      l2 = random.randrange(0,2)
      l3 = random.randrange(0,2)
      l4 = random.randrange(0,2)
      l5 = random.randrange(0,2)
      l6 = random.randrange(0,2)

      a = df_64["Name"].loc[(df_64.layer1 == l1)&(df_64.layer2 == l2)&(df_64.layer3 == l3)&(df_64.layer4 == l4)&(df_64.layer5 == l5)&(df_64.layer6 == l6)]
      index = df_64.index[df_64["Name"] == a.values[0]][0]

#      if i == 0:
#        first_row = df_64["Name"].loc[index] 


      df_64_count.at[index, "Count"] += 1

    max_index = df_64_count["Count"].idxmax()
    max_row = df_64_count.loc[max_index]


 #   output_area.write(first_row)

    for j in stqdm(range(0,100000)):
      l1 = str(random.randrange(0,2))
      l2 = str(random.randrange(0,2))
      l3 = str(random.randrange(0,2))
      l4 = str(random.randrange(0,2))
      l5 = str(random.randrange(0,2))
      l6 = str(random.randrange(0,2))
#      a = df_64["Name"].loc[(df_64.layer1 == l1)&(df_64.layer2 == l2)&(df_64.layer3 == l3)&(df_64.layer4 == l4)&(df_64.layer5 == l5)&(df_64.layer6 == l6)]
#      index = df_64.index[df_64["Name"] == a.values[0]][0]
      a = l1+l2+l3+l4+l5+l6
      output_area.write(a)
      output_area.write(max_row["Name"])
 
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


    
#    total_q = [max_row["Name"],df_est.at[index2, "step2"],df_est.at[index2, "step3"],df_est.at[index2, "step4"]]
           
#    st.write(total_q)

#    if first_row in total_q:
#      st.write(first_row)
#    else:
#      print("다시")
