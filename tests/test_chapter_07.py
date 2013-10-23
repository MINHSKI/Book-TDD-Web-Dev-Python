#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import unittest

from book_parser import Command, Output
from book_tester import ChapterTest

class Chapter7Test(ChapterTest):
    chapter_no = 7

    def test_listings_and_commands_and_output(self):
        self.parse_listings()

        # sanity checks
        self.assertEqual(self.listings[0].type, 'code listing with git ref')
        self.assertEqual(type(self.listings[1]), Command)
        self.assertEqual(type(self.listings[2]), Output)

        self.sourcetree.start_with_checkout(self.chapter_no)
        # other prep
        self.sourcetree.run_command('python3 manage.py syncdb --noinput')

        # skips
        self.skip_with_check(24, 'the -b means ignore whitespace')
        self.skip_with_check(27, 'leave static, for now')
        self.skip_with_check(46, 'will now show all the bootstrap')
        self.skip_with_check(49, 'projects') # tree showing where static goes

        while self.pos < 32:
            print(self.pos)
            self.recognise_listing_and_process_it()

        settings = self.sourcetree.get_contents('superlists/settings.py')
        assert self.listings[32].filename == 'superlists/settings.py'
        for line in self.listings[32].contents.split('\n'):
            assert line in settings
        self.listings[32].skip = True

        while self.pos < 48:
            print(self.pos)
            self.recognise_listing_and_process_it()

        settings = self.sourcetree.get_contents('superlists/settings.py')
        assert self.listings[48].filename == 'superlists/settings.py'
        for line in self.listings[48].contents.split('\n'):
            assert line in settings
        self.listings[48].skip = True

        #import time
        #print(self.tempdir)
        #time.sleep(200)
        while self.pos < len(self.listings):
            print(self.pos)
            self.recognise_listing_and_process_it()


        self.assert_all_listings_checked(self.listings)
        self.check_final_diff(self.chapter_no)


if __name__ == '__main__':
    unittest.main()
