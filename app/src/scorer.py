import pandas as pd
import treelite

MODEL_TH = 0.69
MODEL_PATH = './models/fin_m.model'

# Make prediction
def make_pred(data, path_to_file):
    model = treelite.frontend.load_xgboost_model_legacy_binary(MODEL_PATH)

    result = pd.DataFrame(data['client_id'])
    result['preds'] = None

    data_np = data.to_numpy()

    predictions = treelite.gtil.predict(model, data=data_np)

    binary_predictions = (predictions > MODEL_TH).astype(int).reshape(-1,1)

    result['preds'] = binary_predictions

    return result