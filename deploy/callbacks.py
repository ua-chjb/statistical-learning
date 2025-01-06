from dash import Input, Output
import dash_mantine_components as dmc

from functools import reduce
from operator import or_

from data import uber_df3
from charts import figure3_scorehist, figure4_stripthumbs, figure5_bubble, figure8_3d
from color import simple_layout

import warnings
warnings.filterwarnings("ignore")

def callbacks_baby(app):
    @app.callback(
        Output("comp3_CBOfigure_smhist", "figure"),
        Output("comp4_CB0figure_smstrip", "figure"),
        Output("comp5_CB0figure_bubble", "figure"),
        Output("comp8_CBOfigure_3d", "figure"),
        Input("comp6_CBIinput_dropdown", "value")
    )
    def bigdoubled(versions):
        
        masks_lst = []

        if not versions:
            pass
        else:
            for version in versions:
                mask = ( uber_df3["reviewCreatedVersion"] == version )
                masks_lst.append(mask)

        final_masks = reduce(or_, masks_lst)

        return simple_layout(figure3_scorehist(final_masks)), simple_layout(figure4_stripthumbs(final_masks)), simple_layout(figure5_bubble(final_masks)), simple_layout(figure8_3d(final_masks))
    

