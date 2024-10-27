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

// ----- VALIDATION METHODS ----- //

func (r *Resume) Validate() (bool, string) {
	if r.Author == nil {
		return false, "'author' is missing"
	}
	if r.Location == nil {
		return false, "'location' is missing"
	}
	if r.Phone == nil {
		return false, "'phone' is missing"
	}
	if r.Email == nil {
		return false, "'email' is missing"
	}
	if r.Website == nil {
		return false, "'website' is missing"
	}
	if r.Socials == nil {
		return false, "'socials' is missing"
	} else {
		isValid, msg := r.Socials.Validate()
		if !isValid {
			return false, msg
		}
	}
	if r.Profile == nil {
		return false, "'profile' is missing"
	}
	if r.Experiences == nil {
		return false, "'experiences' is missing"
	} else {
		for _, e := range r.Experiences {
			isValid, msg := e.Validate()
			if !isValid {
				return false, msg
			}
		}
	}
	if r.Projects == nil {
		return false, "'projects' is missing"
	} else {
		for _, p := range r.Projects {
			isValid, msg := p.Validate()
			if !isValid {
				return false, msg
			}
		}
	}
	if r.Education == nil {
		return false, "'education' is missing"
	} else {
		isValid, msg := r.Education.Validate()
		if !isValid {
			return false, msg
		}
	}
	if r.Skills == nil {
		return false, "'skills' is missing"
	} else {
		for _, s := range r.Skills {
			isValid, msg := s.Validate()
			if !isValid {
				return false, msg
			}
		}
	}

	// if nothing is missing:
	return true, ""
}

func (s *Socials) Validate() (bool, string) {
	if s.Github == nil {
		return false, "'socials.github' is missing"
	}
	if s.Linkedin == nil {
		return false, "'socials.linkedin' is missing"
	}

	// if nothing is missing:
	return true, ""
}

func (e *Experience) Validate() (bool, string) {
	if e.Summarize == nil {
		return false, "'summarize' is missing for an experience"
	} else {
		if e.Name == nil {
			return false, "'name' is missing for an experience"
		}
		if e.Role == nil {
			return false, "'role' is missing for an experience"
		}
		if e.Start == nil {
			return false, "'start' is missing for an experience"
		}
		if e.End == nil {
			return false, "'end' is missing for an experience"
		}
		if *e.Summarize {
			if e.Description == nil {
				return false, "'desc' is missing for an experience"
			}
			if e.Skills == nil {
				return false, "'skills' is missing for an experience"
			}
		} else {
			if e.Location == nil {
				return false, "'location' is missing for an experience"
			}
			if e.Attributes == nil {
				return false, "'attributes' is missing for an experience"
			}
		}
	}

	// if nothing is missing:
	return true, ""
}

func (p *Project) Validate() (bool, string) {
	if p.Summarize == nil {
		return false, "'summarize' is missing for a project"
	} else {
		if p.Name == nil {
			return false, "'name' is missing for a project"
		}
		if p.Url == nil {
			return false, "'url' is missing for a project"
		}
		if *p.Summarize {
			if p.Description == nil {
				return false, "'desc' is missing for a project"
			}
			if p.Skills == nil {
				return false, "'skills' is missing for a project"
			}
		} else {
			if p.Role == nil {
				return false, "'role' is missing for a project"
			}
			if p.Start == nil {
				return false, "'start' is missing for a project"
			}
			if p.End == nil {
				return false, "'end' is missing for a project"
			}
			if p.Attributes == nil {
				return false, "'attributes' is missing for a project"
			}
		}
	}

	// if nothing is missing:
	return true, ""
}

func (e *Education) Validate() (bool, string) {
	if e.School == nil {
		return false, "'education.school' is missing"
	}
	if e.Location == nil {
		return false, "'education.location' is missing"
	}
	if e.Program == nil {
		return false, "'education.program' is missing"
	}
	if e.Major == nil {
		return false, "'education.major' is missing"
	}
	// NOTE: we don't use this value in the template
	// if e.Start == nil {
	// 	return false, "'education.start' is missing"
	// }
	if e.End == nil {
		return false, "'education.end' is missing"
	}
	if e.Courses == nil {
		return false, "'education.courses' is missing"
	}

	// if nothing is missing:
	return true, ""
}

func (s *Skill) Validate() (bool, string) {
	if s.Name == nil {
		return false, "'name' is missing for a skill"
	}
	if s.Attributes == nil {
		return false, "'attributes' is missing for a skill"
	}

	// if nothing is missing:
	return true, ""
}
