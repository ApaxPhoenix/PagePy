from enum import Enum
from typing import List, Union, Optional

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

class JustifyContent(Enum):
    FLEX_START = "flex-start"
    FLEX_END = "flex-end"
    CENTER = "center"
    SPACE_BETWEEN = "space-between"
    SPACE_AROUND = "space-around"
    SPACE_EVENLY = "space-evenly"
    START = "start"
    END = "end"
    LEFT = "left"
    RIGHT = "right"

class AlignItems(Enum):
    FLEX_START = "flex-start"
    FLEX_END = "flex-end"
    CENTER = "center"
    BASELINE = "baseline"
    STRETCH = "stretch"
    START = "start"
    END = "end"
    SELF_START = "self-start"
    SELF_END = "self-end"

class Margin(Enum):
    AUTO = "auto"
    ZERO = "0"
    SMALL = "0.5rem"
    MEDIUM = "1rem"
    LARGE = "2rem"
    X_LARGE = "4rem"

class Padding(Enum):
    NONE = "0"
    SMALL = "0.5rem"
    MEDIUM = "1rem"
    LARGE = "2rem"
    X_LARGE = "4rem"

class Overflow(Enum):
    VISIBLE = "visible"
    HIDDEN = "hidden"
    SCROLL = "scroll"
    AUTO = "auto"
    CLIP = "clip"

class Direction(Enum):
    FLEX = "flex"
    FLEX_ROW = "flex-row"
    FLEX_COLUMN = "flex-column"
    FLEX_ROW_REVERSE = "flex-row-reverse"
    FLEX_COLUMN_REVERSE = "flex-column-reverse"
    GRID = "grid"
    GRID_COLS = "grid-cols"
    GRID_ROWS = "grid-rows"
    GRID_DENSE = "grid-dense"

class AlignContent(Enum):
    FLEX_START = "flex-start"
    FLEX_END = "flex-end"
    CENTER = "center"
    SPACE_BETWEEN = "space-between"
    SPACE_AROUND = "space-around"
    STRETCH = "stretch"

