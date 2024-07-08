package main

type Resume struct {
	Name        string       `yaml:"name"`
	Address     string       `yaml:"address"`
	Phone       string       `yaml:"phone"`
	Email       string       `yaml:"email"`
	Website     string       `yaml:"website"`
	Social      string       `yaml:"social"`
	Profile     string       `yaml:"profile"`
	Experiences []Experience `yaml:"experiences"`
	Projects    []Project    `yaml:"projects"`
	Education   Education    `yaml:"education"`
	Skills      []Skill      `yaml:"skills"`
}

type Experience struct {
	Summarize  bool     `yaml:"summarize"`
	Name       string   `yaml:"name"`
	Address    string   `yaml:"address"`
	Role       string   `yaml:"role"`
	Start      string   `yaml:"start"`
	End        string   `yaml:"end"`
	Desc       string   `yaml:"desc"`
	Attributes []string `yaml:"attributes"`
	Skills     []string `yaml:"skills"`
}

type Project struct {
	Summarize  bool     `yaml:"summarize"`
	Name       string   `yaml:"name"`
	Url        string   `yaml:"url"`
	Role       string   `yaml:"role"`
	Start      string   `yaml:"start"`
	End        string   `yaml:"end"`
	Desc       string   `yaml:"desc"`
	Attributes []string `yaml:"attributes"`
	Skills     []string `yaml:"skills"`
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
