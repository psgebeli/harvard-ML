from logic import *

rain = Symbol("rain") # It is raining.
hagrid = Symbol("hagrid") # Harry visited Hagrid
dumbledore = Symbol("dumbledore") # Harry visited dumbledore

knowledge = And(
    Implication(Not(rain), hagrid), # if its not raining, harry visited hagrid
    Or(hagrid, dumbledore), # harry visited hagrid or dumbledore
    Not(And(hagrid, dumbledore)), # harry did not visit both
    dumbledore
)

print(model_check(knowledge, rain))