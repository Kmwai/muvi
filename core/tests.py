from django.test import TestCase
from django.core.paginator import Paginator, InvalidPage
from .models import Movie


class MoviePaginationTestCase(TestCase):
    """
    test pagination w/ model instances
    """
    @classmethod
    def setUpTestData(cls):
        for n in range(1, 10):
            a = Movie(title='Movie %s' % n, slug='title'.format(n), year=1990, runtime=100)
            a.save()

    def test_first_page(self):
        paginator = Paginator(Movie.objects.order_by('id'), 5)
        p = paginator.page(1)
        self.assertEqual("<Page 1 of 2>", str(p))
        self.assertQuerysetEqual(p.object_list, [
            "<Movie: Movie 1 (1990)>",
            "<Movie: Movie 2 (1990)>",
            "<Movie: Movie 3 (1990)>",
            "<Movie: Movie 4 (1990)>",
            "<Movie: Movie 5 (1990)>"
        ])

        self.assertTrue(p.has_next())
        self.assertFalse(p.has_previous())
        self.assertTrue(p.has_other_pages())
        self.assertEqual(2, p.next_page_number())
        with self.assertRaises(InvalidPage):
            p.previous_page_number()
        self.assertEqual(1, p.start_index())
        self.assertEqual(5, p.end_index())

    def test_last_page(self):
        paginator = Paginator(Movie.objects.order_by('id'), 5)
        p = paginator.page(2)
        self.assertEqual("<Page 2 of 2>", str(p))
        self.assertQuerysetEqual(p.object_list, [
            "<Movie: Movie 6 (1990)>",
            "<Movie: Movie 7 (1990)>",
            "<Movie: Movie 8 (1990)>",
            "<Movie: Movie 9 (1990)>"
        ])

        self.assertTrue(p.has_previous())
        self.assertFalse(p.has_next())
        self.assertTrue(p.has_other_pages())
        with self.assertRaises(InvalidPage):
            p.next_page_number()
        self.assertEqual(1, p.previous_page_number())
        self.assertEqual(6, p.start_index())
        self.assertEqual(9, p.end_index())




