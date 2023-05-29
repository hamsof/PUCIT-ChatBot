import pickle

def function_serializer(text_input):
    return "You got me it`s HAMSOF"

#serialization of this function to a file
with open('py.pkl', 'wb') as file:
    pickle.dump(function_serializer, file)
