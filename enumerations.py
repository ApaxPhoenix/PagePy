from enum import Enum
from typing import List, Union, Optional

# Enums for various CSS properties
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

class TextAlign(Enum):
    LEFT = "left"
    RIGHT = "right"
    CENTER = "center"
    JUSTIFY = "justify"

class VerticalAlign(Enum):
    BASELINE = "baseline"
    TOP = "top"
    MIDDLE = "middle"
    BOTTOM = "bottom"
    
class JustifyContent(Enum):
    FLEX_START = "flex-start"
    FLEX_END = "flex-end"
    CENTER = "center"
    SPACE_BETWEEN = "space-between"
    SPACE_AROUND = "space-around"

class AlignItems(Enum):
    FLEX_START = "flex-start"
    FLEX_END = "flex-end"
    CENTER = "center"
    BASELINE = "baseline"
    STRETCH = "stretch"

class Margin(Enum):
    AUTO = "auto"
    ZERO = "0px"
    SMALL = "5px"
    MEDIUM = "10px"
    LARGE = "20px"

class Padding(Enum):
    NONE = "0px"
    SMALL = "5px"
    MEDIUM = "10px"
    LARGE = "20px"

class Overflow(Enum):
    VISIBLE = "visible"
    HIDDEN = "hidden"
    SCROLL = "scroll"
    AUTO = "auto"
    
class Color(Enum):
    BLACK = "black"
    WHITE = "white"
    RED = "red"
    GREEN = "green"
    BLUE = "blue"
    YELLOW = "yellow"
