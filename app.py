import streamlit as st

from pythomata import SimpleDFA

from PIL import Image
import base64


def render_svg(svg):
    b64 = base64.b64encode(svg.encode('utf-8')).decode("utf-8")
    html = r'<img src="data:image/svg+xml;base64,%s"/>' % b64
    st.write(html, unsafe_allow_html=True)


st.write('# Automata DFA Calculator ')

st.write('### Select Automata Question')

selection=st.selectbox("Select Question",['First','Second'])

if selection == 'First':
    alphabet = {"a", "b"}
    states = {"s1", "s2", "s3","s4", "s5", "s6","s7", "s8", "s9","s10", "s11", "s12"}
    initial_state = "s1"
    accepting_states = {"s12"}
    transition_function = {
    "s1": {
        "a" : "s2",
        "b" : "s2"
    },
    "s2": {
        "a" : "s3",
        "b" : "s4",
    },
    "s3":{
        "a" : "s5",
    },
    "s4": {
        "b" : "s5",
    },
    "s5": {
        "a" : "s6",
        "b" : "s7"
    },
    "s6":{
        "b" : "s8"
    },
    "s7": {
        "a" : "s8"
    },
    "s8":{
        "a" : "s9",
        "b" : "s10"
    },
    "s9": {
        "b" : "s11"
    },
    "s10":{
        "a" : "s11"
    },
    "s11": {
        "a" : "s12"
    },
    "s12":{
    }
}
dfa = SimpleDFA(states, alphabet, initial_state, accepting_states, transition_function)

if selection=='Second':
    alphabet = {"a", "b"}
    states = {"s1", "s2", "s3","s4", "s5", "s6","s7", "s8", "s9","s10", "s11", "s12"}
    initial_state = "s1"
    accepting_states = {"s12"}
    transition_function = {
        "s1": {
            "a" : "s2",
            "b" : "s2"
        },
        "s2": {
            "a" : "s3",
            "b" : "s4",
        },
        "s3":{
            "a" : "s5",
        },
        "s4": {
            "b" : "s5",
        },
        "s5": {
            "a" : "s6",
            "b" : "s7"
        },
        "s6":{
            "b" : "s8"
        },
        "s7": {
            "a" : "s8"
        },
        "s8":{
            "a" : "s9",
            "b" : "s10"
        },
        "s9": {
            "b" : "s11"
        },
        "s10":{
            "a" : "s11"
        },
        "s11": {
            "a" : "s12"
        },
        "s12":{
        }
    }
    dfa = SimpleDFA(states, alphabet, initial_state, accepting_states, transition_function)

with st.form(key='regex'):
    sample_string=st.text_input(label="Test the string")
    submit_button=st.form_submit_button(label='Test')

    if submit_button:
       
        st.write('### Is the string accepted?: ')
        st.write(dfa.accepts(sample_string))
        
        st.write('### DFA Diagram:')

        graph = dfa.to_graphviz()
        graph.render("DFA")
        f = open("DFA.svg","r")
        lines = f.readlines()
        line_string=''.join(lines)
        
        render_svg(line_string)
        