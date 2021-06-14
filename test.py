from pythomata import SimpleDFA
from graphviz import Digraph

dot=Digraph()


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

"""word="abbbaaba"
print(dfa.accepts(word))"""


#print graph 
graph = dfa.to_graphviz()
print(graph.render("graph"))



#dot.render('test.dot', view=True)

