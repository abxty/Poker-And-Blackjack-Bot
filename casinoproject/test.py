import unittest 
from usermanagement import checklogin
from viewprofile import viewprofile
from usercreate import createuser

class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

    def test_login_success(self):
        """Test login with correct credentials returns True and success message."""
        success, message, name = checklogin("samuel", "Parad1dl3")
        self.assertTrue(success)
        self.assertEqual(message, "welcome")
        self.assertEqual(name, "samuel")
    
    def test_userdata_success(self):
        """Test whether user data can be retrieved"""
        success, credits, gameswon, gameslost = viewprofile("samuel")
        self.assertTrue(success)
        self.assertEqual(credits, 9955)
        self.assertEqual(gameswon, 0)
        self.assertEqual(gameslost, 2)

    def test_register_success(self):
        """test whether a user can register when meeting requirements"""
        success, message = createuser("sam", "Pineapple")
        self.assertTrue(success)
        self.assertEqual(message, "")



if __name__ == '__main__':
    unittest.main()

