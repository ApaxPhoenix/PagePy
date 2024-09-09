from typing import List, Union, Optional, Dict
from enum import Enum
from lxml import etree
import html

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
    PX_10 = "10px"
    PX_20 = "20px"
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
    def __init__(
        self,
        tag: str,
        children: Optional[List[Union["BaseElement", str]]] = None,
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
        style: Optional[Dict[str, str]] = None,
        href: Optional[str] = None,
        type: Optional[str] = None
    ) -> None:
        """
        Initializes a BaseElement with optional styling and children elements.

        Args:
            tag (str): HTML tag name.
            children (Optional[List[Union["BaseElement", str]]]): Child elements or text.
            position (Optional[Position]): CSS position property.
            display (Optional[Display]): CSS display property.
            text_align (Optional[TextAlign]): CSS text-align property.
            vertical_align (Optional[VerticalAlign]): CSS vertical-align property.
            z_index (Optional[ZIndex]): CSS z-index property.
            margin (Optional[Union[Size, str, int, float]]): CSS margin property.
            padding (Optional[Union[Size, str, int, float]]): CSS padding property.
            overflow (Optional[Overflow]): CSS overflow property.
            width (Optional[Union[Size, str, int, float]]): CSS width property.
            height (Optional[Union[Size, str, int, float]]): CSS height property.
            max_width (Optional[Union[Size, str, int, float]]): CSS max-width property.
            max_height (Optional[Union[Size, str, int, float]]): CSS max-height property.
            min_width (Optional[Union[Size, str, int, float]]): CSS min-width property.
            min_height (Optional[Union[Size, str, int, float]]): CSS min-height property.
            class_name (Optional[str]): CSS class attribute.
            element_id (Optional[str]): HTML id attribute.
            style (Optional[Dict[str, str]]): Additional inline styles.
            href (Optional[str]): Hyperlink reference.
            type (Optional[str]): Input type attribute.
        """
        self.tag: str = tag
        self.class_name: Optional[str] = class_name
        self.element_id: Optional[str] = element_id
        self.href: Optional[str] = href
        self.type: Optional[str] = type
        self.children: List[Union["BaseElement", str]] = children if children else []

        # Initialize styles dictionary
        self.styles: Dict[str, str] = style if style else {}

        # Add CSS styles directly
        if position: self.styles["position"] = position.value
        if display: self.styles["display"] = display.value
        if text_align: self.styles["text-align"] = text_align.value
        if vertical_align: self.styles["vertical-align"] = vertical_align.value
        if z_index: self.styles["z-index"] = z_index.value

        # Handle margin, padding, width, height, max-width, max-height, min-width, min-height
        if margin:
            self.styles["margin"] = (margin.value if isinstance(margin, Size)
                                    else f"{margin}px" if isinstance(margin, (int, float))
                                    else margin)
        if padding:
            self.styles["padding"] = (padding.value if isinstance(padding, Size)
                                     else f"{padding}px" if isinstance(padding, (int, float))
                                     else padding)
        if overflow: self.styles["overflow"] = overflow.value
        if width:
            self.styles["width"] = (width.value if isinstance(width, Size)
                                   else f"{width}px" if isinstance(width, (int, float))
                                   else width)
        if height:
            self.styles["height"] = (height.value if isinstance(height, Size)
                                    else f"{height}px" if isinstance(height, (int, float))
                                    else height)
        if max_width:
            self.styles["max-width"] = (max_width.value if isinstance(max_width, Size)
                                        else f"{max_width}px" if isinstance(max_width, (int, float))
                                        else max_width)
        if max_height:
            self.styles["max-height"] = (max_height.value if isinstance(max_height, Size)
                                         else f"{max_height}px" if isinstance(max_height, (int, float))
                                         else max_height)
        if min_width:
            self.styles["min-width"] = (min_width.value if isinstance(min_width, Size)
                                        else f"{min_width}px" if isinstance(min_width, (int, float))
                                        else min_width)
        if min_height:
            self.styles["min-height"] = (min_height.value if isinstance(min_height, Size)
                                         else f"{min_height}px" if isinstance(min_height, (int, float))
                                         else min_height)

    def __str__(self) -> str:
        """
        Converts the BaseElement to a pretty-printed HTML string.

        Returns:
            str: Pretty-printed HTML representation of the element.
        """
        lxml_element = etree.Element(self.tag)

        # Set attributes
        if self.class_name: lxml_element.set("class", self.class_name)
        if self.element_id: lxml_element.set("id", self.element_id)
        if self.href: lxml_element.set("href", self.href)
        if self.type: lxml_element.set("type", self.type)

        # Add style attributes
        if self.styles:
            style_string = "; ".join(f"{html.escape(key)}: {html.escape(value)}" for key, value in self.styles.items())
            lxml_element.set("style", style_string)

        # Append children
        for child in self.children:
            if isinstance(child, BaseElement):
                child_element = etree.fromstring(str(child))
                lxml_element.append(child_element)
            else:
                lxml_element.text = (lxml_element.text or "") + html.escape(str(child))

        # Convert to HTML string
        html_string = etree.tostring(lxml_element, method="html", encoding="unicode")

        # Parse and pretty-print HTML
        html_parser = etree.HTMLParser(remove_blank_text=True)
        document = etree.fromstring(html_string, parser=html_parser)
        indented_html = etree.tostring(document, pretty_print=True, encoding="unicode")

        return indented_html

# Example usage
child1 = BaseElement(tag="p", children=["This is a paragraph."])
child2 = BaseElement(tag="div", children=["This is a div."])

element = BaseElement(
    tag="div",
    children=[child1, child2, "Some text here."],
    position=Position.RELATIVE,
    display=Display.BLOCK,
    text_align=TextAlign.CENTER,
    margin=Size.PX_20,
    padding=Size.PX_10,
    overflow=Overflow.AUTO,
    width=Size.FULL,
    height=Size.AUTO,
    class_name="container",
    element_id="main-container",
    style={"background-color": "lightgrey"}
)

print(element)
