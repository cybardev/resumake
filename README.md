# Resumake

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
-   import all from `resumake.components`:
    ```py
    from resumake.components import *
    ```
-   create `author` variable and assign it an `Author` object
-   fill `Author` object parameters with info (see [resume/cybardev.py][resume_py])
-   run `resumake.builder` following examples below

Output of `python3 -m resumake.builder -h`:

```
usage: resumake.builder [-h] [-s SCHEMA] [-o OUTPUT] [-t HTML] [-c CSS] RESUME

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
    python3 -m resumake.builder -h
    ```

-   generate resume from `example.py` to current directory

    ```sh
    python3 -m resumake.builder example.py
    ```

-   generate resume from `example.py` to `build/` directory

    ```sh
    python3 -m resumake.builder example.py -o ./build
    ```

-   generate resume from `example.py` to `build/` directory using custom `html` and `css` templates

    ```sh
    python3 -m resumake.builder example.py -o ./build -t custom.html -c custom.css
    ```

-   generate resume from `example.py` with custom section order and omitting a default section (projects)

    ```sh
    python3 -m resumake.builder example.py -s "education, experience, skills"
    ```

### Using GitHub Actions

#### Automatically generate your resume and publish it as a website

-   fork this repo
-   navigate to your fork
-   rename [`resume/cybardev.py`][resume_py] to have your GitHub username instead of `cybardev`
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
docker pull cybardev/resumake:main
```

#### Usage

-   make a `resume` directory at a suitable location
-   place resume `.py` script file in the `resume` directory
-   run the containerized application from within the `resume` directory as such:
    ```sh
    docker run --rm -v $PWD:/app/resume cybardev/resumake:main [args] <resume.py>
    ```
    -   replace `<resume.py>` with the name of your resume `.py` script
    -   for available `[args]`, see main Usage and Examples sections above, or run it with the `-h` flag
        -   **NOTE**: the `-o` flag shouldn't be used for the containerized application as it controls where the files are generated inside the container, not on your computer (move them manually after generation)
        -   for template files, place them alongside the `.py` resume script and refer to them by their basename
-   resume `.md`, `.pdf`, and `.png` files will be generated adjacent to the `.py` file

> **PS**: Since the command is so tedious to type, I suggest setting up a shell alias or function for ease of use. Make sure to replace `$PWD` with absolute path to the `resume` directory.

### Sample Output

**Source**: [resume/cybardev.py][resume_py]

![resume][resume_png]

<!-- links -->

[resume_py]: https://github.com/cybardev/resume/blob/main/resume/cybardev.py
[resume_png]: https://raw.githubusercontent.com/cybardev/resume/main/static/assets/Resume_Sheikh_Saad_Abdullah.png "Resume - Sheikh Saad Abdullah"
