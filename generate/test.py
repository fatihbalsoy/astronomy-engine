#!/usr/bin/env python3
import sys
sys.path.append('../source/python')
import astronomy


def Test_AstroTime():
    expected_ut = 6910.270978506945
    expected_tt = 6910.271779431480
    time = astronomy.Time.Make(2018, 12, 2, 18, 30, 12.543)
    diff = time.ut - expected_ut
    if abs(diff) > 1.0e-12:
        print('Test_AstroTime: excessive UT error {}'.format(diff))
        sys.exit(1)
    diff = time.tt - expected_tt
    if abs(diff) > 1.0e-12:
        print('Test_AstroTime: excessive TT error {}'.format(diff))
        sys.exit(1)
    s = str(time.Utc())
    if s != '2018-12-02 18:30:12.543000':
        print('Test_AstroTime: Utc() returned incorrect string "{}"'.format(s))
        sys.exit(1)
    time = astronomy.Time.Make(2018, 12, 31, 23, 59, 59.9994)
    s = str(time)
    if s != '2018-12-31T23:59:59.999Z':
        print('Test_AstroTime: expected 2018-12-31T23:59:59.999Z but found {}'.format(s))
        sys.exit(1)
    time = astronomy.Time.Make(2018, 12, 31, 23, 59, 59.9995)
    s = str(time)
    if s != '2019-01-01T00:00:00.000Z':
        print('Test_AstroTime: expected 2019-01-01T00:00:00.000Z but found {}'.format(s))
        sys.exit(1)
    print('Current time =', astronomy.Time.Now())


def Test_GeoMoon():
    time = astronomy.Time.Make(2019, 6, 24, 15, 45, 37)
    vec = astronomy.GeoMoon(time)
    print('Test_GeoMoon: vec = {:0.10f}, {:0.10f}, {:0.10f}'.format(vec.x, vec.y, vec.z))


if len(sys.argv) == 2:
    if sys.argv[1] == 'time':
        Test_AstroTime()
        sys.exit(0)

    if sys.argv[1] == 'moon':
        Test_GeoMoon()
        sys.exit(0)

print('test.py: Invalid command line arguments.')
sys.exit(1)
