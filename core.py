from typing import Union, List, Optional, Dict
from enum import Enum

# Define the Enums
class Position(Enum):
    STATIC = "static"
    RELATIVE = "relative"
    ABSOLUTE = "absolute"
    FIXED = "fixed"
    STICKY = "sticky"

class Display(Enum):
    BLOCK = "block"
    INLINE = "inline"
    INLINE_BLOCK = "inline-block"
    NONE = "none"
    FLEX = "flex"
    GRID = "grid"
    INLINE_FLEX = "inline-flex"
    INLINE_GRID = "inline-grid"
    TABLE = "table"
    TABLE_CELL = "table-cell"
    TABLE_ROW = "table-row"

class TextAlign(Enum):
    LEFT = "left"
    RIGHT = "right"
    CENTER = "center"
    JUSTIFY = "justify"
    START = "start"
    END = "end"

class VerticalAlign(Enum):
    BASELINE = "baseline"
    TOP = "top"
    MIDDLE = "middle"
    BOTTOM = "bottom"
    TEXT_TOP = "text-top"
    TEXT_BOTTOM = "text-bottom"
    SUB = "sub"
    SUPER = "super"

class ZIndex(Enum):
    AUTO = "auto"
    ZERO = "0"
    ONE = "1"
    TWO = "2"
    THREE = "3"
    FOUR = "4"
    FIVE = "5"
    TEN = "10"

class Overflow(Enum):
    AUTO = "auto"
    HIDDEN = "hidden"
    SCROLL = "scroll"
    VISIBLE = "visible"

class Size(Enum):
    AUTO = "auto"
    INITIAL = "initial"
    INHERIT = "inherit"
    FULL = "100%"
    HALF = "50%"
    THIRD = "33%"
    QUARTER = "25%"
    ZERO = "0"
    PX_50 = "50px"
    PX_100 = "100px"
    PX_200 = "200px"
    PX_300 = "300px"
    EM_1 = "1em"
    EM_2 = "2em"
    REM_1 = "1rem"
    REM_2 = "2rem"
    VW_50 = "50vw"
    VW_100 = "100vw"
    VH_50 = "50vh"
    VH_100 = "100vh"

