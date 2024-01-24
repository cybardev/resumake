# Resume

## Generate resume using data representation objects in Python

### Dependencies

-   `python >= 3.9`
-   `pandoc`
-   `wkhtmltopdf`
-   `poppler-utils`

### Installation

-   clone this repo
-   add full path of `src/` directory to `PYTHONPATH` environment variable

> **TODO**: publish it on PyPI for easy installation

### Usage

-   create `.py` file
-   import all from `resume.components`:
    ```py
    from resume.components import *
    ```
-   create `author` variable and assign it an `Author` object
-   fill `Author` object parameters with info (see [resume_cybardev.py][resume_py])
-   run `resume.builder` following examples below

Output of `python3 -m resume.builder -h`:

```
usage: resume.builder [-h] [-s SCHEMA] [-o OUTPUT] [-t HTML] [-c CSS] RESUME

Generate a resume from a given Python file containing data representation objects

positional arguments:
  RESUME                path to the Python file containing the resume data

options:
  -h, --help            show this help message and exit
  -s SCHEMA, --schema SCHEMA
                        order of sections to display in the resume
  -o OUTPUT, --output OUTPUT
                        path to the output directory
  -t HTML, --template HTML
                        path to the HTML template file
  -c CSS, --css CSS     path to the CSS template file
```

#### Examples

-   see default help message

    ```sh
    python3 -m resume.builder -h
    ```

-   generate resume from `example.py` to current directory

    ```sh
    python3 -m resume.builder example.py
    ```

-   generate resume from `example.py` to `build/` directory

    ```sh
    python3 -m resume.builder example.py -o ./build
    ```

-   generate resume from `example.py` to `build/` directory using custom `html` and `css` templates

    ```sh
    python3 -m resume.builder example.py -o ./build -t custom.html -c custom.css
    ```

-   generate resume from `example.py` with custom section order and omitting a default section (projects)

    ```sh
    python3 -m resume.builder example.py -s "education, experience, skills"
    ```

### Using GitHub Actions

#### Automatically generate your resume and publish it as a website

-   fork this repo
-   navigate to your fork
-   rename `resume_cybardev.py` to have your GitHub username instead of `cybardev`
-   modify the renamed Python file to include your resume info
-   push changes to your fork

#### Extras

-   check `Actions` tab of your fork for workflow run details
-   configure custom domain (if desired) from `Settings > Pages`

### Using Docker Container

#### Dependencies

-   `docker`
    -   Docker Engine, at least; Docker Desktop optional

#### Installation

```sh
docker pull cybardev/resume
```

#### Usage

```sh
docker run --rm -v $PWD/static:/app/static cybardev/resume [args]
```

> **PS**: for available `[args]`, see main Usage and Examples sections above, or run it with the `-h` flag

Since the command is so tedious to type, I suggest setting up a shell alias or function for ease of use.

### Sample Output

**Source**: [resume_cybardev.py][resume_py]

![resume][resume_png]

<!-- links -->

[resume_py]: resume_cybardev.py
[resume_png]: static/assets/Resume_Sheikh_Saad_Abdullah.png "Resume - Sheikh Saad Abdullah"
