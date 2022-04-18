import ktrain
from ktrain import text


classes = {
    0 : "Fraudulent",
    1 : "Legitimate"
}

with open('listing.txt', 'r') as f:
    listing = f.read()

def inference(input):


    # Transformer Model
    model_ = 'distilbert-base-uncased'
    t_mod = text.Transformer(model_, maxlen=500, classes = [0,1])

    # Model Classifier
    model = t_mod.get_classifier()
    model.from_pretrained('/Models/bert.cpkt')

    preproc = t_mod
    predictor = ktrain.get_predictor(model, preproc)

    predict = predictor.predict(input)
    return classes[predict]

# print(inference(listing))



