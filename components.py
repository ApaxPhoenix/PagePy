from typing import List, Union, Optional, Dict
from core import BaseElement

# Structure Elements
class Html(BaseElement):
    def __init__(self, **kwargs):
        super().__init__("html", **kwargs)

class Head(BaseElement):
    def __init__(self, **kwargs):
        super().__init__("head", **kwargs)

class Body(BaseElement):
    def __init__(self, **kwargs):
        super().__init__("body", **kwargs)

class Header(BaseElement):
    def __init__(self, **kwargs):
        super().__init__("header", **kwargs)

class Footer(BaseElement):
    def __init__(self, **kwargs):
        super().__init__("footer", **kwargs)

class Section(BaseElement):
    def __init__(self, **kwargs):
        super().__init__("section", **kwargs)

class Article(BaseElement):
    def __init__(self, **kwargs):
        super().__init__("article", **kwargs)

class Aside(BaseElement):
    def __init__(self, **kwargs):
        super().__init__("aside", **kwargs)

class Nav(BaseElement):
    def __init__(self, **kwargs):
        super().__init__("nav", **kwargs)

class Div(BaseElement):
    def __init__(self, **kwargs):
        super().__init__("div", **kwargs)

class Span(BaseElement):
    def __init__(self, **kwargs):
        super().__init__("span", **kwargs)

class Main(BaseElement):
    def __init__(self, **kwargs):
        super().__init__("main", **kwargs)

# Text Elements
class H1(BaseElement):
    def __init__(self, **kwargs):
        super().__init__("h1", **kwargs)

class H2(BaseElement):
    def __init__(self, **kwargs):
        super().__init__("h2", **kwargs)

class H3(BaseElement):
    def __init__(self, **kwargs):
        super().__init__("h3", **kwargs)

class H4(BaseElement):
    def __init__(self, **kwargs):
        super().__init__("h4", **kwargs)

class H5(BaseElement):
    def __init__(self, **kwargs):
        super().__init__("h5", **kwargs)

class H6(BaseElement):
    def __init__(self, **kwargs):
        super().__init__("h6", **kwargs)

class P(BaseElement):
    def __init__(self, **kwargs):
        super().__init__("p", **kwargs)

class Blockquote(BaseElement):
    def __init__(self, **kwargs):
        super().__init__("blockquote", **kwargs)

class Pre(BaseElement):
    def __init__(self, **kwargs):
        super().__init__("pre", **kwargs)

class Hr(BaseElement):
    def __init__(self, **kwargs):
        super().__init__("hr", **kwargs)

class Code(BaseElement):
    def __init__(self, **kwargs):
        super().__init__("code", **kwargs)

class Em(BaseElement):
    def __init__(self, **kwargs):
        super().__init__("em", **kwargs)

class Strong(BaseElement):
    def __init__(self, **kwargs):
        super().__init__("strong", **kwargs)

class Small(BaseElement):
    def __init__(self, **kwargs):
        super().__init__("small", **kwargs)

class S(BaseElement):
    def __init__(self, **kwargs):
        super().__init__("s", **kwargs)

class Sub(BaseElement):
    def __init__(self, **kwargs):
        super().__init__("sub", **kwargs)

class Sup(BaseElement):
    def __init__(self, **kwargs):
        super().__init__("sup", **kwargs)

# Lists
class Ul(BaseElement):
    def __init__(self, **kwargs):
        super().__init__("ul", **kwargs)

class Ol(BaseElement):
    def __init__(self, **kwargs):
        super().__init__("ol", **kwargs)

class Li(BaseElement):
    def __init__(self, **kwargs):
        super().__init__("li", **kwargs)

class Dl(BaseElement):
    def __init__(self, **kwargs):
        super().__init__("dl", **kwargs)

class Dt(BaseElement):
    def __init__(self, **kwargs):
        super().__init__("dt", **kwargs)

class Dd(BaseElement):
    def __init__(self, **kwargs):
        super().__init__("dd", **kwargs)

