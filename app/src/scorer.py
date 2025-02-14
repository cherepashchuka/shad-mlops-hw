import pandas as pd
import numpy as np
import seaborn as sns
import xgboost
import json
import matplotlib
matplotlib.use('agg')

MODEL_TH = 0.69
MODEL_PATH = './models/fin_m.model'
JSON_PATH = './output/feature_importance.json'
FIGURE_PATH = './output/kde.png'

def dump_features(model, data):
    print('### Dump features ###')
    
    feature_importance = {}

    sorted_idx = np.argsort(model.feature_importances_)[::-1]

    for index in sorted_idx[:5]:
        feature_importance[data.columns[index]] = str(model.feature_importances_[index])

    with open(JSON_PATH, "w") as outfile: 
        json.dump(feature_importance, outfile, ensure_ascii=False)
    
    print('### Dump features -- Successful###')

def render_kde(result):
    print('### Render plot ###')

    kde_plot = sns.kdeplot(data=result,
                           x="preds",
                           fill=True,
                           common_norm=False,
                           alpha=.5,
                           linewidth=0,)
    figure = kde_plot.get_figure()
    figure.savefig(FIGURE_PATH)

    print('### Render plot -- Successful###')
    


# Make prediction
def make_pred(data, path_to_file):
    print('### Loading model ###')

    model = xgboost.XGBClassifier()
    model.load_model(MODEL_PATH)

    print('### Loading model -- Successful###')

    print('### Generate result file ###')

    result = pd.DataFrame(data['client_id'])
    result['preds'] = None

    data = data.drop('client_id',axis=1)

    print('### Generate result file -- Successful###')

    print('### Score ###')

    predictions = model.predict_proba(data)[:, 1]

    binary_predictions = (predictions > MODEL_TH).astype(int)

    result['preds'] = binary_predictions

    print('### Score -- Successful###')
    
    render_kde(result)

    dump_features(model, data)

    return result, JSON_PATH, FIGURE_PATH