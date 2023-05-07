def metric_component(label, value, tile):
    if label:
        if value:
            if tile:
                # using the metrics function from streamlit library.
                tile.metric(label, value)
