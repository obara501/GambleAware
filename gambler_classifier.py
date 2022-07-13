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

        if result == 0:
            st.success('Category 0')
        elif result == 1:
            st.success('Category 1')
        elif result == 2:
            st.success('Category 2')
        elif result == 3:
            st.success('Category 3')
        elif result == 4:
            st.success('Category 4')
        else:
            st.success('Category 5')

if __name__=='__main__':
    main()
