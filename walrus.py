'''A warlus operator is a operator that can assign a long 
expressions value to a variable at the time of condisonal statement creation.
operator syntex => (:=)
lets see an example.
'''
STRING = "helloooooworld"
if ((length := len(STRING)) > 10):
    print(f"this Lenght is quite long {length}")

while ((length := len(STRING)) > 5):
    STRING = STRING[:-1]
    print(f"poping out {length} index letter,")
else:
    print(f"Reduced the length to {length} letters resulting {STRING}")
