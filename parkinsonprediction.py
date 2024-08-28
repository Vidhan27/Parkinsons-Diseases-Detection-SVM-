import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# Loading the Saved Model
parkinsons_model = pickle.load(open('parkinsons_model (3).sav', 'rb'))

# Sidebar for Navigation
with st.sidebar:
    selected = option_menu('Parkinsons Disease Prediction System',
                           ['Prediction', 'Information', 'About Me', 'How to Use'],
                           icons=['bag-plus'], default_index=0)

# Parkinson Prediction Page
if selected == 'Prediction':
    # Page title
    st.title("Parkinson Prediction using ML")

    # Input fields
    Fo = st.text_input('MDVP:Fo(Hz)')
    Fhi = st.text_input('MDVP:Fhi(Hz)')
    Flo = st.text_input('MDVP:Flo(Hz)')
    JitterPer = st.text_input('MDVP:Jitter(%)')
    JitterAbs = st.text_input('MDVP:Jitter(Abs)')
    RAP = st.text_input('MDVP:RAP')
    PPQ = st.text_input('MDVP:PPQ')
    JitterDDP = st.text_input('Jitter:DDP')
    Shimmer = st.text_input('MDVP:Shimmer')
    ShimmerdB = st.text_input('MDVP:Shimmer(dB)')
    ShimmerAPQ3 = st.text_input('Shimmer:APQ3')
    ShimmerAPQ5 = st.text_input('Shimmer:APQ5')
    APQ = st.text_input('MDVP:APQ')
    DDA = st.text_input('Shimmer:DDA')
    NHR = st.text_input('NHR')
    HNR = st.text_input('HNR')
    RDPE = st.text_input('RDPE')
    DFA = st.text_input('DFA')
    spread1 = st.text_input('spread1')
    spread2 = st.text_input('spread2')
    D2 = st.text_input('D2')
    PPE = st.text_input('PPE')

    # Code for prediction
    park_diagnosis = ''

    # Creating a button for diagnosis
    if st.button('Parkinsons Prediction'):
        # List of user inputs
        user_input = [Fo, Fhi, Flo, JitterPer, JitterAbs, RAP, PPQ, JitterDDP, Shimmer,
                      ShimmerdB, ShimmerAPQ3, ShimmerAPQ5, APQ, DDA, NHR, HNR, RDPE, DFA,
                      spread1, spread2, D2, PPE]

        # Check if any input is empty
        if '' in user_input:
            st.error("Please fill in all the input fields.")
        else:
            # Convert inputs to floats
            user_input = [float(x) for x in user_input]

            # Make prediction
            park_prediction = parkinsons_model.predict([user_input])

            print(park_prediction)

            if park_prediction[0] == 1:
                park_diagnosis = "The Person has a chance to have Parkinson's Disease"
            else:
                park_diagnosis = "The Person does not have a chance for Parkinson's Disease"

            st.success(park_diagnosis)

elif selected == 'Information':
    st.title('Information about Heart Disease')
    st.markdown(
        """
        <p style='font-size:25px;'>
        Parkinson's disease is a progressive neurological disorder that primarily affects movement, balance, and coordination. It is caused by the degeneration of dopamine-producing neurons in a region of the brain called the substantia nigra. Early signs include tremors, stiffness, and difficulty with balance or walking, but symptoms can vary widely among individuals. As the disease progresses, it can lead to more severe physical and cognitive impairments. It's important to be aware of the early symptoms and seek medical advice promptly, as early intervention can help manage the condition and improve quality of life.
        unsafe_allow_html=True
    )

# About Me Page
elif selected == 'About Me':
    st.title('About Me')
    st.markdown(
        """
        <p style='font-size:25px;'>
        Me   Vidhan Prajapati   , A 3rd Year BTech Student pursuing  Computer Science at Karnavati University  <br>
        This project was made on purpose so that i can understand more about application of Machine Learning in healthcare , and would keep on learning
        Thanku for Vising
        </p>
        """, 
        unsafe_allow_html=True
    )

# How to Use Page
elif selected == 'How To Use':
    st.title('How to Use')
    st.markdown(
        """
        <p style='font-size:25px;'>
        This website is made to take in the inputs data of particular reading of a particular machine
        It would not be directly available to public
        But if you add the values it can make the prediction
        <br>This is just the demo of how prediction system would look like
        The algorithm used in model is Support Vector Machine
        </p>
        """, 
        unsafe_allow_html=True
    )
