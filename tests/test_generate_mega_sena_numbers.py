import unittest
from generate_mega_sena_numbers import generate_mega_sena


class TestGenerateMegaSenaNumbers(unittest.TestCase):
    def test_generate_mega_sena_numbers_default(self):
        result = generate_mega_sena()
        self.assertEqual(len(result), 6)
        self.assertTrue(all(1 <= num <= 60 for num in result))
        self.assertEqual(len(result), len(set(result)))

    def test_generate_mega_sena_numbers_custom(self):
        result = generate_mega_sena(10)
        self.assertEqual(len(result), 10)
        self.assertTrue(all(1 <= num <= 60 for num in result))
        self.assertEqual(len(result), len(set(result)))

    def test_generate_mega_sena_numbers_with_existing_list(self):
        existing_numbers = [1, 2, 3]
        result = generate_mega_sena(6, existing_numbers)
        self.assertEqual(len(result), 6)
        self.assertTrue(all(1 <= num <= 60 for num in result))
        self.assertEqual(len(result), len(set(result)))


if __name__ == "__main__":
    unittest.main()
