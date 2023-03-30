import json
import pickle
import numpy as np

__model=None

def get_company(eng,qa,la,cp,essay,core):
    x=np.zeros(6)
    x[0]=eng
    x[1]=qa
    x[2]=la
    x[3]=cp
    x[4]=essay
    x[5]=core
    load_saved_artifects()
    return __model.predict([x])[0]

def load_saved_artifects():
    print("loading saved artifects")
    global __model
    
    with open("./p_p_new.pickle","rb") as f:
        __model=pickle.load(f)
    print("loading saved artifects done")

if __name__=="__main__":
    load_saved_artifects()
    #print(get_company(665,780,730,515,28,15,3))