import softest

class TestDemo(softest.TestCase):

    def test_sample(self):
        self.soft_assert(self.assertEqual, 10, 20)
        self.soft_assert(self.assertTrue, False)
        self.assert_all()