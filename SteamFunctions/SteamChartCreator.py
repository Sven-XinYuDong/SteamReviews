import altair as alt


def compare_chart(dataframe):
    '''
    This function creates an interactive dashboard using Steam's data.

    Parameters:
        dataframe: Pandas dataframe
            This is a dataframe object containing data from Steam, that has
            been transformed to be in the format by the chart_dataframe function
            in the SteamDataFrameConverter module

    Returns:
        c1: Altair chart
            Main Altair chart of Steam information.
    '''
    selection_options = alt.binding_select(options = dataframe["variable"].unique().tolist())
    selection = alt.selection_single(name = "Genre", fields = ["variable"], bind = selection_options, init = {"variable": "Playtime"})
    brush = alt.selection_interval(empty = "none")

    base = alt.Chart(dataframe).mark_bar().encode(
        x = alt.Y("value", title = [" ", " "]),
        y = alt.Y("Name", title = None, sort = "-x")

    ).transform_filter(selection).properties(height = 800, width = 600, title = "Gaming habits of your friend group")

    text = base.mark_text(align = "center", baseline = "top").encode(
        x = alt.value(300),
        y = alt.value(830),
        text = alt.Text("Text"),
        size = alt.value(20)
    )

    image = base.mark_image().encode(
        url = "ProfilePicture"
    ).add_selection(selection).add_selection(brush).transform_filter(selection)

    c1 = (base + image + text).configure_title(fontSize = 24)

    return c1

def development_dashboard(dataframe):
    '''
    This function creates an interactive dashboard using Steam's data.

    Parameters:
        dataframe: Pandas dataframe
            This is a dataframe object containing data from Steam, that has
            been transformed to be in the format by the chart_dataframe function
            in the SteamDataFrameConverter module

    Returns:
        c1: Altair chart
            Main Altair chart of Steam information.
    '''    
    selection_options = alt.binding_select(options = dataframe["variable"].unique().tolist())
    selection = alt.selection_single(name = "Genre", fields = ["variable"], bind = selection_options, init = {"variable": "Playtime"})
    brush = alt.selection_interval(empty = "none")

    base = alt.Chart(dataframe).mark_bar().encode(
        x = alt.Y("value", title = [" ", " "]),
        y = alt.Y("Name", title = None, sort = "-x")

    ).transform_filter(selection).properties(height = 800, width = 600, title = "Gaming habits of your friend group")

    text = base.mark_text(align = "center", baseline = "top").encode(
        x = alt.value(300),
        y = alt.value(830),
        text = alt.Text("Text"),
        size = alt.value(20)
    )

    image = base.mark_image().encode(
        url = "ProfilePicture"
    ).add_selection(selection).add_selection(brush).transform_filter(selection)

    c1 = (base + image + text)

    c2 = alt.Chart(dataframe.explode("GameList")).mark_bar(baseline = "middle").encode(
        x = alt.Y("count()"),
        y = alt.X("GameList")
    ).properties(width = 1000, height = 1000).transform_filter(selection).transform_filter(brush)

    c3 = (c1 | c2)
    return c3
