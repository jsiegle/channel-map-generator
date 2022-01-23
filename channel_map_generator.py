import json

import streamlit as st
import pandas as pd

from probeinterface import get_probe

headstages = pd.read_csv('headstages.csv', index_col=0)
probes = pd.read_csv('probes.csv',index_col=0)

st.header("Channel Map Generator")
st.markdown("Select a probe and a headstage to automatically generate a "
            "JSON configuration file for the Open Ephys GUI. "
            "See the [Channel Map documentation](https://open-ephys.github.io/gui-docs/User-Manual/Plugins/Channel-Map.html) "
            "for more info.")

with st.container():

    col1, col2, col3 = st.columns(3)

    with col1:
        selected_probe = st.selectbox(
         'Select probe...',
         probes.index.values)
        prb_part_number = probes.loc[selected_probe].part_number
        prb_manufacturer = probes.loc[selected_probe].manufacturer
        st.image('images/' + prb_part_number + '-01.png')

    with col2:
        selected_headstage = st.selectbox(
         'Select headstage...',
         headstages.index.values)
        hs_part_number = headstages.loc[selected_headstage].part_number
        st.image('images/' + hs_part_number + '-01.png')

    with col3:
        st.markdown('<p style="font-size: 14px">Config file:</p>',unsafe_allow_html=True)

        # placeholder implementation:
        configuration = {
            'mapping' : [0, 1, 2, 3, 4],
            'enabled' : ['true'] * 5
        }

        ## actual implementation (still needs some work):
        #probe = get_probe(prb_manufacturer, prb_part_number)st
        #probe.wiring_to_device(hs_part_number)
        #configuration = {
        #    'mapping' : probe.device_channel_indices,
         #   'enabled' : ['true'] * len(probe.device_channel_indices)
        #}

        st.download_button(label="Download",
            data=json.dumps(configuration, indent = 6),
            file_name=prb_part_number + '_' + hs_part_number + '.json',
            mime='text/json')
