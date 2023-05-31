import pickle
import streamlit as st
import yfinance as yf

#gold data
GOLD =yf.Ticker("GC=F")
GOLD=GOLD.history(period="max")

#silver data
SILVER =yf.Ticker("SIL=F")
SILVER=SILVER.history(period="max")

#Platinum data
PLATINUM =yf.Ticker("PL=F")
PLATINUM=PLATINUM.history(period="max")


model = pickle.load(open('C:/Users/_Emjay04/Downloads/model/randRegfile', 'rb'))
model2 = pickle.load(open('C:/Users/_Emjay04/Downloads/model/randRegfileSilver', 'rb'))
model3 = pickle.load(open('C:/Users/_Emjay04/Downloads/model/randRegfilePlatinum', 'rb'))

def main():
    st.title('GSP CRYPTO Prediction System')
    st.write('please select any button to view predictions')
    st.write(GOLD)
    new_data= GOLD[['Open','High','Low','Volume']].tail(1)
    new_data1= SILVER[['Open','High','Low','Volume']].tail(1)
    new_data2= PLATINUM[['Open','High','Low','Volume']].tail(1)
    



#prediction code
    if st.button('GOLD PID'):
         st.write(GOLD)
         makeprediction = model.predict(new_data)
         output = (makeprediction)  
         st.success('Prediction for gold per Kg is= {}' .format(output))
         
    if st.button('SILVER PID'):
        makepredictionSilver = model2.predict(new_data1)
        output1 = (makepredictionSilver)
        st.success('Prediction for silver per Kg is= {}' .format(output1))

    if st.button('PLATINUM PID'):
        makepredictionPlatinum = model3.predict(new_data2)
        output2 = (makepredictionPlatinum)
        st.success('Prediction for Platinum per Kg is= {}' .format(output2))



if __name__ == '__main__':
    main() 