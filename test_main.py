import main
import unittest
import test_base
from io import StringIO


class MyTestCase(unittest.TestCase):

    def test_volunteer(self):
        with test_base.captured_io(StringIO('12/11\n11:00\nall of them')) as (out, err):
            main.volunteer()
        self.maxDiff = None
        output = out.getvalue().strip()
        self.assertEqual("""Here are the next 7 days for reference: 
-------------------------
thursday :     2020-12-10
-------------------------
friday   :     2020-12-11
-------------------------
saturday :     2020-12-12
-------------------------
sunday   :     2020-12-13
-------------------------
monday   :     2020-12-14
-------------------------
tuesday  :     2020-12-15
-------------------------
wednesday:     2020-12-16
-------------------------
What date would you like to volunteer? (mm/dd) 
What time would you like to volunteer? (hh:mm) 
need token.
What topics are you willing to cover: 
your booking has been added, Thank You!""", output)
