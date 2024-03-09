#!/usr/bin/env python3

import unittest

from ...src.resumake.utils import xp_fmt, md_to_pdf, pdf_to_png, generate_resume


class TestUtils(unittest.TestCase):
    def test_xp_fmt(self):
        name = "Company"
        address = "Address"
        spec = "Role"
        date = "Aug 1984"
        test_case = (
            "<div class='xp-h'>"
            + f"<span>{name}</span>"
            + f"<span>{address}</span>"
            + "</div>\n"
            + "<div class='xp-s'>"
            + f"<span>{spec}</span>"
            + f"<span>{date}</span>"
            + "</div>"
        )
        self.assertEqual(xp_fmt(name, address, spec, date), test_case)

    def test_md_to_pdf(self):
        pass

    def test_pdf_to_png(self):
        pass

    def test_generate_resume(self):
        pass


if __name__ == "__main__":
    unittest.main()