class BaseElement:
    """
    A base class for HTML elements with optional CSS styling, class, and id attributes.
    """

    def __init__(
        self,
        tag: str,
        *children: Union['BaseElement', str],
        position: Optional[Position] = None,
        display: Optional[Display] = None,
        text_align: Optional[TextAlign] = None,
        vertical_align: Optional[VerticalAlign] = None,
        z_index: Optional[ZIndex] = None,
        margin: Optional[Union[Size, str, int, float]] = None,
        padding: Optional[Union[Size, str, int, float]] = None,
        overflow: Optional[Overflow] = None,
        width: Optional[Union[Size, str, int, float]] = None,
        height: Optional[Union[Size, str, int, float]] = None,
        max_width: Optional[Union[Size, str, int, float]] = None,
        max_height: Optional[Union[Size, str, int, float]] = None,
        min_width: Optional[Union[Size, str, int, float]] = None,
        min_height: Optional[Union[Size, str, int, float]] = None,
        class_name: Optional[str] = None,
        element_id: Optional[str] = None,
        stylesheet: Optional[Dict[str, str]] = None,
        href: Optional[str] = None,
        type: Optional[str] = None
    ) -> None:
        """
        Initialize a new HTML element with optional CSS styles, class, and id attributes.
        """
        self.tag = tag
        self.class_name = class_name
        self.element_id = element_id
        self.children: List[Union['BaseElement', str]] = list(children)
        self.styles = stylesheet if stylesheet else {}
        self.href = href
        self.type = type

        # Optional CSS styles based on the type of element
        if position:
            self.styles["position"] = position.value
        if display:
            self.styles["display"] = display.value
        if text_align and self.tag in {"div", "p", "h1", "h2", "h3", "h4", "h5", "h6", "ul", "ol", "table", "form", "header", "footer", "main", "section", "article", "aside", "nav", "figure", "figcaption", "dialog", "details", "summary", "fieldset"}:
            self.styles["text-align"] = text_align.value
        if vertical_align and self.tag in {"span", "a", "strong", "em", "b", "i", "img", "br", "input", "label", "textarea", "button", "select", "option", "small", "sub", "sup"}:
            self.styles["vertical-align"] = vertical_align.value
        if z_index:
            self.styles["z-index"] = z_index.value
        if margin:
            self.styles["margin"] = margin if isinstance(margin, str) else f"{margin}px"
        if padding:
            self.styles["padding"] = padding if isinstance(padding, str) else f"{padding}px"
        if overflow and self.tag in {"div", "p", "h1", "h2", "h3", "h4", "h5", "h6", "ul", "ol", "table", "form", "header", "footer", "main", "section", "article", "aside", "nav", "figure", "figcaption", "dialog", "details", "summary", "fieldset"}:
            self.styles["overflow"] = overflow.value
        if width is not None:
            self.styles["width"] = width.value if isinstance(width, Size) else f"{width}px"
        if height is not None:
            self.styles["height"] = height.value if isinstance(height, Size) else f"{height}px"
        if max_width is not None:
            self.styles["max-width"] = max_width.value if isinstance(max_width, Size) else f"{max_width}px"
        if max_height is not None:
            self.styles["max-height"] = max_height.value if isinstance(max_height, Size) else f"{max_height}px"
        if min_width is not None:
            self.styles["min-width"] = min_width.value if isinstance(min_width, Size) else f"{min_width}px"
        if min_height is not None:
            self.styles["min-height"] = min_height.value if isinstance(min_height, Size) else f"{min_height}px"

    def render(self) -> str:
        """
        Renders the HTML element and its children as a string.
        """
        attrs: List[str] = []
        if self.class_name:
            attrs.append(f'class="{self.class_name}"')
        if self.element_id:
            attrs.append(f'id="{self.element_id}"')
        if self.styles:
            style = "; ".join(f"{k}: {v}" for k, v in self.styles.items())
            attrs.append(f'style="{style}"')
        if self.href:
            attrs.append(f'href="{self.href}"')
        if self.type:
            attrs.append(f'type="{self.type}"')

        attr_str = " ".join(attrs)

        opening_tag = f"<{self.tag} {attr_str.strip()}>" if attr_str else f"<{self.tag}>"
        closing_tag = f"</{self.tag}>"

        children_html = "".join(child.render() if isinstance(child, BaseElement) else child for child in self.children)
        return f"{opening_tag}{children_html}{closing_tag}"

# Example usage
if __name__ == "__main__":
    header = BaseElement(
        "header",
        BaseElement(
            "h1",
            "Welcome to My Website",
            text_align=TextAlign.CENTER
        ),
        BaseElement(
            "nav",
            BaseElement(
                "ul",
                BaseElement("li", "Home", display=Display.INLINE),
                BaseElement("li", "About", display=Display.INLINE),
                BaseElement("li", "Contact", display=Display.INLINE),
            ),
        ),
        position=Position.STATIC,
        display=Display.BLOCK,
        class_name="main-header",
        element_id="header1"
    )

    link = BaseElement(
        "a",
        "Click here to learn more",
        href="https://example.com",
        display=Display.INLINE
    )

    form = BaseElement(
        "form",
        BaseElement("label", "Name: ", BaseElement("input", type="text")),
        BaseElement("label", "Email: ", BaseElement("input", type="email")),
        BaseElement("button", "Submit", type="submit"),
        display=Display.FLEX
    )

    footer = BaseElement(
        "footer",
        BaseElement("p", "© 2024 My Website", text_align=TextAlign.CENTER),
        BaseElement("p", "Follow us on ", link, text_align=TextAlign.CENTER),
        class_name="main-footer",
        element_id="footer1"
    )

    print(header.render())
    print(form.render())
    print(footer.render())
