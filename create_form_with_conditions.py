import os, json
from dotenv import load_dotenv
import requests
from random import randint

load_dotenv()
api_key = os.environ.get("JOTFORM_API_KEY")
if not api_key:
    print("No API Key set in .env, quitting")
    quit()

quesitons = [
    "Adapting - Changing, adjusting, and conforming to conditions, environment, or people.",
    "Adventuring - Risking, periling, or hazarding safety and comfort to participate in an activity or venture.",
    "Analyzing - Examining, evaluating, and judge data, people, and situations.",
    "Appraising – Assessing, evaluating, estimating the worth of an object or idea.",
    "Bargaining – Negotiating, mediating, or arbitrating with others of differing opinions in order to reach an agreeable solution.",
    "Calculating - Computing, tallying, and reckoning using mathematics.",
    "Coaching – training, developing, and guiding individuals and teams in a common effort.",
    "Competing – Striving, contending, or rivaling to gain a goal, victory, or advantage.",
    "Constructing – Building, making, and erecting mechanical and structural objects.",
    "Consulting – Advising, counseling, and instructing individuals or groups to assist in decision-making.",
    "Cooking/baking – Planning, preparing, or serving food.",
    "Coordinating – Organizing, directing, and synchronizing people and resources for a common purpose.",
    "Counseling - Advising, guiding, or recommending a course of action to an individual or group for their well-being.",
    "Creating – Inventing, originating, or composing a unique creation which would not otherwise exist.",
    "Decorating – Beautifying, enhancing, or adorning an item, increasing its worth.",
    "Designing – Fashioning, conceiving, or drawing an object or artistic work to be created.",
    "Developing - Expanding, extending, or improving the state of a person, idea or thing toward maturity.",
    "Editing – Correcting, revising, or refining written materials and other media.",
    "Empathizing – Sympathizing, understanding, or identifying with another’s situation or need.",
    "Encouraging – Inspiring, strengthening, or energizing others toward excellence and endurance.",
    "Entertaining – Hosting, welcoming, or showing hospitality toward guests.",
    "Envisioning – Imagining, conceiving, or visualizing future events and accomplishments.",
    "Experimenting - Testing, exploring, or investigating to gain experience, discover the unknown, or to prove something.",
    "Facilitating – Assisting, enabling, or furthering an action or process a person or organization is involved in.",
    "Farming – Planting, tending, harvesting crops.",
    "Gardening – Working with soil, growing plants, flowers, or trees.",
    "Helping – Serving, assisting, or aiding others, meeting their practical needs.",
    "Implementing – Executing, carrying out, or enforcing programs, procedures, or plans.",
    "Influencing – Persuading, guiding, or affecting people, policies, or organizations.",
    "Instructing – Teaching, educating, or enlightening learners to facts and concepts through a variety of means.",
    "Leading – Guiding, influencing, or motivating people and organizations toward common goals.",
    "Learning – Grasping, discerning, and ascertaining knowledge or skills.",
    "Listening – Hearing, grasping, or giving attention to the communication of others in order to gain understanding.",
    "Making Music – Creating, performing, arranging, or conducting music.",
    "Managing – Supervising, directing, or guiding people, projects and resources to reach objectives.",
    "“Mechanicing” – Working with machines, motors, or equipment.",
    "Mentoring – Advising, discipling, or coaching individuals toward excellence in a given area in a caring environment.",
    "Motivating – Inspiring, prompting, and stimulating individuals and organizations toward positive action.",
    "Networking – linking, connecting, or associating individuals or groups in a supportive relationship involving a common interest.",
    "Nurturing – Supporting, encouraging, and cultivating growth and development in individuals or groups.",
    "Operating Equipment – Driving, maneuvering, handling equipment for construction and vehicles for transportation.",
    "Performing – Acting, singing, speaking, playing an instrument or sport in the presence of an audience.",
    "Persevering – Enduring, persevering, persisting in an effort in spite of obstacles.",
    "Pioneering – Initiating, innovating, and trailblazing in an enterprise or field of study.",
    "Playing Sports – Demonstrating athletic ability, physical coordination, and strength.",
    "Predicting – Forecasting, anticipating, or projecting future trends and conditions.",
    "Promoting – Advancing, supporting, or furthering a person, group, cause, or ideology.",
    "Rebuilding – Repairing, restoring, and mending things.",
    "Recruiting – Enlisting, drafting, or mobilizing people or resources to serve in accomplishing a task.",
    "Refining – Improving, developing, or enhancing procedures, projects, organizations, or communication.",
    "Relating – Socializing, associating, or connecting with individuals of diverse backgrounds and interests.",
    "Researching – Studying, investigating, or examining a subject in order to gain new knowledge or applications of what is already known.",
    "Selling – Convincing, persuading, or marketing ideas, products, or services.",
    "Speaking – Communicating, conversing, or conveying information with individuals or a group.",
    "Strategizing – Planning, designing, or formulating in advance purposes and activities to accomplish a goal.",
    "Synthesizing – Integrating, unifying, and harmonizing information from various sources into a concise new understanding.",
    "Systematizing – Organizing, arranging, or grouping things and people into a functional structure.",
    "Theorizing – Philosophizing, speculating, conjecturing about life, religion, faith, science, and other matters.",
    "Working with Animals – Training, caring for, befriending animals.",
    "Working in a Craft – making, manufacturing, designing objects requiring manual skill.",
    "Writing – Composing, recording, or communicating through written language in documents.",
]


