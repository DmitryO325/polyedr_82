import unittest
from unittest.mock import patch, mock_open

from preoptimize.polyedr import Polyedr


class TestPolyedr1(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        fake_file_content = """200.0	45.0	45.0	30.0
8	4	16
-0.5	-0.5	0.5
-0.5	0.5	0.5
0.5	0.5	0.5
0.5	-0.5	0.5
-0.5	-0.5	-0.5
-0.5	0.5	-0.5
0.5	0.5	-0.5
0.5	-0.5	-0.5
4	5    6    2    1
4	3    2    6    7
4	3    7    8    4
4	1    4    8    5"""
        fake_file_path = 'data/holey_box.geom'
        with patch('preoptimize.polyedr.open'.format(__name__),
                   new=mock_open(read_data=fake_file_content)) as _file:
            cls.polyedr = Polyedr(fake_file_path)
            _file.assert_called_once_with(fake_file_path)

    def test_num_vertexes(self):
        self.assertEqual(len(self.polyedr.vertexes), 8)

    def test_num_facets(self):
        self.assertEqual(len(self.polyedr.facets), 4)

    def test_num_edges(self):
        self.assertEqual(len(self.polyedr.edges), 16)

    def test_area(self):
        self.polyedr.count_area()
        self.assertAlmostEqual(self.polyedr.area, 0.0)


class TestPolyedr2(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        fake_file_content = """1.0    0.0 0.0 0.0
8	2	8
0.3 0.3 0.5
1.0 0.0 0.7
3.0 5.0 2.0
0.0 0.0 0.0
1.0 1.0 3.0
6.0 1.0 3.0
6.0 6.0 3.0
1.0 6.0 3.0
4	1    2    3    4
4	5    6    7    8"""
        fake_file_path = 'data/holey_box.geom'
        with patch('preoptimize.polyedr.open'.format(__name__),
                   new=mock_open(read_data=fake_file_content)) as _file:
            cls.polyedr = Polyedr(fake_file_path)
            _file.assert_called_once_with(fake_file_path)

    def test_num_vertexes(self):
        self.assertEqual(len(self.polyedr.vertexes), 8)

    def test_num_facets(self):
        self.assertEqual(len(self.polyedr.facets), 2)

    def test_num_edges(self):
        self.assertEqual(len(self.polyedr.edges), 8)

    def test_area(self):
        self.polyedr.count_area()
        self.assertAlmostEqual(self.polyedr.area, 2.5)


class TestPolyedr3(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        fake_file_content = """1.5 10.0    10.0    10.0
9   3   9
-0.5    0.0    1.0
1.0 1.0 0.3
5.6 6.4 0.1
0.0 0.2 0.7
4.5 8.4 7.8
-3.4    4.5 5.7
-0.3    0.0 3.4
4.5 -5.6    2.4
7.4 4.5 -6.2
3   1   2   3
3   4   5   6
3   7   8   9"""
        fake_file_path = 'data/holey_box.geom'
        with patch('preoptimize.polyedr.open'.format(__name__),
                   new=mock_open(read_data=fake_file_content)) as _file:
            cls.polyedr = Polyedr(fake_file_path)
            _file.assert_called_once_with(fake_file_path)

    def test_num_vertexes(self):
        self.assertEqual(len(self.polyedr.vertexes), 9)

    def test_num_facets(self):
        self.assertEqual(len(self.polyedr.facets), 3)

    def test_num_edges(self):
        self.assertEqual(len(self.polyedr.edges), 9)

    def test_area(self):
        self.polyedr.count_area()
        self.assertAlmostEqual(self.polyedr.area, 57.725)


class TestPolyedr4(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        fake_file_content = """40.0	45.0	-30.0	-60.0
8	2	8
0.0 0.0 0.0
5.0 0.0 0.0
5.0 5.0 0.0
0.0 5.0 0.0
1.0 1.0 3.0
6.0 1.0 3.0
6.0 6.0 3.0
1.0 6.0 3.0
4	1    2    3    4    
4	5    6    7    8"""
        fake_file_path = 'data/holey_box.geom'
        with patch('preoptimize.polyedr.open'.format(__name__),
                   new=mock_open(read_data=fake_file_content)) as _file:
            cls.polyedr = Polyedr(fake_file_path)
            _file.assert_called_once_with(fake_file_path)

    def test_num_vertexes(self):
        self.assertEqual(len(self.polyedr.vertexes), 8)

    def test_num_facets(self):
        self.assertEqual(len(self.polyedr.facets), 2)

    def test_num_edges(self):
        self.assertEqual(len(self.polyedr.edges), 8)

    def test_area(self):
        self.polyedr.count_area()
        self.assertAlmostEqual(self.polyedr.area, 25.0)


class TestPolyedr5(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        fake_file_content = """200.0	45.0	45.0	30.0
8	6	24
-0.5	-0.5	0.5	
-0.5	0.5	0.5	
0.5	0.5	0.5	
0.5	-0.5	0.5	
-0.5	-0.5	-0.5	
-0.5	0.5	-0.5	
0.5	0.5	-0.5	
0.5	-0.5	-0.5	
4	1    2    3    4    
4	5    6    2    1    
4	3    2    6    7    
4	3    7    8    4    
4	1    4    8    5    
4	8    7    6    5"""
        fake_file_path = 'data/holey_box.geom'
        with patch('preoptimize.polyedr.open'.format(__name__),
                   new=mock_open(read_data=fake_file_content)) as _file:
            cls.polyedr = Polyedr(fake_file_path)
            _file.assert_called_once_with(fake_file_path)

    def test_num_vertexes(self):
        self.assertEqual(len(self.polyedr.vertexes), 8)

    def test_num_facets(self):
        self.assertEqual(len(self.polyedr.facets), 6)

    def test_num_edges(self):
        self.assertEqual(len(self.polyedr.edges), 24)

    def test_area(self):
        self.polyedr.count_area()
        self.assertAlmostEqual(self.polyedr.area, 2.0)


class TestPolyedr6(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        fake_file_content = """200.0	60.0	-140.0	60.0
8	5	20
-0.5	-0.5	0.5	
-0.5	0.5	0.5	
0.5	0.5	0.5	
0.5	-0.5	0.5	
-0.5	-0.5	-0.5	
-0.5	0.5	-0.5	
0.5	0.5	-0.5	
0.5	-0.5	-0.5	
4	1    2    3    4    
4	5    6    2    1    
4	3    2    6    7    
4	3    7    8    4    
4	1    4    8    5"""
        fake_file_path = 'data/holey_box.geom'
        with patch('preoptimize.polyedr.open'.format(__name__),
                   new=mock_open(read_data=fake_file_content)) as _file:
            cls.polyedr = Polyedr(fake_file_path)
            _file.assert_called_once_with(fake_file_path)

    def test_num_vertexes(self):
        self.assertEqual(len(self.polyedr.vertexes), 8)

    def test_num_facets(self):
        self.assertEqual(len(self.polyedr.facets), 5)

    def test_num_edges(self):
        self.assertEqual(len(self.polyedr.edges), 20)

    def test_area(self):
        self.polyedr.count_area()
        self.assertAlmostEqual(self.polyedr.area, 1.0)
