from core import Element

# Structure Elements
class Html(Element):
    """Root element of an HTML document"""
    def __init__(self, **kwargs):
        super().__init__("html", **kwargs)

class Head(Element):
    """Container for metadata and document head elements"""
    def __init__(self, **kwargs):
        super().__init__("head", **kwargs)

class Body(Element):
    """Container for the document's content"""
    def __init__(self, **kwargs):
        super().__init__("body", **kwargs)

class Header(Element):
    """Introductory content or navigation links"""
    def __init__(self, **kwargs):
        super().__init__("header", **kwargs)

class Footer(Element):
    """Footer content for its nearest sectioning content"""
    def __init__(self, **kwargs):
        super().__init__("footer", **kwargs)

class Section(Element):
    """Standalone section of content"""
    def __init__(self, **kwargs):
        super().__init__("section", **kwargs)

class Article(Element):
    """Self-contained composition"""
    def __init__(self, **kwargs):
        super().__init__("article", **kwargs)

class Aside(Element):
    """Content indirectly related to main content"""
    def __init__(self, **kwargs):
        super().__init__("aside", **kwargs)

class Nav(Element):
    """Navigation links section"""
    def __init__(self, **kwargs):
        super().__init__("nav", **kwargs)

class Div(Element):
    """Generic container for flow content"""
    def __init__(self, **kwargs):
        super().__init__("div", **kwargs)

class Span(Element):
    """Generic inline container"""
    def __init__(self, **kwargs):
        super().__init__("span", **kwargs)

class Main(Element):
    """Main content of the document"""
    def __init__(self, **kwargs):
        super().__init__("main", **kwargs)

# Text Elements
class H1(Element):
    """First-level heading"""
    def __init__(self, **kwargs):
        super().__init__("h1", **kwargs)

class H2(Element):
    """Second-level heading"""
    def __init__(self, **kwargs):
        super().__init__("h2", **kwargs)

class H3(Element):
    """Third-level heading"""
    def __init__(self, **kwargs):
        super().__init__("h3", **kwargs)

class H4(Element):
    """Fourth-level heading"""
    def __init__(self, **kwargs):
        super().__init__("h4", **kwargs)

class H5(Element):
    """Fifth-level heading"""
    def __init__(self, **kwargs):
        super().__init__("h5", **kwargs)

class H6(Element):
    """Sixth-level heading"""
    def __init__(self, **kwargs):
        super().__init__("h6", **kwargs)

class P(Element):
    """Paragraph of text"""
    def __init__(self, **kwargs):
        super().__init__("p", **kwargs)

class Blockquote(Element):
    """Extended quotation"""
    def __init__(self, **kwargs):
        super().__init__("blockquote", **kwargs)

class Pre(Element):
    """Preformatted text"""
    def __init__(self, **kwargs):
        super().__init__("pre", **kwargs)

class Hr(Element):
    """Thematic break between paragraphs"""
    def __init__(self, **kwargs):
        super().__init__("hr", **kwargs)

class Code(Element):
    """Computer code"""
    def __init__(self, **kwargs):
        super().__init__("code", **kwargs)

class Em(Element):
    """Emphasized text"""
    def __init__(self, **kwargs):
        super().__init__("em", **kwargs)

class Strong(Element):
    """Strong importance"""
    def __init__(self, **kwargs):
        super().__init__("strong", **kwargs)

class Small(Element):
    """Side-comments and small print"""
    def __init__(self, **kwargs):
        super().__init__("small", **kwargs)

class S(Element):
    """Strikethrough text"""
    def __init__(self, **kwargs):
        super().__init__("s", **kwargs)

class Sub(Element):
    """Subscript text"""
    def __init__(self, **kwargs):
        super().__init__("sub", **kwargs)

class Sup(Element):
    """Superscript text"""
    def __init__(self, **kwargs):
        super().__init__("sup", **kwargs)

# Lists
class Ul(Element):
    """Unordered list"""
    def __init__(self, **kwargs):
        super().__init__("ul", **kwargs)

class Ol(Element):
    """Ordered list"""
    def __init__(self, **kwargs):
        super().__init__("ol", **kwargs)

class Li(Element):
    """List item"""
    def __init__(self, **kwargs):
        super().__init__("li", **kwargs)

class Dl(Element):
    """Description list"""
    def __init__(self, **kwargs):
        super().__init__("dl", **kwargs)

class Dt(Element):
    """Description term"""
    def __init__(self, **kwargs):
        super().__init__("dt", **kwargs)

class Dd(Element):
    """Description details"""
    def __init__(self, **kwargs):
        super().__init__("dd", **kwargs)

# Tables
class Table(Element):
    """Table container"""
    def __init__(self, **kwargs):
        super().__init__("table", **kwargs)

class Tr(Element):
    """Table row"""
    def __init__(self, **kwargs):
        super().__init__("tr", **kwargs)

class Th(Element):
    """Table header cell"""
    def __init__(self, **kwargs):
        super().__init__("th", **kwargs)

class Td(Element):
    """Table data cell"""
    def __init__(self, **kwargs):
        super().__init__("td", **kwargs)

class Thead(Element):
    """Table head"""
    def __init__(self, **kwargs):
        super().__init__("thead", **kwargs)

class Tbody(Element):
    """Table body"""
    def __init__(self, **kwargs):
        super().__init__("tbody", **kwargs)

class Tfoot(Element):
    """Table footer"""
    def __init__(self, **kwargs):
        super().__init__("tfoot", **kwargs)

class Col(Element):
    """Table column"""
    def __init__(self, **kwargs):
        super().__init__("col", **kwargs)

class Colgroup(Element):
    """Table column group"""
    def __init__(self, **kwargs):
        super().__init__("colgroup", **kwargs)

# Forms
class Form(Element):
    """Form container"""
    def __init__(self, **kwargs):
        super().__init__("form", **kwargs)

class Input(Element):
    """Input control"""
    def __init__(self, **kwargs):
        super().__init__("input", **kwargs)

class Textarea(Element):
    """Multiline text input"""
    def __init__(self, **kwargs):
        super().__init__("textarea", **kwargs)

class Button(Element):
    """Clickable button"""
    def __init__(self, **kwargs):
        super().__init__("button", **kwargs)

class Select(Element):
    """Dropdown list"""
    def __init__(self, **kwargs):
        super().__init__("select", **kwargs)

class Option(Element):
    """Option in a select element"""
    def __init__(self, **kwargs):
        super().__init__("option", **kwargs)

class Label(Element):
    """Label for a form control"""
    def __init__(self, **kwargs):
        super().__init__("label", **kwargs)
