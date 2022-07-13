import pickle
import streamlit as st
from sklearn.tree import DecisionTreeClassifier

with open('gambler_classifier.pickle','rb') as f:
    clf = pickle.load(f)

def main():
    st.title('Gambler Classifier')

    t = st.number_input("Hours Played")
    w = st.number_input("Win/Loss Ratio")
    n = st.number_input("Number of Deposits")

    if st.button('Predict'):
        result = clf.predict([[t,w,n]])
        st.success(result)

if __name__=='__main__':
    main()