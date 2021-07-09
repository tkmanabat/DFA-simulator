import streamlit as st
from visual import dfa,dfa2

from automata.fa.dfa import DFA
from visual_automata.fa.dfa import VisualDFA

import base64


st.set_page_config(
     page_title="DFA Simulator",
     page_icon="🚀",
     layout="wide",
     initial_sidebar_state="expanded",
    )


if 'n' not in st.session_state:
	    st.session_state.n = 0


def show_transition(sample_string,n):
    st.write('### String Checking: `'+ sample_string[0:n]+'`')


    graph=dfa.show_diagram(sample_string[0:n])
    
    graph.format="svg"
    graph.render("test")
    f = open("test.svg","r")
    lines = f.readlines()
    line_string=''.join(lines)
    render_svg(line_string)



def render_svg(svg):
    b64 = base64.b64encode(svg.encode('utf-8')).decode("utf-8")
    html = r'<img src="data:image/svg+xml;base64,%s" width="1100px" height="500px" />' % b64
    st.write(html, unsafe_allow_html=True)



st.write('# DFA Simulator 🤹‍♂️')
st.write ('Web application for step-by-step visual simulation of deterministic finite state machines which are defined with given regular expressions.')


st.sidebar.write('# Input Panel 📚')
st.sidebar.write(' Please select problem and input sample string for testing.')
selection=st.sidebar.selectbox("Select Regular Expression",['(a+b)(a+b)*(aa+bb)(ab+ba)(a+b)*(aba+baa)','(11+00)(1+0)*(101+111+01)(00*+11*)(1+0+11)'])

problem1='(a+b)(a+b)*(aa+bb)(ab+ba)(a+b)*(aba+baa)'
problem2='(11+00)(1+0)*(101+111+01)(00*+11*)(1+0+11)'

with st.sidebar:
        if selection=='(a+b)(a+b)*(aa+bb)(ab+ba)(a+b)*(aba+baa)':
            dfa=dfa
            regex=problem1

        elif selection=='(11+00)(1+0)*(101+111+01)(00*+11*)(1+0+11)':
            dfa=dfa2
            regex=problem2

st.write('### Selected Regular Expression: ```' + regex+'```')

with st.form(key='input'):
    with st.sidebar:
        sample_string=st.text_input('Enter Sample String:')
        submit_button=st.form_submit_button(label='Test')

        simulate_bool=st.checkbox('Simulate steps')


if submit_button:
    #st.write('### Selected Regular Expression: ```' + regex+'```')

    if sample_string[0]== 'a' or 'A' or 'b' or 'B':
            sample_string=sample_string.lower()

    sample_string_bool=dfa.input_check(sample_string)



    graph=dfa.show_diagram(sample_string)
    graph.format="svg"

    graph.render("test")
    f = open("test.svg","r")
    lines = f.readlines()
    line_string=''.join(lines)
    render_svg(line_string)


    if sample_string_bool.columns[0][0][1:-1]=='Accepted':
        st.success(sample_string +' is accepted!')
    elif sample_string_bool.columns[0][0][1:-1]=='Rejected':
        st.error(sample_string +' is rejected!')

    st.write("### Tabulated Steps: ")
    col1, col2, col3 = st.beta_columns(3)
    with col1:
        st.dataframe(dfa.table,width=1100,height=500)

    if selection=="(a+b)(a+b)*(aa+bb)(ab+ba)(a+b)*(aba+baa)":
        with col2:
            st.write("### Context Free Grammar")
            st.write("S → ABCDBE")
            st.write("A → a | b")
            st.write("B → aB | bB | ^")
            st.write("C → aa | bb")
            st.write("D → ab | ba")
            st.write("E → aba | baa")
    elif selection=="(11+00)(1+0)*(101+111+01)(00*+11*)(1+0+11)":
        with col2:
            st.write("### Context Free Grammar")
            st.write("S → ABCDG")
            st.write("A → 11 | 00")
            st.write("B → 1B | 0B | ^")
            st.write("C → 101 | 111 | 01")
            st.write("D → E | F")
            st.write("E → 00E | ^")
            st.write("F → 11F | ^")
            st.write("G → 1 | 0 | 11")

if simulate_bool:
    st.sidebar.write('# Simulator Navigation')
    st.sidebar.write(' Use the buttons below to simulate the sample string thru the DFA.')
    col1, col2 = st.sidebar.beta_columns([1.8,1])
    with col2:
        next_button=st.button('Next >')
    with col1:
        back_button=st.button('< Back')


    if next_button:

        if st.session_state.n<len(sample_string):
            st.session_state.n += 1
            show_transition(sample_string,st.session_state.n)

        elif st.session_state.n==len(sample_string):
            show_transition(sample_string,st.session_state.n)
            st.write("### End of simulation")
            sample_string_bool=dfa.input_check(sample_string)
            st.write('String is: `' + sample_string_bool.columns[0][0][1:-1]+'`')
            st.write('### Tabulated Steps')
            st.write(dfa.table)


    elif back_button:

        if st.session_state.n<=len(sample_string):
            st.session_state.n -= 1
            sample_string_bool=dfa.input_check(sample_string)
            show_transition(sample_string,st.session_state.n)



