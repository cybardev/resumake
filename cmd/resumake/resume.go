package main

type Resume[E ExperienceType, P ProjectType] struct {
	Name        string
	Address     string
	Phone       string
	Email       string
	Website     string
	Social      string
	Profile     string
	Experiences Experiences[E]
	Projects    Projects[P]
	Education   Education
	Skills      Skills
}

type Experiences[T ExperienceType] struct {
	Experiences []T
}

type ExperienceType interface {
	Experience | ExperienceSummary
}

type Experience struct {
	Name       string
	Address    string
	Role       string
	Start      string
	End        string
	Attributes []string
}

type ExperienceSummary struct {
	Name   string
	Role   string
	Start  string
	End    string
	Desc   string
	Skills []string
}

type Projects[T ProjectType] struct {
	Projects []T
}

type ProjectType interface {
	Project | ProjectSummary
}

type Project struct {
	Name       string
	Url        string
	Role       string
	Start      string
	End        string
	Attributes []string
}

type ProjectSummary struct {
	Name   string
	Url    string
	Desc   string
	Skills []string
}

type Education struct {
	School   string
	Location string
	Program  string
	Major    string
	Start    string
	End      string
	Courses  []string
}

type Skills struct {
	Skills []Skill
}

type Skill struct {
	Name       string
	Attributes []string
}
