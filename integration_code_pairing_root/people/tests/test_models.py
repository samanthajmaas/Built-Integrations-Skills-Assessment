from django.test import TestCase
from people.models import People


class PeopleTestCase(TestCase):
    def setUp(self):
        super().setUp()

    def test_person_to_dict_no_id(self):
        p = People(
            id=1,
            person_id=2,
            name='Test Person',
            height=5,
            mass=50,
            hair_color='brown',
            eye_color='brown',
            birth_year='1000',
            gender='female',
        )
        p_dict = p.to_dict()
        self.assertEqual(p.id, 1)
        self.assertNotIn('id', p_dict)
    
    def test_person_to_dict(self):
        expected_dict = {
            'person_id': 2,
            'name': 'Test Person',
            'height': 5,
            'mass': 50,
            'hair_color': 'brown',
            'eye_color': 'brown',
            'birth_year': '1000',
            'gender': 'female'
        }

        p = People(id=1, **expected_dict)
        p_dict = p.to_dict()
        self.assertEqual(p.id, 1)
        self.assertEqual(p_dict, expected_dict)