import string
def read_file(resume_file):

    #open file
    f = open(resume_file, 'r')

    #read file to the list
    resume_list = f.readlines()
    for i in range(len(resume_list)):

        #for every line, strip for empty space
        resume_list[i] = resume_list[i].strip()
    
    #close file
    f.close()

    return resume_list

def get_name(resume_list):

    #get the name from index 0 in the resume list
    name = resume_list[0]

    #if name is empty or first character is not upper case then return invalid name
    if(len(name) == 0 or not name[0].isupper()):
        return "Invalid name"

    else:
        return name

def  get_email(resume_list):

    #for every line in resume list
    for line in resume_list:

        #find the @'s index in the line
        index = line.find('@')

        #if index is valid
        if(index != -1):
            
            #strip the line for empty space 
            email = line.strip()

            #for every character in email if character is digit then return empty string
            for char in email:
                if(char.isdigit()):
                    return ""
                
            #if email is valid then return email otherwise return empty string
            if(email[index + 1].islower() and (email.endswith(".com") or email.endswith(".edu"))):
                return email

            else:
                return ""

def get_projects(resume_list):

    #create a project list
    project_list = []

    #parse throught the resume list and find the position of project
    for idx, line in enumerate(resume_list):

        if(line[:7].lower() == 'project'):
            start_index = idx + 1
            break

    #append all the project into the project list
    while resume_list[start_index][:10] != '-' * 10:
        project_list.append(resume_list[start_index].strip())
        start_index += 1
    
    return project_list

def get_courses(resume_list): 

    ##parse throught the resume list and find the position of course
    for idx, line in enumerate(resume_list):

        if(line[:6].lower() == 'course'):
            
            #find the starting index of the first alphabetic letter 
            start_index = 7
            while(not line[start_index].isalpha()):
                start_index += 1
            
            #create a course list to put all the course inside the course list
            course_contents = line[start_index:].split(',')

            #strip all the empty space 
            for i in range(len(course_contents)):
                course_contents[i] = course_contents[i].strip()
        
            return course_contents

def get_info_html(name, email):

    #put the name into header h1
    header_name = surround_block('h1', name)

    #get the email in the paragraph
    para_email = surround_block('p', email)

    # create a whole division to include both header name and email
    info = surround_block('div', header_name + para_email)

    return info

def get_projects_html(projects):

    #put the projects into header
    header_project = surround_block('h2', 'Projects')

    #create a empty project
    para_project = ''


    for each_project in projects:

        para_project += surround_block('li', each_project)

    #put every bullet line of each project into a unordered line
    all_project = surround_block('ul',  para_project)

    #put the whole thing into div to wrap it up
    project_wrapUp = surround_block('div', header_project + all_project)

    return project_wrapUp

def get_courses_html(courses): 

    #put the course into header
    header_course = surround_block('h3', 'Courses')

    #create a span after using , to create a string from course list
    courses_detail = surround_block('span', ', '.join(courses))

    #put the whole thing into div to wrap it up
    course_wrapUp = surround_block('div', header_course + courses_detail)
    
    return course_wrapUp

def write_html(name, email, projects, courses, html_output_file):

    #open the template file 
    f = open('resume_template.html', 'r')

    #read entire file into list
    lines = f.readlines()

    #close the template file
    f.close()

    #delete the last two lines
    del lines[-1]
    del lines[-1]

    #append the header div
    lines.append('<div id="page-wrap">')

    #get the first part of html and append to lines
    into_html = get_info_html(name, email)
    lines.append(into_html)

    #get the project part of html and append to lines
    projects_html = get_projects_html(projects)
    lines.append(projects_html)

    #get the course part of html and append to lines
    courses_html = get_courses_html(courses)
    lines.append(courses_html)

    #append the closing div
    lines.append('</div>')

    #append the closing body
    lines.append('</body>')

    #append the closing html
    lines.append('</html>')

    #open output file to write resume
    fout = open(html_output_file, 'w')

    #write all the lines into the output file
    fout.writelines(lines)

    #close output file
    fout.close()

def surround_block(tag, text):
    """
    Surrounds the given text with the given html tag and returns the string.
    """
    
    #create surround block passing tag and text
    return '<{}>{}</{}>'.format(tag, text, tag)

def create_email_link(email_address):
    """
    Creates an email link with the given email_address.
    To cut down on spammers harvesting the email address from the webpage,
    displays the email address with [aT] instead of @.

    Example: Given the email address: lbrandon@wharton.upenn.edu
    Generates the email link: <a href="mailto:lbrandon@wharton.upenn.edu">lbrandon[aT]wharton.upenn.edu</a>

    Note: If, for some reason the email address does not contain @,
    use the email address as is and don't replace anything.
    """
    
    #create the final email link
    email = 'Email: <a href="mailto:' + email_address + '">' + email_address.replace('@', '[aT]') + '</a>'

    return email   

def generate_html(txt_input_file, html_output_file):
    """
    Loads given txt_input_file,
    gets the name, email address, list of projects, and list of courses,
    then writes the info to the given html_output_file. """

    # call function(s) to load given txt_input_file
    resume_list = read_file(txt_input_file)

    # call function(s) to get name
    name = get_name(resume_list)

    # call function(s) to get email address
    email = get_email(resume_list)

    # call function(s) to get list of projects
    projects = get_projects(resume_list)

    # call function(s) to get list of courses
    courses = get_courses(resume_list)

    # call function(s) to write the name, email address, list of projects, and list of courses to the given html_output_file
    write_html(name, email, projects, courses, html_output_file)
    
def main():

    # DO NOT REMOVE OR UPDATE THIS CODE
    # generate resume.html file from provided sample resume.txt

    # generate_html(r'C:\Users\Owner\Downloads\6pZfi4DnSLWWX4uA5_i1tQ_a16f950702d94d85a1dd4230834d8010_HW4_Make-a-Website\HW4_Make a Website\resume.txt',
    # r'C:\Users\Owner\Downloads\6pZfi4DnSLWWX4uA5_i1tQ_a16f950702d94d85a1dd4230834d8010_HW4_Make-a-Website\HW4_Make a Website\resume.html')
    
    generate_html('resume.txt', 'resume.html')

    # DO NOT REMOVE OR UPDATE THIS CODE.
    # Uncomment each call to the generate_html function when you’re ready
    # to test how your program handles each additional test resume.txt file

    generate_html('TestResumes/resume_bad_name_lowercase/resume.txt', 'TestResumes/resume_bad_name_lowercase/resume.html')
    generate_html('TestResumes/resume_courses_w_whitespace/resume.txt', 'TestResumes/resume_courses_w_whitespace/resume.html')
    generate_html('TestResumes/resume_courses_weird_punc/resume.txt', 'TestResumes/resume_courses_weird_punc/resume.html')
    generate_html('TestResumes/resume_projects_w_whitespace/resume.txt', 'TestResumes/resume_projects_w_whitespace/resume.html')
    generate_html('TestResumes/resume_projects_with_blanks/resume.txt', 'TestResumes/resume_projects_with_blanks/resume.html')
    generate_html('TestResumes/resume_template_email_w_whitespace/resume.txt', 'TestResumes/resume_template_email_w_whitespace/resume.html')
    generate_html('TestResumes/resume_wrong_email/resume.txt', 'TestResumes/resume_wrong_email/resume.html')

    # If you want to test additional resume files, call the generate_html function with the given .txt file
    # and desired name of output .html file

if __name__ == '__main__':
    main()
