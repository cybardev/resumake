package main

import "strings"

type Resume struct {
	Author      *string      `yaml:"author,omitempty"`
	Location    *string      `yaml:"location,omitempty"`
	Phone       *string      `yaml:"phone,omitempty"`
	Email       *string      `yaml:"email,omitempty"`
	Website     *string      `yaml:"website,omitempty"`
	Socials     *Socials     `yaml:"socials,omitempty"`
	Profile     *string      `yaml:"profile,omitempty"`
	Experiences []Experience `yaml:"experiences,omitempty"`
	Projects    []Project    `yaml:"projects,omitempty"`
	Education   *Education   `yaml:"education,omitempty"`
	Skills      []Skill      `yaml:"skills,omitempty"`
}

type Socials struct {
	Github   *string `yaml:"github,omitempty"`
	Linkedin *string `yaml:"linkedin,omitempty"`
}

type Experience struct {
	Summarize   *Summarize `yaml:"summarize,omitempty"`
	Name        *string    `yaml:"name,omitempty"`
	Location    *string    `yaml:"location,omitempty"`
	Role        *string    `yaml:"role,omitempty"`
	Start       *string    `yaml:"start,omitempty"`
	End         *string    `yaml:"end,omitempty"`
	Description *string    `yaml:"desc,omitempty"`
	Attributes  StrArr     `yaml:"attributes,omitempty"`
	Skills      StrArr     `yaml:"skills,omitempty"`
}

type Project struct {
	Summarize   *Summarize `yaml:"summarize,omitempty"`
	Name        *string    `yaml:"name,omitempty"`
	Url         *string    `yaml:"url,omitempty"`
	Role        *string    `yaml:"role,omitempty"`
	Start       *string    `yaml:"start,omitempty"`
	End         *string    `yaml:"end,omitempty"`
	Description *string    `yaml:"desc,omitempty"`
	Attributes  StrArr     `yaml:"attributes,omitempty"`
	Skills      StrArr     `yaml:"skills,omitempty"`
}

type Education struct {
	School   *string `yaml:"school,omitempty"`
	Location *string `yaml:"location,omitempty"`
	Program  *string `yaml:"program,omitempty"`
	Major    *string `yaml:"major,omitempty"`
	Start    *string `yaml:"start,omitempty"`
	End      *string `yaml:"end,omitempty"`
	Courses  StrArr  `yaml:"courses,omitempty"`
}

type Skill struct {
	Name       *string `yaml:"name,omitempty"`
	Attributes StrArr  `yaml:"attributes,omitempty"`
}

type Summarize bool

func (s Summarize) Bool() bool {
	return bool(s)
}

type StrArr []string

func (s StrArr) Join() string {
	return strings.Join(s, ", ")
}