form_data = {
    "properties[title]": "Natural Abilities",
    "properties[height]": "600",
    "emails[0][type]": "notification",
    "emails[0][name]": "notification",
    "emails[0][from]": "default",
    "emails[0][to]": "noreply@jotform.com",
    "emails[0][subject]": "New Submission",
    "emails[0][html]": "false",
    "questions[0][headerType]": "Large",
    "questions[0][imageAlign]": "Left",
    "questions[0][name]": "heading",
    "questions[0][order]": "1",
    "questions[0][qid]": "1",
    "questions[0][text]": "Natural Abilities Survey",
    "questions[0][textAlign]": "Left",
    "questions[0][type]": "control_head",
    "questions[0][verticalTextAlign]": "Middle",
    "questions[1][compoundHint]": "",
    "questions[1][description]": "",
    "questions[1][labelAlign]": "Auto",
    "questions[1][middle]": "No",
    "questions[1][name]": "name",
    "questions[1][order]": "2",
    "questions[1][prefix]": "No",
    "questions[1][prefixChoices]": "",
    "questions[1][qid]": "2",
    "questions[1][readonly]": "No",
    "questions[1][required]": "Yes",
    "questions[1][sublabels][prefix]": "Prefix",
    "questions[1][sublabels][first]": "First Name",
    "questions[1][sublabels][middle]": "Middle Name",
    "questions[1][sublabels][last]": "Last Name",
    "questions[1][sublabels][suffix]": "Suffix",
    "questions[1][suffix]": "No",
    "questions[1][text]": "Name",
    "questions[1][type]": "control_fullname",
    "questions[2]allowCustomDomains]": "No",
    "questions[2][allowedDomains]": "",
    "questions[2][autoFixed]": "No",
    "questions[2][confirmation]": "No",
    "questions[2][confirmationHint]": "example@example.com",
    "questions[2][confirmationSublabel]": "Confirm Email",
    "questions[2][defaultValue]": "",
    "questions[2][description]": "",
    "questions[2][disallowFree]": "No",
    "questions[2][domainCheck]": "No",
    "questions[2][hint]": "",
    "questions[2][labelAlign]": "Top",
    "questions[2][maxsize]": "",
    "questions[2][name]": "email",
    "questions[2][order]": "3",
    "questions[2][qid]": "3",
    "questions[2][readonly]": "No",
    "questions[2][required]": "Yes",
    "questions[2][shrink]": "Yes",
    "questions[2][size]": "310",
    "questions[2][subLabel]": "example@example.com",
    "questions[2][text]": "Email",
    "questions[2][type]": "control_email",
    "questions[2][validation]": "Email",
    "questions[2][verificationCode]": "No",
    "questions[3][autoFixed]": "No",
    "questions[3][defaultValue]": "",
    "questions[3][description]": "",
    "questions[3][hint]": "",
    "questions[3][inputTextMask]": "",
    "questions[3][labelAlign]": "Top",
    "questions[3][maxsize]": "",
    "questions[3][name]": "studentId",
    "questions[3][order]": "4",
    "questions[3][qid]": "4",
    "questions[3][readonly]": "No",
    "questions[3][required]": "Yes",
    "questions[3][shrink]": "Yes",
    "questions[3][size]": "310",
    "questions[3][subLabel]": "",
    "questions[3][text]": "Student ID #",
    "questions[3][type]": "control_textbox",
    "questions[3][validation]": "None",
    "questions[4][name]": "input4",
    "questions[4][order]": "5",
    "questions[4][qid]": "5",
    "questions[4][text]": "<p>Consider the following descriptions of natural abilities.  Using the scale of 1 – 5, mark the answer which most accurately describes the presence of each ability in your life.  To save time, consider only the main bold words.  Read the sentence if further clarity is needed.  There are no “right” or “wrong” answers. </p>\r\n<p>Agreement Legend:</p>\r\n<p>1 - Not At All</p>\r\n<p>2 - A little</p>\r\n<p>3 - Moderately</p>\r\n<p>4 - Considerably</p>\r\n<p>5 - Strongly</p>",
    "questions[4][type]": "control_text",
}

