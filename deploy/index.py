import dash_mantine_components as dmc
from dash import html, dcc, _dash_renderer
from dash_iconify import DashIconify
_dash_renderer._set_react_version('18.2.0')

from data import uber_df3
from charts import figure0_timescatter, figure2_pie, table7_appversions
from color import simple_layout

# # # # # # # # # # # # # # block0 # # # # # # # # # # # # # #

comp0_figure_time = dmc.Card(
    [
        dcc.Graph(figure=simple_layout(figure0_timescatter()), id="comp0_figure_time", className="g")
    ],
    withBorder=True,
    shadow="md",
    className="t t0"
)

comp1_text_intro = dmc.Card(
    [
        dmc.Text(
            "APP VERSIONS",
            size="md",
            fw=500,
            className="tx tx_header"
        ),
        dmc.Text(
            "- there are several dozen app versions, but 4 comprise ~75% of the data",
            size="xs",
            className="tx tx_body"
        ),
        dmc.Text(
            """- "scores" has a binomial distribution, with peaks at 1 and 5""",
            size="xs",
            className="tx tx_body"
        ),
        dmc.Text(
            """- "thumbs up" is highly skewed right, with most centered around 0 but a few outliers with thumbs up counts of 30-100""",
            size="xs",
            className="tx tx_body"
        ),
    ],
    withBorder=True,
    shadow="md",
    className="t t1"
)

comp2_figure_pie = dmc.Card(
    [
        dcc.Graph(figure=simple_layout(figure2_pie()), id="comp2_figure_pie", className="g"),
    ],
    withBorder=True,
    shadow="md",
    className="t t2"
)

compS_t1t2_inline = html.Div(
    [
        comp1_text_intro,
        comp2_figure_pie
    ],
    className="st t1t2"
)

block0 = html.Div(
    [
        comp0_figure_time,
        compS_t1t2_inline
    ],
    className="d d0"
)

# # # # # # # # # # # # # # block1 # # # # # # # # # # # # # #

comp3_figure_smhist = dmc.Card(
    [
        dcc.Graph(figure={}, id="comp3_CBOfigure_smhist", className="g")
    ],
    withBorder=True,
    shadow="md",
    className="t t3"
)

comp4_figure_smstrip = dmc.Card(
    [
        dcc.Graph(figure={}, id="comp4_CB0figure_smstrip", className="g")
    ],
    withBorder=True,
    shadow="md",
    className="t t4"
)

block1 = html.Div(
    [
        comp3_figure_smhist,
        comp4_figure_smstrip
    ],
    className="d d1"
)

# # # # # # # # # # # # # # block2 # # # # # # # # # # # # # #

comp5_figure_bubble = dmc.Card(
    [
        dcc.Graph(figure={}, id="comp5_CB0figure_bubble", className="g")
    ],
    withBorder=True,
    shadow="md",
    className="t t5"
)

comp6_input_dropdown = dmc.Card(
    [
        dmc.MultiSelect(
            label="VERSION",
            data=uber_df3.sort_values(by="reviewCreatedVersion", ascending=False)["reviewCreatedVersion"].unique(),
            value = uber_df3.sort_values(by="reviewCreatedVersion", ascending=False)["reviewCreatedVersion"].unique()[0:1],
            clearable=True,
            searchable=False,
            placeholder="Filter by version",
            id="comp6_CBIinput_dropdown",
        )
    ],
    withBorder=True,
    shadow="md",
    className="t t6"
)

comp7_table_versions = dmc.Card(
    [
        dmc.Table(
            data={
                "head": ["Version", "s_mean", "s_stdev", "tu_mean", "tu_stdev","count"],
                "body": table7_appversions().values.tolist(),
            },
            horizontalSpacing=0,
            withColumnBorders=True,
            highlightOnHover=True,
            withTableBorder=True,
            mod={"size": "xs"}
        )
    ],
    withBorder=True,
    shadow="md",
    className="t t7"
)

compS_t6t7_dropdownandtable = html.Div(
    [
        comp6_input_dropdown,
        comp7_table_versions
    ],
    className="st st1"
)

comp8_figure_3d = dmc.Card(
    [
        dcc.Graph(figure={}, id="comp8_CBOfigure_3d", className="g")
    ],
    withBorder=True,
    shadow="md",
    className="t t8"
)

block2 = html.Div(
    [
        comp5_figure_bubble,
        compS_t6t7_dropdownandtable,
        comp8_figure_3d
    ],
    className="d d2"
)

# # # # # # # # # # # # # # block3 # # # # # # # # # # # # # #

# # # # # # # # # # # # # # footer # # # # # # # # # # # # # #
color = "white"

icon_github = DashIconify(icon="simple-icons:github", width=30, color=color, className="bb")
link_github = "https://www.github.com/ua-chjb"
icon_linkedin = DashIconify(icon="devicon-plain:linkedin", width=30, color=color, className="bb")
link_linkedin = "https://linkedin.com/in/benjaminbnoyes"
icon_email = DashIconify(icon="mdi:email", width=30, color=color, className="bb")
link_email = "mailto:noyesbenjamin7@gmail.com"
icon_spotify = DashIconify(icon="cib:spotify", width=30, color=color, className="bb")
link_spotify = "https://open.spotify.com/playlist/2s1oHEgwqxVKoqNdOC1Zs4?si=17fbc35fb4c9421c"
icon_soundcloud = DashIconify(icon="cib:soundcloud", width=40, color=color, className="bb")
link_soundcloud = "https://soundcloud.com/bennoyes-onb"  


comp20_footer0_github = dmc.Anchor(
    icon_github, href=link_github, target="_blank", 
    size="xl",
    className="footnt comp20_footer0_github"
)

comp21_footer1_linkedin = dmc.Anchor(
    icon_linkedin, href=link_linkedin, target="_blank", 
    size="xl",
    className="footnt comp21_footer1_linkedin"
)

comp22_footer2_email = dmc.Anchor(
    icon_email, href=link_email, target="_blank", 
    size="sm",
    className="footnt comp22_footer2_email"
)

comp23_footer3_spotify = dmc.Anchor(
    icon_spotify, href=link_spotify, target="_blank", 
    size="xl",
    className="footnt comp23_footer3_spotify"
)

comp24_footer4_soundcloud = dmc.Anchor(
    icon_soundcloud, href=link_soundcloud, target="_blank",
    size="xl",
    className="footnt comp24_footer4_soundcloud"
)

comp25_copyrightfooter = html.P(
    "© Benjamin Noyes 2024 all rights reserved",
    className="footertinytext"
)

footer = dmc.Card(
    [
        comp20_footer0_github,
        comp21_footer1_linkedin,
        comp22_footer2_email,
        comp23_footer3_spotify,
        comp24_footer4_soundcloud,
        comp25_copyrightfooter
    ],
    withBorder=True,
    shadow="sm",
    radius="md",
    className="t f"
)

# # # # # # # # # # # # # # title # # # # # # # # # # # # # #


title = dmc.Card(
    [
        dmc.Text(
            "uber reviews",
            size="xl",
            fw=600
            )
    ],
    className="t tit",
    withBorder=True,
    shadow="sm",
    radius="md",
)
# # # # # # # # # # # # # # final composition # # # # # # # # # # # # # #

lyt = dmc.MantineProvider(
    [
        title,
        block0,
        block1,
        block2,
        footer
    ]
)
