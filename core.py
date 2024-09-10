from typing import List, Union, Optional, Dict
from bs4 import BeautifulSoup, Tag, NavigableString

class BaseElement:
    """
    A base class to represent an HTML element with attributes, styles, and child elements.

    Args:
        tag (str): The HTML tag for the element (e.g., 'div', 'p').
        children (Optional[List[Union['BaseElement', str]]]): Child elements or text content.
        class_name (Optional[str]): CSS class for styling the element.
        element_id (Optional[str]): Unique identifier for the element.
        style (Optional[Dict[str, Union[str, int]]]): Inline CSS styles.
        href (Optional[str]): URL for links.
        type (Optional[str]): Type attribute (e.g., 'text', 'submit').
        target (Optional[str]): Specifies where to open linked documents (e.g., '_blank').
    """
    def __init__(
        self,
        tag: str,
        children: Optional[List[Union["BaseElement", str]]] = None,
        class_name: Optional[str] = None,
        element_id: Optional[str] = None,
        style: Optional[Dict[str, Union[str, int]]] = None,
        href: Optional[str] = None,
        type: Optional[str] = None,
        target: Optional[str] = None
    ) -> None:
        self.tag: str = tag
        self.class_name: Optional[str] = class_name
        self.element_id: Optional[str] = element_id
        self.href: Optional[str] = href
        self.type: Optional[str] = type
        self.target: Optional[str] = target
        self.children: List[Union["BaseElement", str]] = children if children else []
        self.styles: Dict[str, Union[str, int]] = style if style else {}

    def __str__(self) -> str:
        soup = BeautifulSoup(features="html.parser")
        element = soup.new_tag(self.tag)

        # Set attributes
        if self.class_name:
            element['class'] = self.class_name
        if self.element_id:
            element['id'] = self.element_id
        if self.href:
            element['href'] = self.href
        if self.type:
            element['type'] = self.type
        if self.target:
            element['target'] = self.target

        # Add inline styles
        if self.styles:
            style_string = "; ".join(f"{key}: {value}" for key, value in self.styles.items())
            element['style'] = style_string

        # Add child elements or text content
        for child in self.children:
            if isinstance(child, BaseElement):
                child_element = BeautifulSoup(str(child), "html.parser").find(child.tag)
                if child_element:
                    element.append(child_element)
            else:
                element.append(NavigableString(str(child)))

        return str(element)

    def add_tag(self, root_tag: str, content: str) -> None:
        """
        Add a custom tag with content to the element's children.

        Args:
            root_tag (str): The root HTML tag to which content will be added.
            content (str): The tag with content to be inserted.
        """
        content_element = BeautifulSoup(content, "html.parser").find(root_tag)
        if content_element:
            self.children.append(content_element)

    def add_arguments(self, tag: str, arguments: Dict[str, str]) -> None:
        """
        Add attributes to a specified tag and append it to the element's children.

        Args:
            tag (str): The HTML tag to which attributes will be added.
            arguments (Dict[str, str]): A dictionary of attributes and their values.
        """
        element = BeautifulSoup(features="html.parser").new_tag(tag)
        for attr, value in arguments.items():
            element[attr] = value
        self.children.append(element)