index = 5
question_number = 1
condition_index = 0
for question in quesitons:
    ## The question itself
    form_data[f"questions[{index}][description]"] = ""
    form_data[f"questions[{index}][fromText]"] = "Not At All"
    form_data[f"questions[{index}][labelAlign]"] = "Auto"
    form_data[f"questions[{index}][name]"] = f"question{question_number}"
    form_data[f"questions[{index}][order]"] = f"{index + 1}"
    form_data[f"questions[{index}][qid]"] = f"{index + 1}"
    form_data[f"questions[{index}][required]"] = "Yes"
    form_data[f"questions[{index}][scaleAmount]"] = "5"
    form_data[f"questions[{index}][scaleFrom]"] = "1"
    form_data[f"questions[{index}][text]"] = question
    form_data[f"questions[{index}][toText]"] = "Strongly"
    form_data[f"questions[{index}][type]"] = "control_scale"
    index += 1
    question_id = int(index)
    ## 4 Rating field
    # form_data[f"questions[{index}][hidden]"] = "Yes"
    form_data[f"questions[{index}][autoFixed]"] = "No"
    form_data[f"questions[{index}][defaultValue]"] = ""
    form_data[f"questions[{index}][description]"] = ""
    form_data[f"questions[{index}][hint]"] = ""
    form_data[f"questions[{index}][inputTextMask]"] = ""
    form_data[f"questions[{index}][labelAlign]"] = "Auto"
    form_data[f"questions[{index}][maxsize]"] = ""
    form_data[f"questions[{index}][qid]"] = f"{index + 1}"
    form_data[f"questions[{index}][order]"] = f"{index + 1}"
    form_data[f"questions[{index}][name]"] = f"4onquestion{question_number}"
    form_data[f"questions[{index}][required]"] = "No"
    form_data[f"questions[{index}][size]"] = "310"
    form_data[f"questions[{index}][readonly]"] = "No"
    form_data[f"questions[{index}][subLabel]"] = ""
    form_data[f"questions[{index}][text]"] = f"Q{question_number} rated 4?"
    form_data[f"questions[{index}][validation]"] = "None"
    form_data[f"questions[{index}][type]"] = "control_textbox"
    index += 1
    id_4_rating = int(index)
    ## 5 Rating field
    # form_data[f"questions[{index}][hidden]"] = "Yes"
    form_data[f"questions[{index}][autoFixed]"] = "No"
    form_data[f"questions[{index}][defaultValue]"] = ""
    form_data[f"questions[{index}][description]"] = ""
    form_data[f"questions[{index}][hint]"] = ""
    form_data[f"questions[{index}][inputTextMask]"] = ""
    form_data[f"questions[{index}][labelAlign]"] = "Auto"
    form_data[f"questions[{index}][maxsize]"] = ""
    form_data[f"questions[{index}][qid]"] = f"{index + 1}"
    form_data[f"questions[{index}][order]"] = f"{index + 1}"
    form_data[f"questions[{index}][name]"] = f"5onquestion{question_number}"
    form_data[f"questions[{index}][required]"] = "No"
    form_data[f"questions[{index}][size]"] = "310"
    form_data[f"questions[{index}][readonly]"] = "No"
    form_data[f"questions[{index}][subLabel]"] = ""
    form_data[f"questions[{index}][text]"] = f"Q{question_number} rated 5?"
    form_data[f"questions[{index}][validation]"] = "None"
    form_data[f"questions[{index}][type]"] = "control_textbox"
    index += 1
    id_5_rating = int(index)

    # ## Condition for 4
    print(f"Adding condition {condition_index}")
    print(f"When Q{question_id} is 4, add question text into field {id_4_rating}")
    form_data[f"properties[conditions][{condition_index}][type]"] = "calculation"
    form_data[f"properties[conditions][{condition_index}][action]"] = (
        '[{"replaceText":"","readOnly":false,"newCalculationType":true,"allowZeroCopy":true,"useCommasForDecimals":false,"operands":"","equation":"%s","showBeforeInput":false,"showEmptyDecimals":false,"ignoreHiddenFields":false,"insertAsText":false,"resultField":"%d","decimalPlaces":"2","isError":false}]'
        % (question, id_4_rating)
    )
    form_data[f"properties[conditions][{condition_index}][priority]"] = (
        f"{condition_index}"
    )
    form_data[f"properties[conditions][{condition_index}][index]"] = (
        f"{condition_index}"
    )
    form_data[f"properties[conditions][{condition_index}][link]"] = "Any"
    form_data[f"properties[conditions][{condition_index}][terms]"] = (
        '[{"field":"%d","operator":"equals","value":"4","isError":false}]'
        % (question_id)
    )
    condition_index += 1

    ## Condition for 5
    # print(f"Adding condition {condition_index}")
    # print(f"When Q{question_id} is 5, add question text into field {id_5_rating}")
    form_data[f"properties[conditions][{condition_index}][type]"] = "calculation"
    form_data[f"properties[conditions][{condition_index}][action]"] = (
        '[{"replaceText":"","readOnly":false,"newCalculationType":true,"allowZeroCopy":true,"useCommasForDecimals":false,"operands":"","equation":"%s","showBeforeInput":false,"showEmptyDecimals":false,"ignoreHiddenFields":false,"insertAsText":false,"resultField":"%d","decimalPlaces":"2","isError":false, "id": "action_%d"}]'
        % (question, id_5_rating, randint(1000000000000, 9999999999999))
    )
    form_data[f"properties[conditions][{condition_index}][priority]"] = (
        f"{condition_index}"
    )
    form_data[f"properties[conditions][{condition_index}][index]"] = (
        f"{condition_index}"
    )
    form_data[f"properties[conditions][{condition_index}][link]"] = "Any"
    form_data[f"properties[conditions][{condition_index}][terms]"] = (
        '[{"field":"%d","operator":"equals","value":"5","isError":false, "id": "term_%d"}]'
        % (question_id, randint(1000000000000, 9999999999999))
    )
    condition_index += 1
    question_number += 1


url = f"https://api.jotform.com/form?apiKey={api_key}"
response = requests.request("POST", url, data=form_data)

print(response)
print(response.text)
response_json = json.loads(response.text)
print(response_json)
