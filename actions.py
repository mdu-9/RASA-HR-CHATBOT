from typing import Any, Text, Dict, List ## Datatypes

from rasa_sdk import Action, Tracker
from rasa_sdk.executor  import CollectingDispatcher

class action_form(Action):

    def name(self) -> Text:
        return "action_form"

    def run(self, dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        post = tracker.get_slot('post')
        salary = tracker.get_slot('salary')
        experience = tracker.get_slot('experience')
        skills = tracker.get_slot('skills')


        dispatcher.utter_message(text='Form is printed.')
        dispatcher.utter_message(text='''New job post: \n We are hiring!! *******************\n Name of Post: '''+ str(post) + '\n Salary: ' + str(salary) + '''\n Required Experience: '''+ str(experience) + '\n Minimum Required Skills: ' + str(skills))
         

        return []

