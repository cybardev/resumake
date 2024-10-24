package main

type Resume struct {
	Author      string       `yaml:"author"`
	Location    string       `yaml:"location"`
	Phone       string       `yaml:"phone"`
	Email       string       `yaml:"email"`
	Website     string       `yaml:"website"`
	Socials     Socials      `yaml:"socials"`
	Profile     string       `yaml:"profile"`
	Experiences []Experience `yaml:"experiences"`
	Projects    []Projects   `yaml:"projects"`
	Education   Education    `yaml:"education"`
	Skills      []Skill      `yaml:"skills"`
}

type Socials struct {
	Github   string `yaml:"github"`
	Linkedin string `yaml:"linkedin"`
}

type Experience struct {
	Summarize   bool     `yaml:"summarize"`
	Name        string   `yaml:"name"`
	Location    string   `yaml:"location"`
	Role        string   `yaml:"role"`
	Start       string   `yaml:"start"`
	End         string   `yaml:"end"`
	Description string   `yaml:"desc"`
	Attributes  []string `yaml:"attributes"`
	Skills      []string `yaml:"skills"`
}

type Projects struct {
	Summarize   bool     `yaml:"summarize"`
	Name        string   `yaml:"name"`
	Url         string   `yaml:"url"`
	Role        string   `yaml:"role"`
	Start       string   `yaml:"start"`
	End         string   `yaml:"end"`
	Description string   `yaml:"desc"`
	Attributes  []string `yaml:"attributes"`
	Skills      []string `yaml:"skills"`
}

type Education struct {
	School   string   `yaml:"school"`
	Location string   `yaml:"location"`
	Program  string   `yaml:"program"`
	Major    string   `yaml:"major"`
	Start    string   `yaml:"start"`
	End      string   `yaml:"end"`
	Courses  []string `yaml:"courses"`
}

type Skill struct {
	Name       string   `yaml:"name"`
	Attributes []string `yaml:"attributes"`
}

// TODO: ensure data in expected format

func (r Resume) Validate() bool {
	return true
}

func (s Socials) Validate() bool {
	return true
}

func (e Experience) Validate() bool {
	return true
}

func (p Projects) Validate() bool {
	return true
}

func (e Education) Validate() bool {
	return true
}

func (s Skill) Validate() bool {
	return true
}
