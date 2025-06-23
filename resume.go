package main

import (
	"errors"
	"fmt"
	"html/template"
)

type Resume struct {
	Author      *string      `yaml:"author,omitempty"`
	Location    *string      `yaml:"location,omitempty"`
	Links       []Link       `yaml:"links,omitempty"`
	Profile     *string      `yaml:"profile,omitempty"`
	Experiences []Experience `yaml:"experiences,omitempty"`
	Projects    []Project    `yaml:"projects,omitempty"`
	Education   *Education   `yaml:"education,omitempty"`
	Skills      []Skill      `yaml:"skills,omitempty"`
}

type Link struct {
	Text *string `yaml:"text,omitempty"`
	Type *string `yaml:"type,omitempty"`
}

func (l Link) Href() (template.URL, error) {
	switch *l.Type {
	case "mailto", "tel":
		return template.URL(fmt.Sprintf("%s:%s", *l.Type, *l.Text)), nil
	case "url":
		return template.URL(fmt.Sprintf("https://%s", *l.Text)), nil
	}
	return "", errors.New("'kind' must be one of: mailto, tel, url")
}

type Experience struct {
	Summarize   *Summarize `yaml:"summarize,omitempty"`
	Name        *string    `yaml:"name,omitempty"`
	Location    *string    `yaml:"location,omitempty"`
	Role        *string    `yaml:"role,omitempty"`
	Start       *string    `yaml:"start,omitempty"`
	End         *string    `yaml:"end,omitempty"`
	Description *string    `yaml:"desc,omitempty"`
	Attributes  []string   `yaml:"attributes,omitempty"`
	Skills      []string   `yaml:"skills,omitempty"`
}

type Project struct {
	Summarize   *Summarize `yaml:"summarize,omitempty"`
	Name        *string    `yaml:"name,omitempty"`
	Url         *string    `yaml:"url,omitempty"`
	Role        *string    `yaml:"role,omitempty"`
	Start       *string    `yaml:"start,omitempty"`
	End         *string    `yaml:"end,omitempty"`
	Description *string    `yaml:"desc,omitempty"`
	Attributes  []string   `yaml:"attributes,omitempty"`
	Skills      []string   `yaml:"skills,omitempty"`
}

type Education struct {
	School   *string  `yaml:"school,omitempty"`
	Location *string  `yaml:"location,omitempty"`
	Program  *string  `yaml:"program,omitempty"`
	Major    *string  `yaml:"major,omitempty"`
	Start    *string  `yaml:"start,omitempty"`
	End      *string  `yaml:"end,omitempty"`
	Courses  []string `yaml:"courses,omitempty"`
}

type Skill struct {
	Name       *string  `yaml:"name,omitempty"`
	Attributes []string `yaml:"attributes,omitempty"`
}

type Summarize bool

func (s Summarize) Bool() bool {
	return bool(s)
}

// ----- VALIDATION METHODS ----- //

func (r Resume) Validate() error {
	if r.Author == nil {
		return errors.New("'author' is missing")
	}
	if r.Location == nil {
		return errors.New("'location' is missing")
	}
	if r.Links == nil {
		return errors.New("'links' is missing")
	} else {
		for _, l := range r.Links {
			err := l.Validate()
			if err != nil {
				return err
			}
		}
	}
	if r.Profile == nil {
		return errors.New("'profile' is missing")
	}
	if r.Experiences == nil {
		return errors.New("'experiences' is missing")
	} else {
		for _, e := range r.Experiences {
			err := e.Validate()
			if err != nil {
				return err
			}
		}
	}
	if r.Projects == nil {
		return errors.New("'projects' is missing")
	} else {
		for _, p := range r.Projects {
			err := p.Validate()
			if err != nil {
				return err
			}
		}
	}
	if r.Education == nil {
		return errors.New("'education' is missing")
	} else {
		err := r.Education.Validate()
		if err != nil {
			return err
		}
	}
	if r.Skills == nil {
		return errors.New("'skills' is missing")
	} else {
		for _, s := range r.Skills {
			err := s.Validate()
			if err != nil {
				return err
			}
		}
	}

	// if nothing is missing:
	return nil
}

func (l Link) Validate() error {
	if l.Text == nil {
		return errors.New("'text' is missing for a link")
	}
	if l.Type == nil {
		return errors.New("'type' is missing for a link")
	}

	// if nothing is missing:
	return nil
}

func (e Experience) Validate() error {
	if e.Summarize == nil {
		return errors.New("'summarize' is missing for an experience")
	} else {
		if e.Name == nil {
			return errors.New("'name' is missing for an experience")
		}
		if e.Role == nil {
			return errors.New("'role' is missing for an experience")
		}
		if e.Start == nil {
			return errors.New("'start' is missing for an experience")
		}
		if e.End == nil {
			return errors.New("'end' is missing for an experience")
		}
		if *e.Summarize {
			if e.Description == nil {
				return errors.New("'desc' is missing for an experience")
			}
			if e.Skills == nil {
				return errors.New("'skills' is missing for an experience")
			}
		} else {
			if e.Location == nil {
				return errors.New("'location' is missing for an experience")
			}
			if e.Attributes == nil {
				return errors.New("'attributes' is missing for an experience")
			}
		}
	}

	// if nothing is missing:
	return nil
}

func (p Project) Validate() error {
	if p.Summarize == nil {
		return errors.New("'summarize' is missing for a project")
	} else {
		if p.Name == nil {
			return errors.New("'name' is missing for a project")
		}
		if p.Url == nil {
			return errors.New("'url' is missing for a project")
		}
		if *p.Summarize {
			if p.Description == nil {
				return errors.New("'desc' is missing for a project")
			}
			if p.Skills == nil {
				return errors.New("'skills' is missing for a project")
			}
		} else {
			if p.Role == nil {
				return errors.New("'role' is missing for a project")
			}
			if p.Start == nil {
				return errors.New("'start' is missing for a project")
			}
			if p.End == nil {
				return errors.New("'end' is missing for a project")
			}
			if p.Attributes == nil {
				return errors.New("'attributes' is missing for a project")
			}
		}
	}

	// if nothing is missing:
	return nil
}

func (e Education) Validate() error {
	if e.School == nil {
		return errors.New("'education.school' is missing")
	}
	if e.Location == nil {
		return errors.New("'education.location' is missing")
	}
	if e.Program == nil {
		return errors.New("'education.program' is missing")
	}
	if e.Major == nil {
		return errors.New("'education.major' is missing")
	}
	// NOTE: we don't use this value in the template
	// if e.Start == nil {
	// 	return errors.New("'education.start' is missing")
	// }
	if e.End == nil {
		return errors.New("'education.end' is missing")
	}
	if e.Courses == nil {
		return errors.New("'education.courses' is missing")
	}

	// if nothing is missing:
	return nil
}

func (s Skill) Validate() error {
	if s.Name == nil {
		return errors.New("'name' is missing for a skill")
	}
	if s.Attributes == nil {
		return errors.New("'attributes' is missing for a skill")
	}

	// if nothing is missing:
	return nil
}
