# PagePy: Simplified Web Development in Python

PagePy is an experimental Python framework designed for streamlined web development. Build lightweight and efficient web applications effortlessly.

## Why Choose PagePy?

* **Object-Oriented HTML Generation**: Create HTML structures using Python classes, making your code more intuitive and maintainable.
* **Minimalist Approach**: Focus on building your application without unnecessary complexity.
* **Flexible Structure**: Clean and straightforward setup for easy organization and maintenance.
* **Customizable Elements**: Easily extend and customize HTML elements to suit your specific needs.
* **Scalable and Extensible**: Start small and scale up as your project grows. Easily extendable with additional features as needed.

## Getting Started

Get up and running with PagePy in just a few simple steps:

1. **Installation**

Install PagePy using pip:

```
pip install pagepy
```

2. **Write Your Web Application**

Create a Python file (e.g., `app.py`) and start coding:

```python
from pagepy import Html, Head, Body, Div, H1, P

# Create an HTML structure
html = Html(
    children=[
        Head(
            children=[
                BaseElement("title", children=["My PagePy Website"])
            ]
        ),
        Body(
            children=[
                Div(
                    class_name="header",
                    children=[
                        H1(children=["Welcome to PagePy"], style={"text-align": "center"})
                    ],
                    style={"background-color": "#f0f0f0", "padding": "20px"}
                ),
                Div(
                    class_name="content",
                    children=[
                        P(children=["Build web pages easily with PagePy!"])
                    ],
                    style={"margin": "20px", "padding": "20px", "border": "1px solid #ddd"}
                )
            ]
        )
    ]
)

# Generate the HTML
print(html)
```

3. **Generate Your HTML**

Execute your script:

```
python app.py > index.html
```

Your PagePy-generated HTML will be saved in `index.html`.

## License

WebPy is released under the CC0-1.0 License. See [LICENSE](LICENSE) for details.
