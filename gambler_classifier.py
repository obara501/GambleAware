from __future__ import division
import pickle
import streamlit as st
from sklearn.tree import DecisionTreeClassifier

with open('gambler_classifier.pickle','rb') as f:
    clf = pickle.load(f)

def main():
    
    st.title('Gambling Disorder Predictor')

    b = st.number_input("Current Account Balance")
    d = st.number_input("Total funds deposited")
    wd = st.number_input("Total funds withdrawn")
    t = st.number_input("Hours Played")
    
    try:
        wlr = (float(b)+float(wd))/float(d)
    except ZeroDivisionError:
        wlr = 0

    n = st.number_input("Number of Deposits Made")

    if st.button('Predict'):

        result = clf.predict([[t,wlr,n]])

        if result == 0:
            st.success('You were placed in Category 0: Your behaviour does not seem to be destructive.')
        elif result == 1:
            st.success('You were placed in Category 1: You have a low chance of developing GD.\nPlay thoughtfully and you will be fine. ')
        elif result == 2:
            st.success('You were placed in Category 2: You have a low to mediate risk of developing GD.\nPlease try to gamble less or spend less wagers. ')
        elif result == 3:
            st.success('You were placed in Category 3: You have a mediate to high risk of developing GD.\nDo your friends think you gamble too much? Try gambling less and seek professional help.')
        elif result == 4:
            st.success('You were placed in Category 4: You have been placed on the high risk scale of developing GD.\nWe suggest you stop gambling immediatly and seek professional help.')
        else:
            st.success('You were placed in Category 5: You are at the highest risk of developig GD.\nWe suggest you stop gambling immediately. Ask people around you to help you curb your urges and seek professional assistance.')
        

if __name__=='__main__':
    main()
