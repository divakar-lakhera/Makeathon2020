from bs4 import BeautifulSoup
import requests

class linkeinScraper():
    def __init__(self):
        self.name=""
        self.page=""
    
    def loadProfile(self, link):
        self.name=link
        raw_page = requests.get(link)
        if(raw_page.status_code != 200):
            print(f"linkediinScraper request failed : {raw_page.status_code}")
        else :
            self.html = BeautifulSoup(raw_page.content,'html-parser')
    
    def getUserName(self):
        print(self.html)
        return self.html.find("li",attrs={"class":"inline t-24 t-black t-normal break-words"}).get_text()
    
    def getUserExperiences(self):
        experiences = []
        experience = {}
        for exp in self.html.find_all('div', class_ = "pv-entity__summary-info pv-entity__summary-info--background-section"):
            experience['title'] = exp.find("h3",class_="t-16 t-black t-bold").get_text()
            
            experience['company'] = exp.find("p", class_ = "pv-entity__secondary-title t-14 t-black t-normal").get_text()
            
            experience['duration'] = exp.find("div", class_ = "display-flex").find("h4",class_ = "pv-entity__date-range t-14 t-black--light t-normal").find("span").get_text()
            
            experiences.append(experience)
        return experiences
    
    def getuserEducation(self):
        educations = []
        education = {}

        edus = self.html.find("ul",attrs={'id':'ember2674',
         'class':"pv-profile-section__section-info section-info pv-profile-section__section-info--has-no ember-view"}
         ).find_all("div", attrs={"class":"pv-profile-section__sortable-card-item pv-education-entity pv-profile-section__card-item ember-view"})
        
        for edu in edus:
            education['school_name'] = edu.find("h3",class_ = "pv-entity__school-name t-16 t-black t-bold").get_text()
            
            education['degree_name'] = edu.find("p", class_ = "pv-entity__secondary-title pv-entity_degree-name t-14 t-black t-normal"
            ).find("span", class_ = "pv-entity__comma-item").get_text()

            education['field_of_study'] = edu.find("p", class_ = "pv-entity__secondary-title pv-entity__fos t-14 t-black t-normal"
            ).find("span", class_ = "pv-entity__comma-item").get_text()
            
            dates = edu.find("p", class_ = "pv-entity__dates t-14 t-black--light t-normal").find_all("span")
            education['dates'] = f"{dates[0]} - {dates[1]}"

            educations.append(education)
        
        return educations
    
    def getUserLicenseAndCertifications(self):
        certifications = []
        certification = {}

        certificates = self.html.find("div",attrs={'id':"ember4182", 'class':"pv-profile-section-pager ember-view"}
        ).find_all("li",class_="pv-profile-section__sortable-item pv-certification-entity ember-view")

        for certificate in certificates:
            certification['course_name'] = certificate.find('h3',class_ = "t-16 t-bold").get_text()
            
            certification['company'] = certificate.find_first("p",class_ = "t-14").find("span").get_text()

            life_span = str(certificate.find("p",class_ = "t-14").get_text()) + ". " + str(certification.find("p",class_ = "t-14").find("span",class_ = "pv-entity__bullet-item-v2").get_text())
            certification['life-span'] = life_span
            certifications.append(certification)
        return certifications
    
    def getUserAccomplishments(self):
        accomplishments = []
        accomplishment = {}

        all_accomplishments = self.html.find("section",class_ = "pv-profile-section pv-accomplishments-section artdeco-container-card ember-view")

        for i in all_accomplishments:
            honors_awards = []
            awards = all_accomplishments.find("div",attrs={"id":"honors-expandable-content","class":"pv-accomplishments-block__list-container"}).find_all("li", class_ = "pv-accomplishments-block__summary-list-item")
            for award in awards:
                honors_awards.append(award.get_text())
            accomplishment['honor_awards'] = honors_awards

            courses = []
            course_list = all_accomplishments.find("div",attrs={"id":"courses-expandable-content","class":"pv-accomplishments-block__list-container"}).find_all("li",class_ = "pv-accomplishments-block__summary-list-item")
            for course in course_list:
                courses.append(course.get_text())
            accomplishment['courses'] = courses

            languages = []
            language_list = course_list = all_accomplishments.find("div",attrs={"id":"languages-expandable-content","class":"pv-accomplishments-block__list-container"}).find_all("li",class_ = "pv-accomplishments-block__summary-list-item")
            for language in language_list:
                languages.append(language.get_text())
            accomplishment['languages'] = languages

            projects = []
            project_list = course_list = all_accomplishments.find("div",attrs={"id":"projects-expandable-content","class":"pv-accomplishments-block__list-container"}).find_all("li",class_ = "pv-accomplishments-block__summary-list-item")
            for project in projects:
                projects.append(project.get_text())
            accomplishments['projects'] = projects

            test_scores = []
            test_score_list = course_list = all_accomplishments.find("div",attrs={"id":"test-scores-expandable-content","class":"pv-accomplishments-block__list-container"}).find_all("li",class_ = "pv-accomplishments-block__summary-list-item")
            for test_score in test_score_list:
                test_scores.append(test_score.get_text())
            accomplishments['test_scores'] = test_scores
        
        return accomplishments


