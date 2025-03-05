# Resumake

## Programmatic Resume Generator

![UI screenshot][ui_img]

### Usage

#### Using Render

[![Deploy to Render](https://render.com/images/deploy-to-render-button.svg)](https://render.com/deploy?repo=https://github.com/cybardev/resumake)

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

**PS**: recommended to use [Docker](#using-docker) on Windows

##### Dependencies

- `go`: `v1.23.2`
- `weasyprint`

##### Manual

- edit [`resume.yml`](./resume.yml) file
- Download the archive file from the Releases page: [resumake-{os}-{arch}.zip][release]
  - **PS**: Make sure to choose the archive corresponding to your OS and architecture
- extract the archive
- `cd` into the extracted directory
- run the executable (may need to chmod or make it executable otherwise)
- open browser and navigate to [localhost](http://localhost:80)
- upload edited [`resume.yml`](./resume.yml)
- click the <kbd>Create Resume</kbd> button
- download generated PDF

##### Install Go Package

> **Link to package**: [pkg.go.dev/github.com/cybardev/resumake/v4][gopkg]

- Run the following command:

    ```sh
    go install github.com/cybardev/resumake/v4@latest
    ```

- Ensure `$GOPATH/bin` is added to `$PATH`. An easy way is to add this line to `~/.profile`:

    ```sh
    export PATH="$(go env GOPATH)/bin:$PATH"
    ```

> [!IMPORTANT]
> The [pkg.go.dev][gopkg] registry may have an outdated version. If you encounter bugs or feature disparity, please replace `latest` after `@` with `main`, e.g. `github.com/cybardev/resumake/v4@main`, **OR** try the [Manual installation](#manual) method for the latest updates.

##### Build from Source

- edit [`resume.yml`](./resume.yml) file
- run the following commands in project directory:
  - `go get .`
  - `go build`
  - `./resumake`
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
[gopkg]: https://pkg.go.dev/github.com/cybardev/resumake/v4
[release]: https://github.com/cybardev/resumake/releases/
