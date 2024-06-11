import unittest

from playground.Queue import myQueue


class MyTestCase(unittest.TestCase):

    def test_queue_can_add_elements(self):
        organise = myQueue()
        organise.add_to_order("Spotify")
        organise.add_to_order("instagram")
        organise.add_to_order("Twitter")

        self.assertEqual(len(organise.myQueue()),3)


if __name__ == '__main__':
    unittest.main()
