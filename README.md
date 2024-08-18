# Resumake

## Programmatic Resume Generator

### Usage

#### Using GitHub Actions [recommended]

Automatically generate your resume and publish it as a website:

- fork this repo
- navigate to your fork
- edit [`resume.yml`](./resume.yml) file
- edit the `resume_png` link in this readme to the correct png file
- push changes to your fork

#### Using Docker

- install Docker (at least runtime engine)
- pull the image: `docker pull cybardev/resumake`
- run resumake: `docker run --rm -v $PWD:/app/data cybardev/resumake <resume.yml> [MARGIN]`
  - `resume.yml` must be in current working directory. Can be named anything as long as it's a `.yml/.yaml` file.
  - optional: `MARGIN` is a number to use as `margin-top`. Default is `2`

#### Running Locally

##### Dependencies

- `pandoc`
- `wkhtmltopdf`
- `fonts-roboto` (or install the `Roboto` font family to your system)

##### Instructions

- edit [`resume.yml`](./resume.yml) file
- run `resumake.sh` with bash
  - optional: provide a number to use as `margin-top`. Default is `2`

### Extras

- check `Actions` tab of your fork for workflow run details
- configure custom domain (if desired) from `Settings > Pages`
- edit [`resources/template.html`][template] to change order of sections or show/hide sections in resume

### Sample Output

![resume][resume_png]

<!-- links -->

[template]: ./resources/template.html "Resume Template"
[resume_png]: https://raw.githubusercontent.com/cybardev/resumake/main/static/assets/Resume_Sheikh_Saad_Abdullah.png "Resume - Sheikh Saad Abdullah"
