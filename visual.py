#import automata-lib
from automata.fa.dfa import DFA

#import visual automata wrapper
from visual_automata.fa.dfa import VisualDFA


#DFA given
dfa = VisualDFA(
    states={"s0","s1","s2","s3","s4","s5","s6","s7","s8","s9","s10","s11","s12","s13","s14","s15","s16"},
    input_symbols={"a","b"},
    transitions={
        "s0":{"a":"s1","b":"s1"},
        "s1":{"a":"s2","b":"s3"},
        "s2":{"a":"s4","b":"s3"},
        "s3":{"a":"s2","b":"s6"},
        "s4":{"a":"s9","b":"s5"},
        "s5":{"a":"s10","b":"s6"},
        "s6":{"a":"s7","b":"s8"},
        "s7":{"a":"s4","b":"s10"},
        "s8":{"a":"s10","b":"s8"},
        "s9":{"a":"s10","b":"s9"},
        "s10":{"a":"s11","b":"s12"},
        "s11":{"a":"s11","b":"s13"},
        "s12":{"a":"s14","b":"s12"},
        "s13":{"a":"s15","b":"s12"},
        "s14":{"a":"s16","b":"s13"},
        "s15":{"a":"s16","b":"s13"},
        "s16":{"a":"s11","b":"s13"},
    },
        
    initial_state="s0",
    final_states={"s15","s16"},
)


dfa2 = VisualDFA(
    states={"s0","s1","s2","s3","s4","s5","s6","s7","s8","s9","s10","s11","s12","s13","s14","s15","s16","s17"},
    input_symbols={"0","1"},
    transitions={
        "s0":{"0":"s2","1":"s1"},
        "s1":{"0":"s3","1":"s4"},
        "s2":{"0":"s4","1":"s3"},
        "s3":{"0":"s3","1":"s3"},
        "s4":{"0":"s5","1":"s6"},
        "s5":{"0":"s5","1":"s10"},
        "s6":{"0":"s5","1":"s7"},
        "s7":{"0":"s5","1":"s8"},
        "s8":{"0":"s9","1":"s12"},
        "s9":{"0":"s14","1":"s15"},
        "s10":{"0":"s9","1":"s11"},
        "s11":{"0":"s17","1":"s13"},
        "s12":{"0":"s14","1":"s13"},
        "s13":{"0":"s14","1":"s13"},
        "s14":{"0":"s14","1":"s15"},
        "s15":{"0":"s9","1":"s16"},
        "s16":{"0":"s17","1":"s13"},
        "s17":{"0":"s5","1":"s10"},

    },
        
    initial_state="s0",
    final_states={"s13","s14","s15","s16","s17"},
)




#print transition table for dfa
#print(dfa.table)

#show DFA figure
#dfa2.show_diagram(view=True)


#check input string without diagram
#df=dfa2.input_check("000111")
#print(df.columns[0][0][1:-1])




#check input string with diagram
# #dfa.show_diagram("aabbabaa",view=True)