class BaseElement:
    """
    A base class for HTML elements with optional CSS styling.
    
    Attributes:
        tag (str): The HTML tag name for this element.
        children (List[Union['BaseElement', str]]): The child elements or text contained within this element.
        styles (dict): Optional CSS styles applied to this element.
    """
    block_elements = {"div", "p", "h1", "h2", "h3", "h4", "h5", "h6", "ul", "ol", "table", "form"}
    inline_elements = {"span", "a", "strong", "em", "b", "i", "img", "br", "input"}
    list_elements = {"ul", "ol"}
    table_elements = {"table", "thead", "tbody", "tfoot", "tr", "th", "td"}
    form_elements = {"form", "input", "textarea", "button", "select", "fieldset"}

    def __init__(
        self, 
        tag: str, 
        *children: Union['BaseElement', str], 
        position: Optional[Position] = None, 
        display: Optional[Display] = None, 
        text_align: Optional[TextAlign] = None,
        vertical_align: Optional[VerticalAlign] = None,
        margin: Optional[Margin] = None,
        padding: Optional[Padding] = None,
        justify_content: Optional[JustifyContent] = None,
        align_items: Optional[AlignItems] = None,
        overflow: Optional[Overflow] = None,
        direction: Optional[Direction] = None,
        align_content: Optional[AlignContent] = None
    ):
        """
        Initialize a new HTML element with optional CSS styles.

        Args:
            tag (str): The HTML tag name for this element.
            *children (Union['BaseElement', str]): Optional child elements or text.
            position (Optional[Position]): The CSS position property.
            display (Optional[Display]): The CSS display property.
            text_align (Optional[TextAlign]): The CSS text-align property.
            vertical_align (Optional[VerticalAlign]): The CSS vertical-align property.
            margin (Optional[Margin]): The CSS margin property.
            padding (Optional[Padding]): The CSS padding property.
            justify_content (Optional[JustifyContent]): The CSS justify-content property.
            align_items (Optional[AlignItems]): The CSS align-items property.
            overflow (Optional[Overflow]): The CSS overflow property.
            direction (Optional[Direction]): The CSS flex-direction or grid property.
            align_content (Optional[AlignContent]): The CSS align-content property.
        """
        self.tag = tag
        self.children: List[Union['BaseElement', str]] = list(children)
        self.styles = {}

        # Optional CSS styles based on the type of element
        if position:
            self.styles["position"] = position.value
        if display:
            self.styles["display"] = display.value
        if text_align and (self.tag in self.block_elements or self.tag in {"th", "td"}):
            self.styles["text-align"] = text_align.value
        if vertical_align and (self.tag in self.inline_elements or self.tag in {"th", "td"}):
            self.styles["vertical-align"] = vertical_align.value
        if margin:
            self.styles["margin"] = margin.value
        if padding:
            self.styles["padding"] = padding.value
        if direction and direction in {Direction.FLEX, Direction.FLEX_ROW, Direction.FLEX_COLUMN, Direction.FLEX_ROW_REVERSE, Direction.FLEX_COLUMN_REVERSE}:
            self.styles["display"] = "flex"
            if direction != Direction.FLEX:
                self.styles["flex-direction"] = direction.value.replace("flex-", "")
        elif direction in {Direction.GRID, Direction.GRID_COLS, Direction.GRID_ROWS, Direction.GRID_DENSE}:
            self.styles["display"] = "grid"
            if direction == Direction.GRID_COLS:
                self.styles["grid-auto-flow"] = "column"
            elif direction == Direction.GRID_ROWS:
                self.styles["grid-auto-flow"] = "row"
            elif direction == Direction.GRID_DENSE:
                self.styles["grid-auto-flow"] = "dense"
        if justify_content and self.styles.get("display") in {"flex", "grid", "inline-flex", "inline-grid"}:
            self.styles["justify-content"] = justify_content.value
        if align_items and self.styles.get("display") in {"flex", "grid", "inline-flex", "inline-grid"}:
            self.styles["align-items"] = align_items.value
        if overflow and self.tag in self.block_elements:
            self.styles["overflow"] = overflow.value
        if align_content and self.styles.get("display") in {"flex", "grid", "inline-flex", "inline-grid"}:
            self.styles["align-content"] = align_content.value

    def add_child(self, child: Union['BaseElement', str]) -> None:
        """
        Add a child element to this element with validation.

        Args:
            child (Union['BaseElement', str]): The child element or text to add.

        Raises:
            ValueError: If the child cannot be contained within this element.
        """
        if isinstance(child, BaseElement):
            if not self._can_contain(child):
                raise ValueError(f"Cannot add <{child.tag}> inside <{self.tag}>.")
        self.children.append(child)
    
    def _can_contain(self, child: 'BaseElement') -> bool:
        """
        Determine if this element can contain the specified child element.

        Args:
            child (BaseElement): The child element to check.

        Returns:
            bool: True if the child can be contained, False otherwise.
        """
        if self.tag in self.block_elements:
            return True
        elif self.tag in self.inline_elements:
            return False
        elif self.tag in self.list_elements:
            return child.tag == "li"
        elif self.tag in self.table_elements:
            return child.tag in {"thead", "tbody", "tfoot", "tr", "th", "td"}
        elif self.tag == "form":
            return child.tag in self.form_elements and child.tag != "form"
        elif self.tag == "head":
            return child.tag in {"title", "meta", "link"}
        elif self.tag == "body":
            return True
        return False

    def __str__(self) -> str:
        """
        Return the HTML representation of this element and its children.

        Returns:
            str: A string containing the HTML representation.
        """
        style_str = f' style="{"; ".join(f"{k}: {v}" for k, v in self.styles.items())}"' if self.styles else ""
        children_str = ''.join(str(child) for child in self.children)
        return f"<{self.tag}{style_str}>{children_str}</{self.tag}>"
    
    def __repr__(self) -> str:
        """
        Return a string representation of this element for debugging.

        Returns:
            str: A string representing this element.
        """
        return f"BaseElement(tag='{self.tag}')"