# Tables
class Table(BaseElement):
    def __init__(self, **kwargs):
        super().__init__("table", **kwargs)

class Tr(BaseElement):
    def __init__(self, **kwargs):
        super().__init__("tr", **kwargs)

class Th(BaseElement):
    def __init__(self, **kwargs):
        super().__init__("th", **kwargs)

class Td(BaseElement):
    def __init__(self, **kwargs):
        super().__init__("td", **kwargs)

class Thead(BaseElement):
    def __init__(self, **kwargs):
        super().__init__("thead", **kwargs)

class Tbody(BaseElement):
    def __init__(self, **kwargs):
        super().__init__("tbody", **kwargs)

class Tfoot(BaseElement):
    def __init__(self, **kwargs):
        super().__init__("tfoot", **kwargs)

class Col(BaseElement):
    def __init__(self, **kwargs):
        super().__init__("col", **kwargs)

class Colgroup(BaseElement):
    def __init__(self, **kwargs):
        super().__init__("colgroup", **kwargs)

# Forms
class Form(BaseElement):
    def __init__(self, **kwargs):
        super().__init__("form", **kwargs)

class Input(BaseElement):
    def __init__(self, **kwargs):
        super().__init__("input", **kwargs)

class Textarea(BaseElement):
    def __init__(self, **kwargs):
        super().__init__("textarea", **kwargs)

class Button(BaseElement):
    def __init__(self, **kwargs):
        super().__init__("button", **kwargs)

class Select(BaseElement):
    def __init__(self, **kwargs):
        super().__init__("select", **kwargs)

class Option(BaseElement):
    def __init__(self, **kwargs):
        super().__init__("option", **kwargs)

class Label(BaseElement):
    def __init__(self, **kwargs):
        super().__init__("label", **kwargs)

# Media
class Audio(BaseElement):
    def __init__(self, src: str, controls: bool = False, **kwargs):
        super().__init__("audio", src=src, controls=controls, **kwargs)

class Video(BaseElement):
    def __init__(self, src: str, controls: bool = False, **kwargs):
        super().__init__("video", src=src, controls=controls, **kwargs)

class Iframe(BaseElement):
    def __init__(self, src: str, width: Optional[str] = None, height: Optional[str] = None, **kwargs):
        super().__init__("iframe", src=src, width=width, height=height, **kwargs)

class Img(BaseElement):
    def __init__(self, src: str, alt: str, **kwargs):
        super().__init__("img", src=src, alt=alt, **kwargs)

class Source(BaseElement):
    def __init__(self, src: str, type: str, **kwargs):
        super().__init__("source", src=src, type=type, **kwargs)

class Track(BaseElement):
    def __init__(self, src: str, kind: str = "subtitles", srclang: str = "en", label: str = "", **kwargs):
        super().__init__("track", src=src, kind=kind, srclang=srclang, label=label, **kwargs)


html = Html(
    children=[
        Head(
            children=[
                BaseElement("title", children=["My Simple Webpage"])
            ]
        ),
        Body(
            children=[
                Div(
                    class_name="header",
                    children=[
                        H1(children=["Welcome to My Webpage"], style={"text-align": "center"})
                    ],
                    style={"background-color": "#f0f0f0", "padding": "20px"}
                ),
                Div(
                    class_name="content",
                    children=[
                        P(children=["This is a paragraph in the main content area."]),
                        Ul(
                            children=[
                                Li(children=["First item"]),
                                Li(children=["Second item"]),
                                Li(children=["Third item"])
                            ]
                        ),
                    ],
                    style={"margin": "20px", "padding": "20px", "border": "1px solid #ddd"}
                ),
                Div(
                    class_name="footer",
                    children=[
                        P(children=["© 2024 My Simple Webpage"], style={"text-align": "center"})
                    ],
                    style={
                        "background-color": "#f0f0f0",
                        "padding": "10px",
                        "position": "fixed",
                        "bottom": "0",
                        "width": "100%"
                    }
                )
            ]
        )
    ]
)

# Print the resulting HTML
print(html)