import unittest

from make_website import *

class MakeWebsite_Test(unittest.TestCase):

    def setUp(self):

        self.resume_list = read_file('resume.txt')

    def test_surround_block(self):

        # test surrounding html
        self.assertEqual(surround_block('h1', 'Yiting Guevara'), "<h1>Yiting Guevara</h1>")

        # test surrounding html
        self.assertEqual(surround_block('h1', 'Eagles'), "<h1>Eagles</h1>")

        # test surrounding html
        self.assertEqual(surround_block('p', 'Lorem ipsum dolor sit amet, consectetur ' +
                                        'adipiscing elit. Sed ac felis sit amet ante porta ' +
                                        'hendrerit at at urna. Donec in vehicula ex. Aenean ' +
                                        'scelerisque accumsan augue, vitae cursus sapien venenatis ' +
                                        'ac. Quisque dui tellus, rutrum hendrerit nisl vitae, ' +
                                        'pretium mollis lorem. Pellentesque eget quam a justo ' +
                                        'egestas vehicula in eu justo. Nulla cursus, metus vitae ' +
                                        'tincidunt luctus, turpis lectus bibendum purus, eget ' +
                                        'consequat est lacus ac nibh. In interdum metus vel est ' +
                                        'posuere aliquet. Maecenas et euismod arcu, eu auctor ' +
                                        'libero. Phasellus lectus magna, auctor ac auctor in, ' +
                                        'suscipit id turpis. Maecenas dignissim enim ac justo ' +
                                        'tincidunt viverra. Sed interdum molestie tincidunt. Etiam ' +
                                        'vitae justo tincidunt, blandit augue id, volutpat ligula. ' +
                                        'Aenean ut aliquet mi. Suspendisse consequat blandit posuere.'),
                                        '<p>Lorem ipsum dolor sit amet, consectetur ' +
                                        'adipiscing elit. Sed ac felis sit amet ante porta ' +
                                        'hendrerit at at urna. Donec in vehicula ex. Aenean ' +
                                        'scelerisque accumsan augue, vitae cursus sapien venenatis ' +
                                        'ac. Quisque dui tellus, rutrum hendrerit nisl vitae, ' +
                                        'pretium mollis lorem. Pellentesque eget quam a justo ' +
                                        'egestas vehicula in eu justo. Nulla cursus, metus vitae ' +
                                        'tincidunt luctus, turpis lectus bibendum purus, eget ' +
                                        'consequat est lacus ac nibh. In interdum metus vel est ' +
                                        'posuere aliquet. Maecenas et euismod arcu, eu auctor ' +
                                        'libero. Phasellus lectus magna, auctor ac auctor in, ' +
                                        'suscipit id turpis. Maecenas dignissim enim ac justo ' +
                                        'tincidunt viverra. Sed interdum molestie tincidunt. Etiam ' +
                                        'vitae justo tincidunt, blandit augue id, volutpat ligula. ' +
                                        'Aenean ut aliquet mi. Suspendisse consequat blandit posuere.</p>')

    def test_create_email_link(self):

        # test created email
        self.assertEqual(
            create_email_link('yiting@gmail.com'),
            'Email: <a href="mailto:yiting@gmail.com">yiting[aT]gmail.com</a>')

        # test created email
        self.assertEqual(
            create_email_link('lbrandon@wharton.upenn.edu'),
            'Email: <a href="mailto:lbrandon@wharton.upenn.edu">lbrandon[aT]wharton.upenn.edu</a>')

        # test created email
        self.assertEqual(
            create_email_link('lbrandon.at.wharton.upenn.edu'),
            'Email: <a href="mailto:lbrandon.at.wharton.upenn.edu">lbrandon.at.wharton.upenn.edu</a>')

    def test_get_name(self):

        #test for invalid name because of number
        self.assertEqual(get_name(['  25Lucy', 'Courses :- Math, English, History', 'Projects', 'Java Spring', 'Spring MVC',
        'Designed a complete website using React', '------------------------------', 'yiting@seas.upenn.edu']), 'Invalid name')

        #test for invalid name because of lowercase letter
        self.assertEqual(get_name(['lucy', 'Courses :- Math, English, History', 'Projects', 'Java Spring', 'Spring MVC',
        'Designed a complete website using React', '------------------------------', 'yiting@seas.upenn.edu']), 'Invalid name')

        ##test for the correct name
        self.assertEqual(get_name(['Lucy', 'Courses :- Math, English, History', 'Projects', 'Java Spring', 'Spring MVC',
        'Designed a complete website using React', '------------------------------', 'yiting@seas.upenn.edu']), 'Lucy')


    def test_get_email(self):
        
        #test for invalid email
        self.assertEqual(get_email(['Yiting', 'Courses :- Math, English, History', 'Projects', 'Java Spring', 'Spring MVC',
        'Designed a complete website using React', '------------------------------', 'yiting@seas.upenn.org']), '')

        #test for invalid email
        self.assertEqual(get_email(['Yiting', 'Courses :- Math, English, History', 'Projects', 'Java Spring', 'Spring MVC',
        'Designed a complete website using React', '------------------------------', 'yiting@25seas.upenn.org']), '')

        #test for invalid email
        self.assertEqual(get_email(['Lucy (name lowercase)', 'Courses :- Math, English, History', 'Projects', 'Java Spring', 'Spring MVC',
        'Designed a complete website using React', '------------------------------', 'yiting@seas.upenn.edu']), 'yiting@seas.upenn.edu')

    def test_get_projects(self):

        #test for get projects
        self.assertListEqual(get_projects(['Lucy', 'Courses :- Math, English, History', 'Projects', 'Java Spring', 'Spring MVC',
        'Designed a complete website using React', '------------------------------', 'yiting@seas.upenn.edu']), ['Java Spring', 'Spring MVC', 'Designed a complete website using React'])
        
        #test for get projects for leading or trailing whitespace
        self.assertListEqual(get_projects(['Yiting', 'Courses :- Math, English, History', 'Projects    ', '   Java Spring   ', '   Spring MVC   ',
        'Designed a complete website using React', '------------------------------', 'yiting@seas.upenn.edu']), ['Java Spring', 'Spring MVC', 'Designed a complete website using React'])
        
        #test for get projects
        self.assertListEqual(get_projects(self.resume_list), ['CancerDetector.com, New Jersey, USA - Project manager, codified the assessment and mapped it to the CancerDetector ontology. Member of the UI design team, designed the portfolio builder UI and category search pages UI. Reviewed existing rank order and developed new search rank order approach.', 'Biomedical Imaging - Developed a semi-automatic image mosaic program based on SIFT algorithm (using Matlab)'])

    def test_get_courses(self):
        
        #test for get courses for any random punctuation
        self.assertListEqual(get_courses(['Lucy', 'Courses++++++++ :- Math, English, History', 'Projects', 'Java Spring', 'Spring MVC',
        'Designed a complete website using React', '------------------------------', 'yiting@seas.upenn.edu']), ['Math', 'English', 'History'])

        #test for get courses for leading or trailing whitespace
        self.assertListEqual(get_courses(['Lucy', 'Courses :-   Math  ,    English   ,    History  ', 'Projects', 'Java Spring', 'Spring MVC',
        'Designed a complete website using React', '------------------------------', 'yiting@seas.upenn.edu']), ['Math', 'English', 'History'])

        #test for get courses 
        self.assertListEqual(get_courses(self.resume_list),['Programming Languages and Techniques', 'Biomedical image analysis', 'Software Engineering'])

    def test_get_info_html(self):

        #test for get info html
        self.assertEqual(get_info_html('Yiting', 'yitingchen@gmail.com'), '<div><h1>Yiting</h1><p>yitingchen@gmail.com</p></div>')

        #test for get info html
        self.assertEqual(get_info_html('David', 'davidgch@gmail.com'), '<div><h1>David</h1><p>davidgch@gmail.com</p></div>')

        #test for get info html
        self.assertEqual(get_info_html('Lucy', 'lucyCat@gmail.com'), '<div><h1>Lucy</h1><p>lucyCat@gmail.com</p></div>')

    def test_get_projects_html(self):

        
        projects = get_projects(self.resume_list)
        #test for get project html
        self.assertEqual(get_projects_html(projects), '<div><h2>Projects</h2><ul><li>CancerDetector.com, New Jersey, USA - Project manager, codified the assessment and mapped it to the CancerDetector ontology. Member of the UI design team, designed the portfolio builder UI and category search pages UI. Reviewed existing rank order and developed new search rank order approach.</li><li>Biomedical Imaging - Developed a semi-automatic image mosaic program based on SIFT algorithm (using Matlab)</li></ul></div>')

        projectOne = ['Java Spring', 'Spring MVC', 'Designed a complete website using React']
        #test for get projectOne html
        self.assertEqual(get_projects_html(projectOne), '<div><h2>Projects</h2><ul><li>Java Spring</li><li>Spring MVC</li><li>Designed a complete website using React</li></ul></div>')
  
        projectTwo = ['Create Rocket', 'Create aircraft', 'Designed computer']
        #test for get projectTwo html
        self.assertEqual(get_projects_html(projectTwo), '<div><h2>Projects</h2><ul><li>Create Rocket</li><li>Create aircraft</li><li>Designed computer</li></ul></div>')

    def test_get_courses_html(self):

        courseOne = ['Math', 'English', 'History']
        #test for get course html
        self.assertEqual(get_courses_html(courseOne), '<div><h3>Courses</h3><span>Math, English, History</span></div>')

        courseTwo = ['Basketball', 'Soccer', 'Skydive']
        #test for get course html
        self.assertEqual(get_courses_html(courseTwo), '<div><h3>Courses</h3><span>Basketball, Soccer, Skydive</span></div>')


        courseThree = ['Programming Languages and Techniques', 'Biomedical image analysis', 'Software Engineering']
        #test for get course html
        self.assertEqual(get_courses_html(courseThree), '<div><h3>Courses</h3><span>Programming Languages and Techniques, Biomedical image analysis, Software Engineering</span></div>')


if __name__ == '__main__':
    unittest.main()
