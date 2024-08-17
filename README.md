# Resumake

## Programmatic Resume Generator

### Dependencies

- `pandoc`
- `wkhtmltopdf`
- `fonts-roboto` (or install the `Roboto` font family to your system)

### Usage

#### Using GitHub Actions [recommended]

Automatically generate your resume and publish it as a website:

- fork this repo
- navigate to your fork
- edit [`resume.yml`](./resume.yml) file
- edit the `resume_png` link in this readme to the correct png file
- push changes to your fork

#### Running Locally

- edit [`resume.yml`](./resume.yml) file
- run `resumake.sh` with bash
  - optional: provide a number to use as `margin-top`

### Extras

- check `Actions` tab of your fork for workflow run details
- configure custom domain (if desired) from `Settings > Pages`
- edit [`resources/template.html`][template] to change order of sections or show/hide sections in resume

### Sample Output

![resume][resume_png]

<!-- links -->

[template]: ./resources/template.html "Resume Template"
[resume_png]: https://raw.githubusercontent.com/cybardev/resumake/main/static/assets/Resume_Sheikh_Saad_Abdullah.png "Resume - Sheikh Saad Abdullah"
