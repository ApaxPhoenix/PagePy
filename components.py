from typing import List, Union, Optional
From core import *

class Container(BaseElement):
    """
    A custom Container component, which is a div with optional flex or grid layout.
    
    Args:
        *children (Union['BaseElement', str]): Child elements contained within the container.
        direction (Optional[Direction]): Flex or grid layout direction.
        justify_content (Optional[JustifyContent]): Flex or grid justify content.
        align_items (Optional[AlignItems]): Flex or grid align items.
        padding (Optional[Padding]): Optional padding for the container.
        margin (Optional[Margin]): Optional margin for the container.
    """
    def __init__(
        self, 
        *children: Union['BaseElement', str],
        direction: Optional[Direction] = Direction.FLEX,
        justify_content: Optional[JustifyContent] = None,
        align_items: Optional[AlignItems] = None,
        padding: Optional[Padding] = Padding.MEDIUM,
        margin: Optional[Margin] = Margin.MEDIUM
    ):
        super().__init__("div", *children, direction=direction, justify_content=justify_content, align_items=align_items, padding=padding, margin=margin)

class Grid(BaseElement):
    """
    A custom Grid component, which is a div with grid layout.
    
    Args:
        *children (Union['BaseElement', str]): Child elements contained within the grid.
        columns (Optional[int]): Number of grid columns.
        gap (Optional[str]): Gap between grid items (e.g., '1rem').
        padding (Optional[Padding]): Optional padding for the grid container.
        margin (Optional[Margin]): Optional margin for the grid container.
    """
    def __init__(
        self,
        *children: Union['BaseElement', str],
        columns: Optional[int] = 3,
        gap: Optional[str] = "1rem",
        padding: Optional[Padding] = Padding.MEDIUM,
        margin: Optional[Margin] = Margin.MEDIUM
    ):
        super().__init__("div", *children, direction=Direction.GRID, padding=padding, margin=margin)
        self.styles["grid-template-columns"] = f"repeat({columns}, 1fr)"
        self.styles["gap"] = gap

class Flex(BaseElement):
    """
    A custom Flex component, which is a div with flexbox layout.
    
    Args:
        *children (Union['BaseElement', str]): Child elements contained within the flex container.
        direction (Optional[Direction]): Flexbox direction (row, column, etc.).
        justify_content (Optional[JustifyContent]): How to justify content in the flex container.
        align_items (Optional[AlignItems]): How to align items in the flex container.
        gap (Optional[str]): Gap between flex items (e.g., '1rem').
        padding (Optional[Padding]): Optional padding for the flex container.
        margin (Optional[Margin]): Optional margin for the flex container.
    """
    def __init__(
        self,
        *children: Union['BaseElement', str],
        direction: Optional[Direction] = Direction.FLEX_ROW,
        justify_content: Optional[JustifyContent] = JustifyContent.FLEX_START,
        align_items: Optional[AlignItems] = AlignItems.STRETCH,
        gap: Optional[str] = "0.5rem",
        padding: Optional[Padding] = Padding.MEDIUM,
        margin: Optional[Margin] = Margin.MEDIUM
    ):
        super().__init__("div", *children, direction=direction, justify_content=justify_content, align_items=align_items, padding=padding, margin=margin)
        self.styles["gap"] = gap


