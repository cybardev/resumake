# Resumake

## Programmatic Resume Generator

![UI screenshot][ui_img]

### Usage

#### Using Docker

- edit [`resume.yml`](./resume.yml) file
- install Docker (at least runtime engine)
- pull the image: `docker pull cybardev/resumake`
- run resumake: `docker run -d --name resumake -p 80:80 cybardev/resumake`
- open browser and navigate to [localhost](http://localhost:80)
- upload edited [`resume.yml`](./resume.yml)
- click the <kbd>Create Resume</kbd> button
- download generated PDF
- shutdown the Docker container when done

#### Using the Web App

**PS**: recommended to use [Docker](#using-docker) to avoid rate limits

- edit [`resume.yml`](./resume.yml) file
- go to [resumake.cybar.dev](https://resumake.cybar.dev)
- upload edited [`resume.yml`](./resume.yml)
- click the <kbd>Create Resume</kbd> button
- download generated PDF

#### Using GitHub Actions

**PS**: recommended to use [Docker](#using-docker) to avoid rate limits

Automatically generate your resume and publish it as a website:

- fork this repo
- navigate to your fork
- edit [`resume.yml`](./resume.yml) file
- edit the `resume_png` link in this readme to the correct png file
- push changes to your fork

#### Running Locally

**PS**: recommended to use [Docker](#using-docker) on non-Linux systems

##### Dependencies

- `go`: `v1.23.2`
- `pandoc`
- `wkhtmltopdf`
- `fonts-roboto` (or install the `Roboto` font family to your system)

##### Instructions

- edit [`resume.yml`](./resume.yml) file
- run the following commands in project directory:
  - `go get .`
  - `go build`
  - `resumake`
- open browser and navigate to [localhost](http://localhost:80)
- upload edited [`resume.yml`](./resume.yml)
- click the <kbd>Create Resume</kbd> button
- download generated PDF

### Extras

- check `Actions` tab of your fork for workflow run details
- configure custom domain (if desired) from `Settings > Pages`
- edit [`resources/template.go.tmpl`][template] to change order of sections or show/hide sections in resume

### Sample Output

![resume][resume_png]

<!-- links -->

[template]: ./resources/template.go.tmpl "Resume Template"
[resume_png]: https://raw.githubusercontent.com/cybardev/resumake/main/static/assets/Resume_Sheikh_Saad_Abdullah.png "Resume - Sheikh Saad Abdullah"
[ui_img]: https://github.com/user-attachments/assets/caa4e42d-9fb4-415b-9377-02c829d13621 "UI screenshot of deployed container"
