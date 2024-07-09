# Resumake

## Generate resume using data representation objects in Python

### Dependencies

-   `python >= 3.9`
-   `pandoc`
-   `wkhtmltopdf`
-   `poppler-utils`

### Installation

Install package `resumake` from PyPI:

```sh
python3 -m pip install resumake
```

### Usage

-   create `.py` file
-   import all from `resumake.components`:
    ```py
    from resumake.components import *
    ```
-   create `author` variable and assign it an `Author` object
-   fill `Author` object parameters with info (see [resume/cybardev.py][resume_py])
-   run `resumake.builder` following examples below

Output of `python3 -m resumake.builder -h`:

```
