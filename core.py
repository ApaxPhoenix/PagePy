from typing import List, Union, Optional, Dict, Any
from bs4 import BeautifulSoup, NavigableString, Tag


class Element:
    """
    Represents an HTML element with attributes, styles, and child elements.
    Uses BeautifulSoup for robust HTML handling and parsing.

    Args:
        tag (str): The HTML tag for the element (e.g., 'div', 'p').
        children (Optional[List[Union['Element', str]]]): Child elements or text content.
        **attrs: Variable keyword arguments for HTML attributes:
            - class_name (Optional[str]): CSS class for styling
            - element_id (Optional[str]): Unique identifier
            - style (Optional[Dict[str, Union[str, int]]]): Inline CSS styles
            - href (Optional[str]): URL for links
            - type (Optional[str]): Type attribute
            - target (Optional[str]): Link target
    """

    def __init__(
            self,
            tag: str,
            children: Optional[List[Union["Element", str]]] = None,
            **attrs: Optional[Union[str, Dict[str, Any]]]
    ) -> None:
        self.soup: BeautifulSoup = BeautifulSoup(features="html.parser")
        self.tag: str = tag
        self.children: List[Union["Element", str]] = children or []
        # Process attributes and styles
        self.attrs: Dict[str, str] = {}
        for k, v in attrs.items():
            if v is not None:
                if k == 'style' and isinstance(v, dict):
                    self.attrs[k] = '; '.join(f"{sk}: {sv}" for sk, sv in v.items())
                else:
                    self.attrs[k] = str(v)

    def __str__(self) -> str:
        """
        Convert the Element to its HTML string representation.

        Returns:
            str: HTML string of the element and its children.
        """
        # Create element with attributes
        elem: Tag = self.soup.new_tag(self.tag, **self.attrs)

        # Add children recursively
        for child in self.children:
            if isinstance(child, Element):
                # Parse and append child element
                child_soup = BeautifulSoup(str(child), "html.parser")
                elem.append(child_soup.find(child.tag))
            else:
                # Append text content as NavigableString
                elem.append(NavigableString(str(child)))

        return str(elem)

    def add_tag(self, tag: str, content: str) -> None:
        """
        Add a custom tag with content to the element's children.

        Args:
            tag (str): The HTML tag to create.
            content (str): The content to be wrapped in the tag.
        """
        soup = BeautifulSoup(f"<{tag}>{content}</{tag}>", "html.parser")
        if soup.find(tag):
            self.children.append(Element(tag, [content]))

    def add_arguments(self, tag: str, arguments: Dict[str, str]) -> None:
        """
        Add a new element with specified attributes to children.

        Args:
            tag (str): The HTML tag to create.
            arguments (Dict[str, str]): Dictionary of HTML attributes and values.
        """
        self.children.append(Element(tag, **arguments))
