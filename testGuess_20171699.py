import unittest

from guess import Guess

class TestGuess(unittest.TestCase):

    def setUp(self):
        self.g1 = Guess('default')

    def tearDown(self):
        pass

    def testDisplayCurrent(self):
        self.assertEqual(self.g1.displayCurrent(), '_ e _ _ _ _ _ ')
        self.g1.guess('a')
        self.assertEqual(self.g1.displayCurrent(), '_ e _ a _ _ _ ')
        self.g1.guess('t')
        self.assertEqual(self.g1.displayCurrent(), '_ e _ a _ _ t ')
        self.g1.guess('u')
        self.assertEqual(self.g1.displayCurrent(), '_ e _ a u _ t ')

    def testDisplayGuessed(self):
        self.assertEqual(self.g1.displayGuessed(), ' e n ')
        self.g1.guess('a')
        self.assertEqual(self.g1.displayGuessed(), ' a e n ')
        self.g1.guess('t')
        self.assertEqual(self.g1.displayGuessed(), ' a e n t ')
        self.g1.guess('u')
        self.assertEqual(self.g1.displayGuessed(), ' a e n t u ')

    def testguess(self):
        #리턴 값이 올바른가
        self.assertTrue(self.g1.guess('d'))
        self.assertFalse(self.g1.guess('r'))
        #부분적으로 맞추어진 단어의 상태가 올바르게 유지되는가
        #이용된 글자들의 집합을 나타내는 데이터는 올바르게 유지되는가
        self.assertEqual(self.g1.currentStatus, 'de_____')
        self.g1.guess('a')
        self.assertEqual(self.g1.currentStatus, 'de_a___')
        self.g1.guess('t')
        self.assertEqual(self.g1.currentStatus, 'de_a__t')
        self.g1.guess('u')
        self.assertEqual(self.g1.currentStatus, 'de_au_t')
        #단어 전체를 다 맞춘 경우에 대한 처리가 올바른가?
        self.g1.guess('f')
        self.g1.guess('l')



if __name__ == '__main__':
    unittest.main()
